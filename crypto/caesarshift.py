# Author List:
# - pbwaffles
# - jnwarp

import argparse

def decrypt(encrypted, shift = 3):
    """
    encryped is a string that contains the encrypted text in all uppercase characters.
    converts characters to the ascii decimal notation, shifts them by a given amount,
    and then converts back to the symbol.
    """
    decrypted = ''

    for letter in encrypted:
        # don't shift spaces
        if letter == " ":
            decrypted += " "
            continue

        newLetter = chr(ord(letter)+shift)
        # don't allow letter to go past 'Z', loops back to 'A'
        if ord(newLetter) > 90: # ord('Z') = 90
            newLetter = chr(ord(letter)+i-26) # loops back to beginning of alphabet
        decrypted += newLetter # builds the decrypted text string
    return decrypted


########################################
# you can ignore everything below here #
###################################### #

# use argparse to get inputs
parser = argparse.ArgumentParser(description='Decrypt an input caesar cipher.')
parser.add_argument('text', help='input text to decrypt')
parser.add_argument('shift', type=int, default=None, nargs='?',
                    help='how many characters to shift by (shows all by default)')

# do stuff with the inputs
args = parser.parse_args()
if args.shift == None:
    # list all cipher shifts by default
    for i in range(1, 26):
        print("Shift %2i: %s" % (i, decrypt(args.text, i)))
else:
    # only output decrypted text
    print(decrypt(args.text, args.shift))
