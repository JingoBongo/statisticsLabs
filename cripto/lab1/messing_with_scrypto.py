import scrypt

data = scrypt.encrypt('a secret message', 'password')



print(scrypt.decrypt(data, 'password'))