from CryptoAttacks.Math import factors
from CryptoAttacks.Utils import *


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
        encryption_oracle(function)
        constant(bool): True if prefix and suffix have constant length

    Returns:
        int
    """
    if constant:
        log.debug("constant == True")
        payload = 'A'
        size = len(encryption_oracle(payload))
        while True:
            payload += 'A'
            new_size = len(encryption_oracle(payload))
            if new_size > size:
                log.info("block_size={}".format(new_size - size))
                return new_size - size
    else:
        log.debug("constant == False")
        payload = 'A'
        max_size = len(encryption_oracle(payload))
        possible_sizes = factors(max_size)
        possible_sizes.add(max_size)
        blocks_to_send = 5

        for block_size in sorted(possible_sizes):
            """send payload of length x, so at least x-1 blocks should be identical"""
            payload = random_char() * (blocks_to_send*block_size)
            enc_chunks = chunks(encryption_oracle(payload), block_size)
            for x in xrange(len(enc_chunks)-1):
                if enc_chunks[x] == enc_chunks[x+1]:
                    log.debug("Found two identical blocks at {}: {}".format(x, print_chunks(enc_chunks)))
                    for y in xrange(2, blocks_to_send-1):
                        if enc_chunks[x] != enc_chunks[x+y]:
                            break
                    else:
                        log.info("block_size={}".format(block_size))
                        return block_size


def find_prefix_suffix_size(encryption_oracle, block_size=16):
    """Determine prefix and suffix sizes if ecb mode, sizes must be constant

    Args:
        encryption_oracle(function)
        block_size(int)

    Returns:
        tuple(int,int): prefix_size, suffix_size
    """
    blocks_to_send = 5
    payload = random_char() * (blocks_to_send * block_size)
    enc_chunks = chunks(encryption_oracle(payload), block_size)
    # log.debug("Encryption of {}".format(payload))
    # log.debug(print_chunks(enc_chunks))

    for position_start in xrange(len(enc_chunks) - 1):
        if enc_chunks[position_start] == enc_chunks[position_start + 1]:
            for y in xrange(2, blocks_to_send - 1):
                if enc_chunks[position_start] != enc_chunks[position_start + y]:
                    break
            else:
                log.debug("Controlled payload start at chunk {}".format(position_start))
                break
    else:
        log.critical_error("Position of controlled chunks not found")

    changed_char = chr(ord(payload[0])-1)
    for aligned_bytes in xrange(block_size):
        payload_new = payload[:aligned_bytes] + changed_char + payload[aligned_bytes+1:]
        enc_chunks_new = chunks(encryption_oracle(payload_new), block_size)
        # log.debug("Encryption of {}".format(payload_new))
        # log.debug(print_chunks(enc_chunks_new))
        if enc_chunks_new[position_start] != enc_chunks[position_start]:
            prefix_size = position_start*block_size - aligned_bytes
            log.info("Prefix size: {}".format(prefix_size))
            break
    else:
        log.critical_error("Size of prefix not found")

    payload = random_char() * (block_size - (prefix_size % block_size))  # align to block_size
    encrypted = encryption_oracle(payload)
    suffix_size = len(encrypted) - len(payload) - prefix_size
    while True:
        payload += random_char()
        suffix_size -= 1
        if len(encryption_oracle(payload)) > len(encrypted):
            log.info("Suffix size: {}".format(suffix_size))
            break
    else:
        log.critical_error("Size of suffix not found")

    return prefix_size, suffix_size


def decrypt(encryption_oracle, constant=True, block_size=16, prefix_size=None, secret_size=None,
            alphabet=None):
    """Given encryption oracle which produce ecb(prefix || our_input || secret), find secret
    
    Args:
        encryption_oracle(function)
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
        alphabet = string.printable

    if not block_size:
        block_size = find_block_size(encryption_oracle, constant)

    if constant:
        log.debug("constant == True")
        if not prefix_size or not secret_size:
            prefix_size, secret_size = find_prefix_suffix_size(encryption_oracle, block_size)

        """Start decrypt"""
        secret = ''
        aligned_bytes = random_char() * (block_size - (prefix_size % block_size))
        if len(aligned_bytes) == block_size:
            aligned_bytes = ''
        aligned_bytes_suffix = random_char() * (block_size - (secret_size % block_size))
        if len(aligned_bytes_suffix) == block_size:
            aligned_bytes_suffix = ''
        block_to_find_position = -1
        controlled_block_position = (prefix_size+len(aligned_bytes)) // block_size

        while len(secret) < secret_size:
            if (len(secret)+1) % block_size == 0:
                block_to_find_position -= 1
            payload = aligned_bytes + aligned_bytes_suffix + random_char() + secret
            enc_chunks = chunks(encryption_oracle(payload), block_size)
            block_to_find = enc_chunks[block_to_find_position]

            log.debug("To guess at position {}:".format(block_to_find_position))
            log.debug("Plain: " + print_chunks(chunks('P'*prefix_size+payload+'S'*secret_size, block_size)))
            log.debug("Encry: " + print_chunks(enc_chunks)+"\n")

            for guessed_char in alphabet:
                payload = aligned_bytes + add_padding(guessed_char + secret, block_size)
                enc_chunks = chunks(encryption_oracle(payload), block_size)

                log.debug("Plain: " + print_chunks(chunks('P' * prefix_size + payload + 'S' * secret_size, block_size)))
                log.debug("Encry: " + print_chunks(enc_chunks)+"\n")
                if block_to_find == enc_chunks[controlled_block_position]:
                    secret = guessed_char + secret
                    log.debug("Found char, secret={}".format(repr(secret)))
                    break
            else:
                log.critical_error("Char not found, try change alphabet. Secret so far: {}".format(repr(secret)))
        log.info("Secret(hex): {}".format(secret.encode('hex')))
        return secret
    else:
        log.debug("constant == False")

