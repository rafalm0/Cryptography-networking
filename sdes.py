def encript(key, text):
    if len(key) <= 10:
        try:
            key = int(key, 2)
        except ValueError:
            return 'Forneça uma chave valida(Valor binario de 10 bits)'
    else:
        return 'Forneça uma chave valida(Valor binario de 10 bits)'
    x = sdes()
    x.set_key(key)
    return x.cript(text)


def decript(key, text):
    if len(key) <= 10:
        try:
            key = int(key, 2)
        except ValueError:
            return 'Forneça uma chave valida(Valor binario de 10 bits)'
    else:
        return 'Forneça uma chave valida(Valor binario de 10 bits)'
    x = sdes()
    x.set_key(key)
    return x.decript(text)


class sdes:

    def __init__(self):
        self.p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.p8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.ip = [2, 6, 3, 1, 4, 8, 5, 7]
        self.ip1 = [4, 1, 3, 5, 7, 2, 8, 6]
        self.ep = [4, 1, 2, 3, 2, 3, 4, 1]
        self.p4 = [2, 4, 3, 1]
        self.s0 = [[1, 0, 3, 2],
                   [3, 2, 1, 0],
                   [0, 2, 1, 3],
                   [3, 1, 3, 2]]
        self.s1 = [[0, 1, 2, 3],
                   [2, 0, 1, 3],
                   [3, 0, 1, 0],
                   [2, 1, 0, 3]]

        self.key = '0110001010'

    def set_key(self, chave):
        chave2 = bin(chave)[2:]
        if len(chave2) > 10:
            print('Tamanho de chave inválido, por favor forneça uma chave de 10 bits')
            return
        self.key = bin(chave)[2:].rjust(10, '0')

    def Fip(self, inpt):
        output = []
        for x in self.ip:  # 2,6,3,1,4,8,5,7
            output.append(inpt[x - 1])
        return output[:4], output[4:]

    def Fip1(self, inpt1, inpt2):
        inpt = inpt1 + inpt2
        output = []
        for x in self.ip1:  # 4, 1, 3, 5, 7, 2, 8, 6
            output.append(inpt[x - 1])
        return output

    def Fep(self, inpt):
        output = []
        for x in self.ep:  # 4,1,2,3,2,3,4,1
            output.append(inpt[x - 1])
        return output

    def xor8(self, inpt: list, key: int):
        output = int(''.join(inpt), 2)
        output = output ^ key
        output = bin(output)[2:].rjust(8, '0')
        output = [l for l in output]
        return output[:4], output[4:]

    def xor4(self, inpt1: list, inpt2: list):

        x1 = int(''.join(inpt1), 2)
        x2 = int(''.join(inpt2), 2)
        output = x1 ^ x2
        output = bin(output)[2:].rjust(4, '0')
        output = [l for l in output]
        return output

    def Fs0(self, inpt):
        inpt1 = int(''.join(inpt[0] + inpt[3]), 2)
        inpt2 = int(''.join(inpt[1:3]), 2)
        output = self.s0[inpt1][inpt2]
        output = bin(output)[2:].rjust(2, '0')
        return output

    def Fs1(self, inpt):
        inpt1 = int(''.join(inpt[0] + inpt[3]), 2)
        inpt2 = int(''.join(inpt[1:3]), 2)
        output = self.s1[inpt1][inpt2]
        output = bin(output)[2:].rjust(2, '0')
        return output

    def Fp4(self, inpt1, inpt2):
        inpt = inpt1 + inpt2
        output = []
        for x in self.p4:  # 2, 4, 3, 1
            output.append(inpt[x - 1])
        return output

    def Fk(self, inpt1, inpt2, key):
        output1 = self.xor4(inpt1, self.F(inpt2, key))
        output2 = inpt2
        return output1, output2

    def F(self, inpt, key):
        x = self.Fep(inpt)
        x0, x1 = self.xor8(x, key)
        x0 = self.Fs0(x0)
        x1 = self.Fs1(x1)
        output = self.Fp4(x0, x1)
        return output

    def shift1(self, inpt: list):
        return inpt[1:] + inpt[:1]

    def shift2(self, inpt: list):
        return inpt[2:] + inpt[:2]

    def Fp8(self, inpt1: list, inpt2: list):
        inpt = inpt1 + inpt2
        output = []
        for x in self.p8:  # 6,3,7,4,8,5,10,9
            output.append(inpt[x - 1])
        return output

    def Fp10(self, inpt):
        output = []
        for x in self.p10:  # 3,5,2,7,4,10,1,9,8,6
            output.append(inpt[x - 1])
        return output[:5], output[5:]

    def gen_key(self, key):
        out1, out2 = self.Fp10(key)  # P10

        out1 = self.shift1(out1)  # LS-1
        out2 = self.shift1(out2)  # LS-1

        k1 = self.Fp8(out1, out2)  # P8(K1)

        out1 = self.shift2(out1)  # LS-2
        out2 = self.shift2(out2)  # LS-2

        k2 = self.Fp8(out1, out2)  # P8(K2)
        return int(''.join(k1), 2), int(''.join(k2), 2)

    def encript_letra(self, text):
        text = self.bitfy(text)

        k1, k2 = self.gen_key(self.key)
        v1, v2 = self.Fip(text)
        v1, v2 = self.Fk(v1, v2, k1)
        v1, v2 = self.Fk(v2, v1, k2)
        output = self.Fip1(v1, v2)

        output = self.desbitfy(output)
        return output

    def decript_letra(self, text):
        text = self.bitfy(text)

        k1, k2 = self.gen_key(self.key)
        v1, v2 = self.Fip(text)
        v1, v2 = self.Fk(v1, v2, k2)
        v1, v2 = self.Fk(v2, v1, k1)
        output = self.Fip1(v1, v2)

        output = self.desbitfy(output)
        return output

    def bitfy(self, text):
        text = bin(ord(text))[2:].rjust(8, '0')
        text = [l for l in text]
        return text

    def desbitfy(self, bits):
        return chr(int(''.join(bits), 2))

    def cript(self, text):
        new_text = ''
        for letra in text:
            new_text += self.encript_letra(letra)
        return new_text

    def decript(self, text):
        new_text = ''
        for letra in text:
            new_text += self.decript_letra(letra)
        return new_text
