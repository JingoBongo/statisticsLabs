import time


def stage1_encrypt(plain_text, key):
    S = list(range(256))
    j = 0
    out = []
    data = str(plain_text)

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

def sstr(s):
    new = ""
    for x in s:
        new += x
    return new


ti = time.time()
print(len(str(ti)))
print(len(stage1_encrypt(ti,'32345234523454')))

# from __future__ import division
# import math
# from decimal import Decimal as D
# from decimal import getcontext
# import multiprocessing as mp
#
# prec_count = 100
# getcontext().prec = prec_count
# MAX = 10000
# pi = D(0)
#
#
#
# print('PI >>>>>>>>>>' , pi)
#
# def calc_pi(number_to_find):
#     global pi
#     str_num = str(number_to_find)
#     ind = 0
#     for k in range(MAX):
#         pi += D(math.pow(16, -k)) * (D(4 / (8 * k + 1)) - D(2 / (8 * k + 4)) - D(1 / (8 * k + 5)) - D(1 / (8 * k + 6)))
#         if str_num in str(pi):
#             print(pi)
#             print('number found on index '+str(ind))
#             break;
#         ind += 1
#
#
# # pool = mp.Pool(mp.cpu_count())
# # results = pool.apply(calc_pi())
#
# calc_pi(285)