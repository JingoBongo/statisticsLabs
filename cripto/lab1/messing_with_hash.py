import uuid
import base64

def encrypt2(message,key):
    return base64.decodebytes(bytes(([chr(message[i] ^ ord(key[i % len(key)]))
                                 for i in range(len(message))])), 'ascii')


def decrypt2(message,key):
    decoded = base64.decodebytes(message)
    return (chr(ord(decoded[i]) ^ ord(key[i % len(key)]))
                   for i in range(len(decoded)))

def ascii_encode(plain):
    return plain.encode('ascii')


def ascii_decode(encoded):
    return encoded.decode('ascii')

def xor_the_cipher(cipher, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(cipher, key))

string = 'N«%@Ý«_Jè	ÞlÓ:1644149439.686216:thekey'
byted_string = bytes(string, 'utf-8')
str2 = '1644149439.686216:thekey'
key = 'kek'

res = ascii_encode(str2)
print(res)
decoded = ascii_decode(res)
print(decoded)

# encoded = string.encode('utf-8')
# print(encoded)
#
# decoded = encoded.decode('utf-8')

# encoded = encrypt2(byted_string, key)
#
# decoded = decrypt2(encoded, key)
#
#
# print(decoded == string)