

def encript(key, text):
    try:
        key = int(key)
    except ValueError:
        return 'Forneça uma chave valida(Valor inteiro)'
    return ''.join([chr(ord(x)+key) for x in text])


def decript(key, text):
    try:
        key = int(key)
    except ValueError:
        return 'Forneça uma chave valida(Valor inteiro)'
    return ''.join([chr(ord(x) - key) for x in text])
