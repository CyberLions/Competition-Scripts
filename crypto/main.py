#! /usr/bin/env python

import argparse
import sys
import ceasershift
import transpositionDecrypt
import vinegrecipher



if __name__ == '__main__':

    #do stuff here
    parser = argparse.ArgumentParser(description='Decrypt encrypted text. Supports ceasershift, substitution, transposition, and vigenere.')
    parser.add_argument('-c', '--cipher', help='Choose which cipher to use', choices=['ceaser', 'substitution', 'transposition', 'vigenere'])
    parser.add_argument('-e', '--encrypted', help='Encrypted text to decrypt')
    args = parser.parse_args()
    args = vars(args)
    if None in args.values():
        print 'You must supply the cipher to use and the encrypted text to decrypt'
        parser.print_help()
        sys.exit(2)
    encryptedText = args['encrypted'].upper()
    cipher = args['cipher']
    if cipher == 'ceaser':
        ceasershift.decrypt(encryptedText)
    elif cipher == 'substituition':
        print 'This doesnt exist yet'
    elif cipher == 'transposition':
        transpositionDecrypt.main(encryptedText)
    elif cipher == 'vigenere':
        vinegrecipher.main(encryptedText)
