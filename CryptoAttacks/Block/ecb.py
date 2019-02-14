from __future__ import absolute_import, division, print_function

import string
from builtins import bytes, range

from CryptoAttacks.Math import factors
from CryptoAttacks.Utils import (add_padding, b2h, chunks, log, print_chunks,
                                 random_bytes)


def encryption_oracle(payload):
    """Function implementing encryption oracle with ecb mode

    Args:
        payload(string): raw data to encrypt

    Returns:
        string
    """
    raise NotImplementedError


def is_ecb(cipher, block_size=16):
    """Check if there are repeated blocks in ciphertext

    Args:
        cipher(string)
        block_size(int)

    Returns:
        bool: True if there are repeated blocks (so it's probably ECB mode)
    """
    cipher_blocks = chunks(cipher, block_size)
    unique_blocks = set(cipher_blocks)
    if len(unique_blocks) < len(cipher_blocks):
        return True
    return False


def find_block_size(encryption_oracle, constant=True):
    """Determine block size if ecb mode

    Args:
        encryption_oracle(callable)
        constant(bool): True if prefix and suffix have constant length

    Returns:
        int
    """
    if constant:
        log.debug("constant == True")
        payload = bytes(b'A')
        size = len(encryption_oracle(payload))
        while True:
            payload += bytes(b'A')
            new_size = len(encryption_oracle(payload))
            if new_size > size:
                log.info("block_size={}".format(new_size - size))
                return new_size - size
    else:
        log.debug("constant == False")
        payload = bytes(b'A')
        max_size = len(encryption_oracle(payload))
        possible_sizes = factors(max_size)
        possible_sizes.add(max_size)
        blocks_to_send = 5

        for block_size in sorted(possible_sizes):
            """send payload of length x, so at least x-1 blocks should be identical"""
            payload = random_bytes(1) * (blocks_to_send*block_size)
            enc_chunks = chunks(encryption_oracle(payload), block_size)
            for x in range(len(enc_chunks)-1):
                if enc_chunks[x] == enc_chunks[x+1]:
                    log.debug("Found two identical blocks at {}: {}".format(x, print_chunks(enc_chunks)))
                    for y in range(2, blocks_to_send-1):
                        if enc_chunks[x] != enc_chunks[x+y]:
                            break
                    else:
                        log.info("block_size={}".format(block_size))
                        return block_size


def find_prefix_suffix_size(encryption_oracle, block_size=16):
    """Determine prefix and suffix sizes if ecb mode, sizes must be constant
    Rarely may fail (if random data that are send unhappily matches prefix/suffix)

    Args:
        encryption_oracle(callable)
        block_size(int)

    Returns:
        tuple(int,int): prefix_size, suffix_size
    """
    blocks_to_send = 5
    payload = random_bytes(1) * (blocks_to_send * block_size)
    enc_chunks = chunks(encryption_oracle(payload), block_size)
    log.debug("Encryption of length {}".format(blocks_to_send * block_size))
    log.debug(print_chunks(enc_chunks))

    for position_start in range(len(enc_chunks) - 1):
        if enc_chunks[position_start] == enc_chunks[position_start + 1]:
            for y in range(2, blocks_to_send - 1):
                if enc_chunks[position_start] != enc_chunks[position_start + y]:
                    break
            else:
                log.success("Controlled payload start at chunk {}".format(position_start))
                break
    else:
        log.critical_error("Position of controlled chunks not found")

    log.info('Finding prefix')
    changed_char = bytes([(payload[0] - 1)%256])
    for aligned_bytes in range(block_size):
        payload_new = payload[:aligned_bytes] + changed_char + payload[aligned_bytes+1:]
        enc_chunks_new = chunks(encryption_oracle(payload_new), block_size)
        log.debug(print_chunks(chunks(payload_new, block_size)))
        log.debug(print_chunks(enc_chunks_new))
        if enc_chunks_new[position_start] != enc_chunks[position_start]:
            prefix_size = position_start*block_size - aligned_bytes
            log.success("Prefix size: {}".format(prefix_size))
            break
    else:
        log.critical_error("Size of prefix not found")

    log.info('Finding suffix')
    payload = random_bytes(1) * (block_size - (prefix_size % block_size))  # align to block_size
    encrypted = encryption_oracle(payload)
    suffix_size = len(encrypted) - len(payload) - prefix_size
    while True:
        payload += random_bytes(1)
        suffix_size -= 1
        if len(encryption_oracle(payload)) > len(encrypted):
            log.success("Suffix size: {}".format(suffix_size))
            break
    else:
        log.critical_error("Size of suffix not found")

    return prefix_size, suffix_size


def decrypt(encryption_oracle, constant=True, block_size=16, prefix_size=None, secret_size=None,
            alphabet=None):
    """Given encryption oracle which produce ecb(prefix || our_input || secret), find secret
    
    Args:
        encryption_oracle(callable)
        constant(bool): True if prefix have constant length (secret must have constant length)
        block_size(int/None)
        prefix_size(int/None)
        secret_size(int/None)
        alphabet(string): plaintext space
    
    Returns:
        secret(string)
    """
    log.debug("Start decrypt function")
    if not alphabet:
        alphabet = bytes(string.printable.encode())

    if not block_size:
        block_size = find_block_size(encryption_oracle, constant)

    if constant:
        log.debug("constant == True")
        if not prefix_size or not secret_size:
            prefix_size, secret_size = find_prefix_suffix_size(encryption_oracle, block_size)

        """Start decrypt"""
        secret = bytes(b'')
        aligned_bytes = random_bytes(1) * (block_size - (prefix_size % block_size))
        if len(aligned_bytes) == block_size:
            aligned_bytes = bytes(b'')

        aligned_bytes_suffix = random_bytes(1) * (block_size - (secret_size % block_size))
        if len(aligned_bytes_suffix) == block_size:
            aligned_bytes_suffix = bytes(b'')

        block_to_find_position = -1
        controlled_block_position = (prefix_size+len(aligned_bytes)) // block_size

        while len(secret) < secret_size:
            if (len(secret)+1) % block_size == 0:
                block_to_find_position -= 1
            payload = aligned_bytes + aligned_bytes_suffix + random_bytes(1) + secret
            enc_chunks = chunks(encryption_oracle(payload), block_size)
            block_to_find = enc_chunks[block_to_find_position]

            log.debug("To guess at position {}:".format(block_to_find_position))
            log.debug("Plain: " + print_chunks(chunks(bytes(b'P'*prefix_size) + payload + bytes(b'S'*secret_size), block_size)))
            log.debug("Encry: " + print_chunks(enc_chunks)+"\n")

            for guessed_char in range(256):
                guessed_char = bytes([guessed_char])
                payload = aligned_bytes + add_padding(guessed_char + secret, block_size)
                enc_chunks = chunks(encryption_oracle(payload), block_size)

                log.debug("Plain: " + print_chunks(chunks(bytes(b'P'*prefix_size) + payload + bytes(b'S'*secret_size), block_size)))
                log.debug("Encry: " + print_chunks(enc_chunks)+"\n")
                if block_to_find == enc_chunks[controlled_block_position]:
                    secret = guessed_char + secret
                    log.debug("Found char, secret={}".format(repr(secret)))
                    break
            else:
                log.critical_error("Char not found, try change alphabet. Secret so far: {}".format(repr(secret)))
        log.success("Secret(hex): {}".format(b2h(secret)))
        return secret
    else:
        log.debug("constant == False")


def known_plaintexts(pairs, ciphertext, block_size=16):
    """Given enough pairs plaintext-ciphertext, we can assign ciphertexts blocks to plaintexts blocks,
    then we can possibly decrypt ciphertext

    Args:
        pairs(list): list of dict, [{'cipher': 'aaa', 'plain': 'bbb'}, {'cipher': 'xxx', 'plain': 'pwa'}]
                     plaintexts have to be correctly padded (len(cipher) == len(plain))
        ciphertext(string): ciphertext to decrypt
        block_size(int)

    Returns
        tuple: ([decrypted_ciphertext_blocks], {'ciphertext_block': 'plaintext_block', ...})
        decrypted_ciphertext_blocks may contain not-decrypted blocks from ciphertext
    """
    result_mapping = {}
    for pair in pairs:
        ciphertext_blocks = chunks(pair['cipher'], block_size)
        plaintext_blocks = chunks(pair['plain'], block_size)
        if len(ciphertext_blocks) != len(plaintext_blocks):
            print(pair)
            print(ciphertext_blocks, plaintext_blocks)
            print(len(ciphertext_blocks), len(plaintext_blocks))
            assert 0
        for cipher_block_no in range(len(ciphertext_blocks)):
            result_mapping[ciphertext_blocks[cipher_block_no]] = plaintext_blocks[cipher_block_no]

    target_ciphertext_blocks = chunks(ciphertext, block_size)
    for cipher_block_no in range(len(target_ciphertext_blocks)):
        if target_ciphertext_blocks[cipher_block_no] in list(result_mapping.keys()):
            target_ciphertext_blocks[cipher_block_no] = result_mapping[target_ciphertext_blocks[cipher_block_no]]

    return target_ciphertext_blocks, result_mapping
