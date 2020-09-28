from Cryptodome.Cipher import AES


# AES ->  pelo menos 128 bits, mas pode ser também 192 ou 256 (mas não maior que 256)
# 128b / 16 letras
# 192b / 24 letras
# 256b / 32 letras

def encript(key, text):
    if (len(key) != 16) and (len(key) != 24) and (len(key) != 32):
        return 'Forneça uma chave valida(texto de 16, 24 ou 32 letras)'

    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX, nonce=b'poiuytrewqasdfgh')
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return ''.join([chr(x) for x in list(ciphertext)]).replace('\r', '\\r')


def decript(key, text):
    if (len(key) != 16) and (len(key) != 24) and (len(key) != 32):
        return 'Forneça uma chave valida(texto de 16, 24 ou 32 letras)'

    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX, nonce=b'poiuytrewqasdfgh')
    texto = bytes(bytearray([ord(x) for x in text.replace('\\r', '\r')]))
    ciphertext = cipher.decrypt(texto)
    return ciphertext.decode('utf-8')


