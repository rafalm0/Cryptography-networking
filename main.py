from sdes import sdes
from Cesar import Cesar_cypher
from xor import Xor
from des import DesKey
from Cryptodome.Cipher import AES

text = open('text.txt', 'r')


x1 = sdes()
x1.cript(text.read())
# x2 = Xor()
# x3 = Cesar_cypher()
# x4 = DesKey(b"chave")
# x5 = AES.new(b'chave', AES.MODE_EAX)


