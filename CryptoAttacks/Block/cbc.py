from CryptoAttacks.Utils import *


def padding_oracle(payload, iv):
    """Function implementing padding oracle

    Args:
        payload(string): ciphertext to check
        iv(string): initialization vector (most often: append it at beginning of payload)

    Returns:
        bool: True if padding is correct, False otherwise
    """
    raise NotImplementedError


def decryption_oracle(block):
    """Function implementing decryption oracle. Have to work with ciphertexts that decrypt to
    incorrectly padded plaintexts, so before decryption you should append two blocks
    that will decrypt to something with valid padding, and return properly stripped plaintext

    Args:
        block(string): ciphertext to decrypt

    Returns:
        string: decrypted ciphertext (don't strip with padding)
    """
    raise NotImplementedError


def _check_oracles(padding_oracle=None, decryption_oracle=None, block_size=16):
    """Check if padding or decryption oracle works"""
    if not padding_oracle and not decryption_oracle:
        log.critical_error("Give padding_oracle and/or decryption_oracle functions")

    if decryption_oracle:
        try:
            decryption_oracle('B' * block_size)
        except NotImplementedError:
            log.critical_error("decryption_oracle not implemented")
        except Exception, e:
            log.critical_error("Error in first call to decryption_oracle: {}".format(e.message))

    if padding_oracle:
        try:
            padding_oracle(payload='B'*block_size, iv='A'*block_size)
        except NotImplementedError:
            log.critical_error("padding_oracle not implemented")
        except Exception, e:
            log.critical_error("Error in first call to padding_oracle: {}".format(e.message))


def decrypt(ciphertext, padding_oracle=None, decryption_oracle=None, iv=None, block_size=16,
            is_correct=True, amount=0, known_plaintext=None, async=False):
    """Decrypt ciphertext
    Give padding_oracle or decryption_oracle (or both)

    Args:
        ciphertext(string): to decrypt
        padding_oracle(function/None)
        decryption_oracle(function/None)
        iv(string): if not specified, first block of ciphertext is treated as iv
        block_size(int)
        is_correct(bool): set if ciphertext will decrypt to something with correct padding
        amount(int): how much blocks decrypt (counting from last), zero (default) means all
        known_plaintext(string): with padding, from end
        async(bool): make asynchronous calls to oracle (not implemented yet)

    Returns:
        plaintext(string): with padding
    """
    _check_oracles(padding_oracle=padding_oracle, decryption_oracle=decryption_oracle, block_size=block_size)

    if decryption_oracle:
        if not iv:
            ciphertext = ciphertext[block_size:]
        blocks = chunks(ciphertext, block_size)[::-1]  # from last
        plaintext = []
        for block in blocks:
            plaintext.append(decryption_oracle(block))
            if amount !=0 and len(plaintext) == amount:
                break
        return ''.join(plaintext[::-1]) 

    if block_size % 8 != 0:
        log.critical_error("Incorrect block size: {}".format(block_size))

    log.info("Start cbc padding oracle")
    log.debug(print_chunks(chunks(ciphertext, block_size)))

    if len(ciphertext) % block_size != 0:
        log.critical_error("Incorrect ciphertext length: {}".format(len(ciphertext)))

    # prepare blocks
    blocks = chunks(ciphertext, block_size)
    if iv:
        if len(iv) % block_size != 0:
            log.critical_error("Incorrect iv length: {}".format(len(iv)))
        log.info("Set iv")
        blocks.insert(0, iv)

    if amount != 0:
        amount = len(blocks) - amount - 1
    if amount < 0 or amount >= len(blocks):
        log.critical_error(
            "Incorrect amount of blocks to decrypt: {} (have to be in [0,{}]".format(amount, len(blocks) - 1))
    log.info("Will decrypt {} block(s)".format(len(blocks) - 1 - amount))

    # add known plaintext
    plaintext = ''
    position_known = 0
    if known_plaintext:
        is_correct = False
        plaintext = known_plaintext
        blocks_decoded = len(plaintext) // block_size
        chars_decoded = len(plaintext) % block_size

        if blocks_decoded == len(blocks):
            log.debug("Nothing decrypted, known plaintext long enough")
            return plaintext
        if blocks_decoded > len(blocks) - 1:
            log.critical_error("Too long known plaintext ({} blocks)".format(blocks_decoded))

        if blocks_decoded != 0:
            blocks = blocks[:-blocks_decoded]
        if chars_decoded != 0:
            blocks[-2] = blocks[-2][:-chars_decoded] + xor(plaintext[:chars_decoded], blocks[-2][-chars_decoded:],
                                                           chr(chars_decoded + 1))
        position_known = chars_decoded
        log.info("Have known plaintext, skip {} block(s) and {} bytes".format(blocks_decoded, chars_decoded))

    for count_block in xrange(len(blocks) - 1, amount, -1):
        """ Blocks from the last to the second (all except iv)"""
        log.info("Block no. {}".format(count_block))

        payload_prefix = ''.join(blocks[:count_block - 1])
        payload_modify = blocks[count_block - 1]
        payload_decrypt = blocks[count_block]

        position = block_size - 1 - position_known
        position_known = 0
        while position >= 0:
            """ Every position in block, from the end"""
            log.debug("Position: {}".format(position))

            found_correct_char = False
            for guess_char in xrange(256):
                modified = payload_modify[:position] + chr(guess_char) + payload_modify[position + 1:]
                payload = ''.join([payload_prefix, modified, payload_decrypt])

                iv = payload[:block_size]
                payload = payload[block_size:]
                log.debug(print_chunks(chunks(iv + payload, block_size)))

                correct = padding_oracle(payload=payload, iv=iv)
                if correct:
                    """ oracle returns True """
                    padding = block_size - position  # sent ciphertext decoded to that padding
                    decrypted_char = chr(ord(payload_modify[position]) ^ guess_char ^ padding)

                    if is_correct:
                        """ If we didn't send original ciphertext, then we have found original padding value.
                            Otherwise keep searching and if won't find any other correct char - padding is \x01
                        """
                        if guess_char == ord(blocks[-2][-1]):
                            log.debug("Skip this guess char ({})".format(guess_char))
                            continue

                        dc = ord(decrypted_char)
                        log.info("Found padding value for correct ciphertext: {}".format(dc))
                        if dc == 0 or dc > block_size:
                            log.critical_error("Found bad padding value (given ciphertext may not be correct)")

                        plaintext = decrypted_char * dc
                        payload_modify = payload_modify[:-dc] + xor(payload_modify[-dc:], decrypted_char, chr(dc + 1))
                        position = position - dc + 1
                        is_correct = False
                    else:
                        """ abcd efgh ijkl o|guess_char|xy  || 1234 5678 9tre qwer - ciphertext
                            what ever itma ybex             || xyzw rtua lopo k|\x03|\x03\x03 - plaintext
                            abcd efgh ijkl |guess_char|wxy  || 1234 5678 9tre qwer - next round ciphertext
                            some thin gels eheh             || xyzw rtua lopo guessing|\x04\x04\x04 - next round plaintext
                        """
                        if position == block_size - 1:
                            """ if we decrypt first byte, check if we didn't hit other padding than \x01 """
                            payload = iv + payload
                            payload = payload[:-block_size - 2] + 'A' + payload[-block_size - 1:]
                            iv = payload[:block_size]
                            payload = payload[block_size:]
                            correct = padding_oracle(payload=payload, iv=iv)
                            if not correct:
                                log.debug("Hit false positive, guess char({})".format(guess_char))
                                continue

                        payload_modify = payload_modify[:position] + xor(
                            chr(guess_char) + payload_modify[position + 1:], chr(padding), chr(padding + 1))
                        plaintext = decrypted_char + plaintext

                    found_correct_char = True
                    log.debug(
                        "Guessed char(\\x{:02x}), decrypted char(\\x{:02x})".format(guess_char, ord(decrypted_char)))
                    log.debug("Plaintext: {}".format(plaintext))
                    log.info("Plaintext(hex): {}".format(b2h(plaintext)))
                    break
            position -= 1
            if found_correct_char is False:
                if is_correct:
                    padding = 0x01
                    payload_modify = payload_modify[:position + 1] + xor(payload_modify[position + 1:], chr(padding),
                                                                         chr(padding + 1))
                    plaintext = "\x01"
                    is_correct = False
                else:
                    log.critical_error("Can't find correct padding (oracle function return False 256 times)")
    log.success("Decrypted(hex): {}".format(b2h(plaintext)))
    return plaintext


def fake_ciphertext(new_plaintext, padding_oracle=None, decryption_oracle=None, original_ciphertext=None,
                    iv=None, original_plaintext=None, block_size=16):
    """Make ciphertext that will decrypt to given plaintext
    Give padding_oracle or decryption_oracle (or both)

    Args:
        new_plaintext(string): with padding
        padding_oracle(function/None)
        decryption_oracle(function/None): maximum one block to decrypt
        original_ciphertext(string): have to be correct,
                                    len(new_plaintext) == len(original_ciphertext)+len(iv)-len(block_size)
        iv(string): if not specified, first block of ciphertext is treated as iv
        original_plaintext(string): corresponding to original_ciphertext, with padding,
                                    only last len(block_size) bytes will be used
        block_size(int)

    Returns:
        fake_ciphertext(string): fake ciphertext that will decrypt to new_plaintext
    """
    _check_oracles(padding_oracle=padding_oracle, decryption_oracle=decryption_oracle, block_size=block_size)

    if block_size % 8 != 0:
        log.critical_error("Incorrect block size: {}".format(block_size))

    log.info("Start fake ciphertext")

    if original_ciphertext is None:
        if original_plaintext:
            log.critical_error("Original plaintext given without original ciphertext")
        if iv:
            log.critical_error("iv given without original ciphertext")
        ciphertext = 'A' * (len(new_plaintext) + block_size)
    else:
        ciphertext = original_ciphertext

    if original_ciphertext and len(original_ciphertext) % block_size != 0:
        log.critical_error("Incorrect original ciphertext length: {}".format(len(original_ciphertext)))
    if len(new_plaintext) % block_size != 0:
        log.critical_error("Incorrect new plaintext length: {}".format(len(new_plaintext)))

    # prepare blocks
    blocks = chunks(ciphertext, block_size)
    new_pl_blocks = chunks(new_plaintext, block_size)
    if iv:
        log.info("Set iv")
        blocks.insert(0, iv)
    if len(new_pl_blocks) != len(blocks) - 1:
        log.critical_error(
            "Wrong new plaintext length({}), should be {}".format(len(new_plaintext), block_size * (len(blocks) - 1)))
    new_ct_blocks = list(blocks)

    # add known plaintext
    if original_plaintext:
        if original_plaintext > block_size:
            log.info("Cut original plaintext from {} to last {} bytes".format(len(original_plaintext), block_size))
            original_plaintext = original_plaintext[-block_size:]

    for count_block in xrange(len(blocks) - 1, 0, -1):
        """ Every block, modify block[count_block-1] to set block[count_block] """
        log.info("Block no. {}".format(count_block))

        ciphertext_to_decrypt = ''.join(new_ct_blocks[:count_block + 1])

        if original_plaintext is None and original_ciphertext is None:
            original_plaintext = decrypt(ciphertext_to_decrypt, padding_oracle=padding_oracle, decryption_oracle=decryption_oracle,
                                         block_size=block_size, amount=1, is_correct=False)
        elif original_plaintext and original_ciphertext:
            original_plaintext = decrypt(ciphertext_to_decrypt, padding_oracle=padding_oracle, decryption_oracle=decryption_oracle,
                                         block_size=block_size, amount=1, is_correct=True, known_plaintext=original_plaintext)
        else:
            original_plaintext = decrypt(ciphertext_to_decrypt, padding_oracle=padding_oracle, decryption_oracle=decryption_oracle,
                                         block_size=block_size, amount=1, is_correct=True)

        log.info("Set block no. {}".format(count_block))
        new_ct_blocks[count_block - 1] = xor(blocks[count_block - 1], original_plaintext,
                                             new_pl_blocks[count_block - 1])
        original_plaintext = None
        original_ciphertext = None

    fake_ciphertext_res = ''.join(new_ct_blocks)
    log.success("Fake ciphertext(hex): {}".format(b2h(fake_ciphertext_res)))
    return fake_ciphertext_res


def bit_flipping(ciphertext, plaintext, wanted, block_size=16):
    """Given ciphertext and corresponding plaintext (two blocks) we can set first block of ciphertext
    so that last block of plaintext will be our wanted value

    Args:
        ciphertext(string): size == 2*block_size
        plaintext(string): size == block_size, plaintext of second ciphertext block
        wanted(string): size == block_size, we want ciphertext last block decrypt to this
        block_size(int)

    Returns:
        string: ciphertext that will decrypt to garbage_block+wanted_last_block
    """
    if len(ciphertext) != 2*block_size:
        log.critical_error("Incorrect ciphertext size")
    if len(plaintext) != block_size:
        log.critical_error("Incorrect plaintext size")
    if len(wanted) != block_size:
        log.critical_error("Incorrect wanted_last_block size")

    return xor(ciphertext[:block_size], plaintext, wanted) + ciphertext[block_size:]


def iv_as_key(padding_oracle=None, decryption_oracle=None, ciphertext=None, plaintext=None, block_size=16):
    """If iv is used as key, we can recover it using decryption (or padding) oracle
    Give padding_oracle or decryption_oracle or ciphertext and plaintext pair

    Args:
        padding_oracle(function/None)
        decryption_oracle(function/None)
        ciphertext(string/None): first block must be AES.encrypt(iv xor whatever),
                                 first block repeated at least once
        plaintext(string/None): with padding
        block_size(int)

    Returns:
        string: key (==iv)
    """
    # find positions of the same blocks
    appended = False
    ciphertext = chunks(ciphertext, block_size)
    try:
        position_second = ciphertext.index(ciphertext[0], 1)
    except:
        appended = True
        log.debug("Append first block to ciphertext")
        ciphertext.append(ciphertext[0])
        position_second = len(ciphertext) - 1
    log.debug("Position of the same block as the first is {}".format(position_second))

    if not plaintext or appended:
        _check_oracles(padding_oracle=padding_oracle, decryption_oracle=decryption_oracle, block_size=block_size)

        plaintext = decrypt(ciphertext[0] + ciphertext[position_second], padding_oracle=padding_oracle,
                            decryption_oracle=decryption_oracle, iv='A'*block_size,  # iv will be never used anyway
                            block_size=block_size, is_correct=False, amount=2)
        plaintext = chunks(plaintext, block_size)
    else:
        plaintext = chunks(plaintext, block_size)
        plaintext = [plaintext[0], plaintext[position_second]]

    key = xor(plaintext[0], ciphertext[position_second-1], plaintext[1])
    return key
