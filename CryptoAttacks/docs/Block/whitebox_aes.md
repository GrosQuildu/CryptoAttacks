# WHITEBOX AES

```python
# Constants:
XorBox
Ty tables
mulby{1,2,3,9,11,13,14}
Sbox, Sbox_inv
mix_columns_matrix, inv_mix_columns_matrix

# AES FUNCTIONS
def shift_rows(state):
    """
    0   4   8   12
    1   5   9   13
    2   6   10  14
    3   7   11  15

    0   4   8   12
    5   9   13  1
    10  14  2   6
    15  3   7   11
    """
    
def sub_bytes(state):
    """
    0   4   8   12
    1   5   9   13
    2   6   10  14
    3   7   11  15

    Sbox[0]   Sbox[4]   Sbox[8]   Sbox[12]
    Sbox[1]   Sbox[5]   Sbox[9]   Sbox[13]
    Sbox[2]   Sbox[6]   Sbox[10]  Sbox[14]
    Sbox[3]   Sbox[7]   Sbox[11]  Sbox[15]
    """
    
def mix_columns(m):
    """
    for all columns:
    |d0|   |2 3 1 1|   |c0|
    |d1| = |1 2 3 1| * |c1|
    |d2|   |1 1 2 3|   |c2|
    |d3|   |3 1 1 2|   |c3|
    """
    
def key_schedule(key):
    """
    returns 11 round keys as 4x4 matrices
    """
    
def inv_key_schedule(key, round_no=10):
    """
    returns aes key from given round key
    """
    
def encrypt(state, key):
    """ Standard AES-128 encryption
    State: 4x4 matrix
    Key: 4x4 matrix
    """

# WHITEBOX
def generate_boxes(key):
    """Returns boxes used by whitebox AES:
    T-boxes
    Ty tables
    composed T and Ty boxes
    final (last) composed T box

    for dfa attack you need only last two
    """
    
def encrypt_whitebox(state, Tboxes, Tyboxes, TTyboxesComposed=None, TTyboxFinal=None):
    """
    state: matrix(4x4), plaintext
    Tboxes: T[round_no][byte_no][x] = Sbox[x ^^ shift_rows(k[round_no][byte_no])] -> 10*16*256
    Tyboxes: Ty[byte_in_column_no][x] -> 4*256
    TTyboxesComposed: TTyboxesComposed[round_no][byte_no][x] = Ty[byte_no%4][ T[round_no][byte_no][x] ] -> 9*16*256
    TTyboxFinal: Sbox[x ^^ shift_rows(k[last_round][byte_no])], if None Tboxes[-1] is used
    """
    
def recover_key_unprotected_wbaes(TTyboxesComposed, Tyboxes)
def recover_key_unprotected_wbaes_from_TTyboxFinal(TTyboxFinal, probes=3)


def dfa(TTyboxesComposed, TTyboxFinal, trials=5):
    """
    Differential fault analysis attack on whitebox AES-128
    
    trials: more trials, higher probability of key recovery, but takes more time


    k' = shift_rows(k)

    A ... ... ...
    B ... ... ...
    C ... ... ...
    D ... ... ...

    S[ 2.S[A+k'8,0] + 3.S[B+k'8,1] + S[C+k'8,2]   + S[D+k'8,3] + k'9,0 ] + k10,0
    ... ... ... S[ S[A+k'8,0]   + 2.S[B+k'8,1] + 3.S[C+k'8,2] + S[D+k'8,3] + k'9,7 ] + k10,7
    ... ... S[ S[A+k'8,0]   + S[B+k'8,1]   + 2.S[C+k'8,2] + 3.S[D+k'8,3] + k'9,10 ] + k10,10
    ... S[ 3.S[A+k'8,0] + S[B+k'8,1]   + S[C+k'8,2]   + 2.S[D+k'8,3] + k'9,13 ] + k10,13


    TTyboxesComposed[8][0] = Ty[0][X]  <-- fault in TTyboxesComposed

    S[ 2.X + 3.S[B+k'8,1] + S[C+k'8,2]   + S[D+k'8,3] + k'9,0 ] + k10,0
    ... ... ... S[ X   + 2.S[B+k'8,1] + 3.S[C+k'8,2] + S[D+k'8,3] + k'9,7 ] + k10,7
    ... ... S[ X   + S[B+k'8,1]   + 2.S[C+k'8,2] + 3.S[D+k'8,3] + k'9,10 ] + k10,10
    ... S[ 3.X + S[B+k'8,1]   + S[C+k'8,2]   + 2.S[D+k'8,3] + k'9,13 ] + k10,13
    
    From this equations we can compute candidates for key
    See https://eprint.iacr.org/2013/104.pdf for details
    """
```