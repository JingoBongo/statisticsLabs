from Crypto.Cipher import ARC4 as rc
from arc4 import ARC4


arc4 = ARC4('s3cret')
cipher1 = arc4.encrypt('some text')

print(cipher1)


key = b's3cret'
cipher = rc.new(key)
msg = cipher.encrypt(b'some text')

print(msg)