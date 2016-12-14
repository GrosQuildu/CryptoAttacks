#!/usr/bin/env python

import string
from Utils import *


class ECB(object):
    def __init__(self, alphabet=string.printable+'\x01', block_size=False):
        self.block_size = block_size
        self.alphabet = alphabet

    def encryption_oracle(self, payload, **kwargs):
        """
        You have to implement wrapper around encryption function
            payload - raw plaintext to encrypt
        Return raw ciphertext
        """
        raise NotImplementedError

    def recognize(self, cipher):
        """
        Check if there are repeated blocks in ciphertext
        """
        cipher_blocks = chunks(cipher, 16)
        unique_blocks = len(set(cipher_blocks))
        if unique_blocks < len(cipher_blocks):
            return True
        return False

    def find_block_size(self, constant=True):
        """
        Determine block size
            constant - wheter prefix and suffif have constant length
        """
        log.debug("Start find_block_size method")
        if constant:
            log.debug("constant == True")
            payload = 'A'
            size = len(self.encryption_oracle(payload))
            log.debug("size {}: {}".format(size, payload))
            for x in xrange(2, 256):
                payload = 'a'*x
                new_size = len(self.encryption_oracle(payload))
                log.debug("new_size {}: {}".format(new_size, payload))
                if new_size > size:
                    size = new_size
                    log.debug("size=new_size")
                    """with payload of length size we created new blocks, but there could be prefix"""
                    for y in xrange(1, 256):
                        second_payload = payload + 'b'*y
                        new_size = len(self.encryption_oracle(second_payload))
                        log.debug("new_size {}: {}".format(new_size, second_payload))
                        if new_size > size:
                            self.block_size = y
                            return self.block_size
        else:
            log.debug("constant == False")
            payload = random_char()*256
            enc = self.encryption_oracle(payload)
            for block_size in xrange(4, 256):
                log.debug("block_size {}: enc_size {}".format(block_size, len(enc)))
                if len(enc) % block_size != 0:
                    continue
                enc_chunks = chunks(enc, block_size)
                for x in xrange(len(enc_chunks)-1):
                    """find two identical blocks (this may be our payload), then compare to next blocks - should be the same"""
                    if enc_chunks[x] == enc_chunks[x+1]:
                        log.debug("Found two identical blocks: {}".format(pretty_chunks(enc_chunks)))
                        match = True
                        for y in xrange(2, (len(payload)/block_size)-1):
                            if enc_chunks[x] != enc_chunks[x+y]:
                                match = False
                                break
                        if match:
                            self.block_size = block_size
                            return self.block_size
        return False

    def decrypt(self, constant=False, prefix_size=False, max_payload_length=False):
        """
        Given encryption function which produce ecb(prefix || our_input || secret), return secret
            constant - prefix constant length  (secret must be constant length)
        """
        log.debug("Start decrypt method")
        if not self.block_size:
            self.block_size = self.find_block_size(constant)
        if not max_payload_length:
            max_payload_length = 512*self.block_size
        log.info("Block size: {}".format(self.block_size))

        if max_payload_length < self.block_size:
            log.error("Max payload length is smaller than block size")
            sys.exit(1)

        if max_payload_length < self.block_size*3 and prefix_size==False:
            log.error("Max payload length is too small to find prefix size (min 3*bock_size)")
            sys.exit(1)

        if constant:
            log.debug("constant == True")
            """find size of prefix"""
            if not prefix_size:
                count = 0
                previous_position = -1
                aligned = False
                while count < 5:
                    payload = random_char()*(3*self.block_size)
                    enc = chunks(self.encryption_oracle(payload), self.block_size)
                    for x in xrange(len(enc)-2):
                        if enc[x] == enc[x+1]:
                            if enc[x] == enc[x+2]:
                                aligned = True
                            position = x
                            break
                    if position != previous_position and previous_position != -1:
                        count = 0
                        previous_position = -1
                        aligned = False
                    else:
                        count += 1
                        previous_position = position

                """payload block is aligned to block_size (start at new block)"""
                if aligned:
                    prefix_size = position*self.block_size
                else:
                    for x in xrange(1, self.block_size):
                        payload = random_char()*(3*self.block_size)
                        payload = payload[:-x]
                        enc = chunks(self.encryption_oracle(payload), self.block_size)
                        if enc[position] != enc[position+1]:
                            overflow = x-1
                            break
                    prefix_size = (position*self.block_size)-(self.block_size-overflow)
            log.info("Prefix size: {}".format(prefix_size))

            if max_payload_length - prefix_size < self.block_size:
                log.error("Max payload length is smaller than block size + prefix size")
                sys.exit(1)

            """Start decrypt"""
            prefix_align = random_char()*(self.block_size - prefix_size % self.block_size)
            if prefix_size%self.block_size == 0:
                prefix_align = ''
            position = (prefix_size+len(prefix_align))/self.block_size
            payload_position = position
            secret = ''
            cipher_len = len(chunks(self.encryption_oracle(prefix_align + random_char()*self.block_size), self.block_size))
            known_block = random_char()*self.block_size

            while position < cipher_len:
                secret_block = ''

                """decrypt one block"""
                for x in xrange(1, self.block_size+1):

                    """Get block with one char unknown"""
                    if position >= cipher_len:
                        return secret
                    found_char = False
                    payload = prefix_align + known_block[x:]
                    enc = chunks(self.encryption_oracle(payload), self.block_size)
                    to_decrypt = enc[position]
                    log.debug("Test: {}".format( b2h(payload) ))
                    log.debug("One unknown char: {}".format( pretty_chunks(enc) ))
                    log.debug("To decrypt: {}, position {}".format( b2h(to_decrypt), position ))

                    """Guess unknow char"""
                    guess_char = 0
                    while guess_char < len(self.alphabet) and found_char == False:
                        payload = prefix_align

                        """as much blocks at one time as can be"""
                        max_blocks = (max_payload_length - len(prefix_align)) / self.block_size
                        for i in xrange(min( max_blocks, len(self.alphabet)-guess_char )):
                            payload += known_block[x:] + secret_block + self.alphabet[guess_char+i]

                        enc = chunks(self.encryption_oracle(payload), self.block_size)
                        log.debug("Test: {}".format( b2h(payload) ))
                        log.debug("{}\n\n".format( pretty_chunks(enc) ))
                        for i in xrange(min( max_blocks, len(self.alphabet)-guess_char )):
                            if enc[payload_position+i] == to_decrypt:
                                found_char = True
                                secret_block += self.alphabet[guess_char+i]
                                log.info("Secret: {}".format(secret+secret_block))

                                """Found correct padding"""
                                if position == cipher_len-2 and secret_block[-1] == '\x01':
                                    secret += secret_block
                                    position += cipher_len
                                    return secret
                                break
                        guess_char += min( max_blocks, len(self.alphabet)-guess_char )
                    if not found_char:
                        log.warning("Can't guess block, maybe try another alphabet?")
                        return False
                secret += secret_block
                known_block = secret_block
                position += 1
            return secret

        else:
            log.debug("constant == False")
            secret = ''
            known_block = random_char()*self.block_size
            while True:
                payload = random_char()*(4*block_size) #need to find 3 same blocks, to know where our payload is
                payload += ''.join(known_block[x:]+guess_char for guess_char in self.alphabet)
                payload += known_block[random.randint(1, self.block_size):] #prefix-size is random, so rand align bytes
                return False
 