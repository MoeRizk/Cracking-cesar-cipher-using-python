import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PLAIN_TEXT_FILE_PATH = os.path.join(THIS_FOLDER, 'plaint_text.txt')
PLAINT_TEXT = open('plaint_text.txt','r')
key = int(input("Enter your shifting key:"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = ''
the_outcome = ''
with PLAINT_TEXT as f:
    cipher = f.read().upper()

for cipher_letter in cipher:
    if cipher_letter.lower () in alphabet:
        the_outcome += alphabet[ (alphabet.index ( cipher_letter.lower () ) + key) % (len ( alphabet )) ]


print(the_outcome.upper())
