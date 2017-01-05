# One time pad

```python
from CryptoAttacks.Classic import one_time_pad

def compare_by_frequencies(a, b, lang='English', no_of_comparisons=5):
    """Check which text have more similar letter frequencies (compared to language)
    todo: add words, diagraphs etc...

    Args:
        a(string)
        b(string)
        lang(string)
        no_of_comparisons(int): how much letters compare

    Returns:
        int: -1 if a is less similar than b, 0 if equal, 1 if a is more similar
    """

def break_one_char_key(ciphertext, lang='English', no_of_comparisons=5, alphabet=False, key_space=False,
                       reliability=100.0):
    """Brute for all one-char keys, return most language-like

    Args:
        ciphertext(string): text xored with short key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, plaintext)
    """

def guess_key_size(ciphertext, max_key_size=40):
    """Given sentence xored with short key, guess key size
    From: http://trustedsignal.blogspot.com/2015/06/xord-play-normalized-hamming-distance.html

    Args:
         ciphertext(string)
         max_key_size(int)

    Returns:
        list: sorted list of tuples (key_size, probability),
        note that most probable key size not necessary have the largest probability
    """

def break_repeated_key(ciphertext, lang='English', no_of_comparisons=5, key_size=None, max_key_size=40,
                       alphabet=None, key_space=None, reliability=100.0):
    """Short key encrypted with long plaintext

    Args:
        ciphertext(string): text xored with short key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        key_size(int/None)
        max_key_size(int/None)
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, plaintext)
    """

def break_reuse_key(ciphertexts, lang='English', no_of_comparisons=5, alphabet=None,
                    key_space=None, reliability=100.0):
    """Sentences xored with the same key

    Args:
        ciphertexts(list): texts xored with the same key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, list(plaintexts))
    """
```
