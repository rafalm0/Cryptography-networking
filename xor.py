def encript(key, text):
    if len(key) == 8:  # input em bits
        try:
            key = int(key, 2)
            return ''.join([chr(ord(letra) ^ key) for letra in text])
        except ValueError:
            pass

    try:  # input em numero
        key = int(key)
        return ''.join([chr(ord(letra) ^ key) for letra in text])
    except ValueError:
        pass

    try:  # input em letra
        key = ord(key)
        return ''.join([chr(ord(letra) ^ key) for letra in text])
    except TypeError:
        return 'Forneça uma chave valida(Valor inteiro ou caractere)'


def decript(key, text):
    return encript(key, text)
