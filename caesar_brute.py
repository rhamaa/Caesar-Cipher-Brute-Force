#based on : http://programeveryday.com/post/implementing-a-basic-caesar-cipher-in-python/

from sys import argv
print "\n"
print "-" * 34
print "- Caesar  Cipher Brute Force" + " " * 5  + "-"
print "- rhama.my.id" + " " * 20  + "-"
print "-" * 34
print "\n"

if len(argv) == 1:
    print "Usage : %s <caesar>" % (__file__)
    exit(1)

key = 'abcdefghijklmnopqrstuvwxyz'
KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def encrypt(n, plaintext):
#     """Encrypt the string and return the ciphertext"""
#     for l in ciphertext:
#         try:
#             if l.isupper():
#                 index = KEY.index(l)
#                 i =  (index + n) % 26
#                 result += KEY[i]
#             else:
#                 index = key.index(l)
#                 i =  (index + n) % 26
#                 result += key[i]            
            
#         except ValueError:
#             result += l

#     return result

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            if l.isupper():
                index = KEY.index(l)
                i =  (index - n) % 26
                result += KEY[i]
            else:
                index = key.index(l)
                i =  (index - n) % 26
                result += key[i]            
            
        except ValueError:
            result += l

    return result


for n in range(0,27):
    dec = decrypt(n, argv[1])
    print "%d . %s" % (n,dec)
