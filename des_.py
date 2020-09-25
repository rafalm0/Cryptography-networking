from des import DesKey

def encript(key, text):

    key0 = DesKey(key)
    return key0.encrypt(text)

def decript(key, text):
    key0 = DesKey(key)
    return key0.decrypt(text)
