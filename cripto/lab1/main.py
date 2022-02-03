import base64


def sstr(s):
    new = ""
    for x in s:
        new += x
    return new

class RC4_Basic:
    def __init__(self):
        self.key = None

    def set_key(self, nkey):
        self.key = nkey




    def encrypt(self, plain_text):
        S = list(range(256))
        j = 0
        out = []
        key = self.key
        data = plain_text

        # KSA Phases
        for i in range(256):
            j = (j + S[i] + ord(key[i % len(key)])) % 256
            S[i], S[j] = S[j], S[i]

        # PRGA Phase
        i = j = 0
        for char in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

        return sstr(out)

    def decrypt(self, ciphered_text):
        S = list(range(256))
        j = 0
        out = []
        key = self.key
        data = ciphered_text

        # KSA Phase
        for i in range(256):
            j = (j + S[i] + ord(key[i % len(key)])) % 256
            S[i], S[j] = S[j], S[i]

        # PRGA Phase
        i = j = 0
        for char in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

        return sstr(out)

RC4_alg = RC4_Basic()
RC4_alg.set_key('s3cret')
plain_text = 'some text'
print(f'plain text: %s' % plain_text)
ciphered_text = RC4_alg.encrypt(plain_text)
print(f'ciphered text: %s' % ciphered_text)
decyphered_text = RC4_alg.decrypt(ciphered_text)
print(f'decrypted text: %s' % decyphered_text)