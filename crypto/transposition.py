# Transposition Cipher Decryption
# Created by inventwithpython
# Adapted by pbwaffles
import math

def main(myMessage):
    """
    myMessage is the encrypted string that will be attempted to be decrypted.
    calls decryptMessage x amount of times in order to brute force the decryption.
    Returns None, prints plaintext as output.
    """

    for myKey in range(1,10): #number of keys to brute force
        plaintext = decryptMessage(myKey, myMessage)
        print('using key: %i' % myKey)
        print(plaintext)


def decryptMessage(key, message):
    """
    key is a decimal number to try as the key. message is a string of the encrypted text.
    key represents the number of columns to try. For example, a key of 3 with encrypted string
    abcdefg will be written as...
    abc
    def
    g
    which will result in a decrpyted string of adgbecf.
    The decrypted string is returned.
    """

    numOfColumns = math.ceil(float(len(message)) / float(key))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * int(numOfColumns)
    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column
         # If there are no more columns OR we're at a shaded box, go back to
         # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
        message = 'Cenoonommstmme oo snnio. s s c' # example of encrypted string "Common sense is
                                                   # not so common."
        main(message)
