from corr_coeff import corr_Coeff
from cipher_freq_analysis import get_the_value
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
cipher_path = os.path.join(THIS_FOLDER, 'ciphertext.txt')
cipher_text = ''
with open("ciphertext.txt") as f:
    cipher_text = f.read().upper()

english_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987 ,0.06327 ,0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
cipher_freq = ''
key_corr = {}
cipher_key = 0


def cracking_cesar(cipher_text_to_crack):

    message = cipher_text_to_crack.upper()

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):

        translated = ''

        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) # get the number of the symbol
                num = num - key


                if num < 0:
                    num = num + len(LETTERS)


                translated = translated + LETTERS[num]

            else:

                translated = translated + symbol

        cipher_freq = get_the_value(translated)

        key_corr[key] = abs(corr_Coeff(english_freq, cipher_freq))

        s = [(k, key_corr[k]) for k in sorted (key_corr, key=key_corr.get, reverse=True)]

    return next(iter(s))[0]


def encrypting( cipher_key_to_use ):
    key = int( cipher_key_to_use )

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ''
    for cipher_letter in cipher_text:
        if cipher_letter.lower() in alphabet:
            cipher += alphabet[(alphabet.index(cipher_letter.lower()) + key) % (len(alphabet))]

    # write_in_file = open("cipher_text.txt", "a")
    # write_in_file.write(cipher)

    return cipher.upper()


def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


if __name__ == '__main__':
    cipher_key = cracking_cesar(cipher_text)
    print("the key is : " + str(cipher_key))
    print("the plaint text is : " + decrypt(cipher_key, cipher_text))
    print("The cipher message is : " + encrypting(cipher_key))
