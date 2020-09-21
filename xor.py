class Cesar_cypher:

    def __init__(self):
        self.chave = ord('a')

    def cript(self, text):
        return ''.join([chr(ord(letra) ^ self.chave) for letra in text])

    def decript(self, text):
        return self.cript(text)
