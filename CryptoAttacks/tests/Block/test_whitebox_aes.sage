#!/usr/bin/env sage

from whitebox_aes_sage import *
from CryptoAttacks.Utils import *


def test_recover_key_unprotected_wbaes():
    for test_case in xrange(10):
        key = bytes_to_matrix(random_bytes(16))

        T = generate_tboxes(key)
        Ty = generate_tyboxes()
        TTy_composed = compose_T_Ty_boxes(T, Ty)

        key_recovered = recover_key_unprotected_wbaes(TTy_composed, Ty)
        assert key == key_recovered


def test_recover_key_from_TTyboxFinal():
    for test_case in xrange(10):
        key = bytes_to_matrix(random_bytes(16))

        T = generate_tboxes(key)

        key_recovered = recover_key_from_TTyboxFinal(T[-1])
        assert key == key_recovered


def test_dfa():
    for test_case in xrange(10):
        key = bytes_to_matrix(random_bytes(16))

        T = generate_tboxes(key)
        Ty = generate_tyboxes()
        TTy_composed = compose_T_Ty_boxes(T, Ty)

        key_recovered = dfa(TTy_composed, T[-1])
        assert key == key_recovered


if __name__ == "__main__":
    test_recover_key_unprotected_wbaes()
    test_recover_key_from_TTyboxFinal()
    test_dfa()
