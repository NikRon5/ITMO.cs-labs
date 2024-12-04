def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for l in plaintext:
        if not l.isalpha():
            ciphertext += l
        elif l.isupper():
            ciphertext += chr((ord(l) - ord("A") + shift) % 26 + ord("A"))
        elif l.islower():
            ciphertext += chr((ord(l) - ord("a") + shift) % 26 + ord("a"))
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for l in ciphertext:
        if not l.isalpha():
            plaintext += l
        elif l.isupper():
            plaintext += chr((ord(l) - ord("A") - shift) % 26 + ord("A"))
        elif l.islower():
            plaintext += chr((ord(l) - ord("a") - shift) % 26 + ord("a"))
    return plaintext