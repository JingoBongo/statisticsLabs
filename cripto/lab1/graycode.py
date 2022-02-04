# so, the idea is: we already have base rc4 code and I don't want to repeat existing options
# in that case i will add layers to this cipher.



# functions to xor the plain and key and then to xor it back.
# it is very fast in both ways, so this would be just the first layer

# a = plain
# b = key
# c = a ^= b
# b = c ^= a
# a = c ^= b
# therefore
# to get from c to a we need
# a = c ^= b


def xor_the_plain(plain, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(plain,key))

def xor_the_cipher(cipher, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(cipher, key))



plain = 'summm text'
key = 'very_s3cr3t_key'
print('plain: %s' % plain)
xored_plain = xor_the_plain(plain, key)
print('xored plain: %s' % xored_plain)
xored_cipher = xor_the_cipher(xored_plain, key)
print('xored cipher: %s' % xored_cipher)


# alg = m.RC4_Basic()
# alg.key = key


