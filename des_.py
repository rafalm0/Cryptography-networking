from des import DesKey


# DES -> 64 bits - 8B - letras


def encript(key, text):
    if len(key) != 8:
        return 'Forneça uma chave valida(8 caracteres)'
    key0 = DesKey(key.encode('utf-8'))
    texto_init = text.encode('utf-8')
    cipher_text = key0.encrypt(texto_init, padding=True)
    texto_amostra = ''.join([chr(x) for x in list(cipher_text)]).replace('\r', '\\r')
    return texto_amostra


def decript(key, text):
    key0 = DesKey(key.encode('utf-8'))
    texto_volta = bytes(bytearray([ord(x) for x in text.replace('\\r', '\r')]))
    decipher_text = key0.decrypt(texto_volta, padding=True)
    return decipher_text.decode('utf-8')



