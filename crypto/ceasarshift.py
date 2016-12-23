# Author - pbwaffles


def decrypt(encrypted):
    """
    encryped is a string that contains the encrypted text in all uppercase characters.
    converts characters to the ascii decimal notation, shifts them by a given amount,
    and then converts back to the symbol.
    prints out decrpyted string using every shift (1-25).
    """
    for i in range(1,26):
        decrypted = ''
        for letter in encrypted:
            newLetter = chr(ord(letter)+i)
            #don't allow letter to go past 'Z', loops back to 'A'
            if ord(newLetter) > 90: # ord('Z') = 90
                newLetter = chr(ord(letter)+i-26) #loops back to beginning of alphabet
            decrypted += newLetter # builds the decrypted text string
        print 'Shift %i: %s' % (i, decrypted)
