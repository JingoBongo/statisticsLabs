plain = "some text"
key = "short key bla bla bla"


def xor(text, key):
    a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(text, key)]
    return "".join(a_list)


a = xor(plain, key)
print('encoded: %s' % a)
print('decoded: %s' % xor(a, key))
