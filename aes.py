from Cryptodome.Cipher import AES


def encript(key, text):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(bytes(text, 'utf-8'))
    return ciphertext


def decript(key, text):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.decrypt(text)
    return ciphertext
