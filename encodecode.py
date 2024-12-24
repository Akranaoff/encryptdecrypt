import random
import string

def randchar():
  res = ''.join((random.choice(string.ascii_letters))for i in range(3))
  return res


a = input("Enter your message : ")
l = a.split()
user = int(input("Would you like to encrypt(1) or decrypt(2) : "))

def encrypt():
  i = 0
  for i in l:
    if(len(i)<3):
      l[l.index(i)] = i[::-1]
    else:
      newword = l[l.index(i)][1:]+l[l.index(i)][0]
      res = randchar()+newword+randchar()
      l[l.index(i)] = res

def decrypt():
  i = 0
  for i in l:
    if(len(i)<3):
      l[l.index(i)] = i[::-1]
    else:
      newword2 = l[l.index(i)][3:-3]
      l[l.index(i)] = newword2[-1]+newword2[:-1]

if user == 1:
  encrypt()
  print("Encrypted message : ",' '.join(l))
else:
  decrypt()
  print("Decrypted message : ",' '.join(l))




print("Your message : ", a)
