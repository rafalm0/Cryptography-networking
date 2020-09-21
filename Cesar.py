class Cesar_cypher:

    def __init__(self):
        self.shift = 0

    def cript(self, text):
        return ''.join([chr(ord(x)+self.shift) for x in text])

    def decript(self, text):
        return ''.join([chr(ord(x) - self.shift) for x in text])
