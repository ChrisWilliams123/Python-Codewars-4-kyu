#Solution to Codewars kata https://www.codewars.com/kata/54b72c16cd7f5154e9000457

import re

def decode_bits(bits):
    buffer = min(len(i) for i in re.findall(r'1+|0+', bits.strip("0")))
    return bits[::buffer].replace("111","-").replace("1",".").replace("0000000", '    ').replace('000', ' ').replace('0','')

def decode_morse(morseCode):
    return ' '.join("".join(MORSE_CODE[chr] for chr in word.split()) for word in morseCode.split('   '))
