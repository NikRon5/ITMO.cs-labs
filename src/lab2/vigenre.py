def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
        elif plaintext[i].isupper():
            ciphertext += chr((ord(plaintext[i]) - ord("A") + shift) % 26 + ord("A"))
        elif plaintext[i].islower():
            ciphertext += chr((ord(plaintext[i]) - ord("a") + shift) % 26 + ord("a"))
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
        elif ciphertext[i].isupper():
            plaintext += chr((ord(ciphertext[i]) - ord("A") - shift) % 26 + ord("A"))
        elif ciphertext[i].islower():
            plaintext += chr((ord(ciphertext[i]) - ord("a") - shift) % 26 + ord("a"))
    return plaintext