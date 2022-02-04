import base64

# according to paper  weak keys are the ones with length = power of 2. make key change that is not visible for end user
# https://wiki-files.aircrack-ng.org/doc/technique_papers/rc4_ksaproc.pdf
# "these weak keys have length which is divisible by some non-trivial power of two"

# also the method has a weakness while the key is constant. I want to add some data to the array with cur_date of ciphering
# and then change the key accordingly, before changing key length. ""according to the same paper
# here exactly I need that with same 'key' we were getting different results based on time

# maybe due to entire algorithm being based on xor operations I will keep the spirit and hide my metadata in xors as well

# is there a chance to implement one way function on top of that all?

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

# with open("ciphered.txt", "w", encoding="utf-8") as f:
#     f.write(ciphered_text)
#     f.close()

# print(f'ciphered text: %s' % ciphered_text)
print(bytes(ciphered_text, 'utf-8'))

decyphered_text = RC4_alg.decrypt(ciphered_text)
print(f'decrypted text: %s' % decyphered_text)