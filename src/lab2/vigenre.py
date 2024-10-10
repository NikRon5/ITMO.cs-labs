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
        shift = ord(keyword[i % len(keyword)].upper()) - 65
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
        elif plaintext[i].isupper():
            ciphertext += chr((ord(plaintext[i]) - 65 + shift) % 26 + 65)
        elif plaintext[i].islower():
            ciphertext += chr((ord(plaintext[i]) - 97 + shift) % 26 + 97)
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
        shift = ord(keyword[i % len(keyword)].upper()) - 65
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
        elif ciphertext[i].isupper():
            plaintext += chr((ord(ciphertext[i]) - 65 - shift) % 26 + 65)
        elif ciphertext[i].islower():
            plaintext += chr((ord(ciphertext[i]) - 97 - shift) % 26 + 97)
    return plaintext