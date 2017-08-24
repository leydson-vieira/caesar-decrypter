# -*- encoding:utf-8 -*-
import string

class Decrypter(object):
    '''
    Utiliza da cifra de cesar para buscar padrões de decriptados de palavras
    '''

    def __init__(self, enc_word, enc_key):
        self.enc_word = enc_word
        self.enc_key = enc_key

    def decrypt(self):
        word = ''
        for letter in self.enc_word:
            word += chr(ord(letter) + self.enc_key)
        print word

if __name__ == "__main__":
    enc_word = input('Digite a frase encriptada: ')
    enc_key = input('Digite o número da chave: ')
    print '\n ---------- \n'
    d = Decrypter(enc_word.upper(), int(enc_key))
    d.decrypt()
