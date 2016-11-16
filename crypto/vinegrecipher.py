# Vigenere Cipher Solver
# Decryption method written by inventwithpython
# Everything else written by pbwaffles

import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def attempt_keys(message, bestKeys, keyWordList):
    """
    message is a string of the encrypted text. bestKeys is a dictionary of the current best keys
    found. bestKeys is a dictionary of the current best keys for the encrypted text. keyWordList
    is a string to the location of the dictionary to use for possible keys.
    This will go through a dictionary and attempt to decrypt the encrypted string using keys from
    the dictionary.
    Returns the best keys found which produced the most amount of english words.
    """
    with open(keyWordList, 'r') as f: #wordlist to try (dictionary of keys)
        count = 0
        keyFound = False
        newBestKeys = bestKeys # creates new dict to edit with adding/removing keys
        for myKey in f:
            count += 1
            if (count % 1000) == 0:
                print 'Attempt %i' % count # prints every time 1000 keys are attempted
            myKey = myKey.strip('\n') # removes those damned newline characters
            translated = translateMessage(myKey, message)
            if translated: # checks to make sure there is a decrypted message in case of an error
                if translated[0] == 'C': # use this to specify location of a known plaintext 
                                         # character if known, case sensitive
                    score = is_english(translated)
                    if len(bestKeys) <= 10: # if less than 10 keys, automatically add the key and score
                        newBestKeys[myKey] = score
                    else:
                        for key in bestKeys: # loops through all keys and keeps the 10 highest
                            if score > bestKeys[key]:
                                del newBestKeys[key]
                                newBestKeys[myKey] = score
                                break
                    for key in newBestKeys: # checks to see if the right key has been found based on
                                            # if the score is high enough
                        if int(newBestKeys[key]) > 70: #70 is an arbitrary score number to guess at 
                                                       # (don't know a good way to determine this)
                            keyFound = True
                    if keyFound:
                        return newBestKeys
    return newBestKeys


def is_english(decryptText):
    """
    decryptText is a string of the plaintext produced using a given key.
    This attempts to determine how much english is in the plaintext and returns this as a score.
    For every word found in the decryptText a point is added to the overall score.
    Higher scores mean there are more english words present and is more likely to be correct.
    Returns a decimal number denoting score of decryptText
    """
    #this will check for words that are x letters or shorter
    f = open('dictionary.txt', 'r')
    englishWords = []
    for line in f:
        englishWords.append(line.strip('\n'))
    score = 0
    currentPos = 0
    for word in englishWords:
        if word in decryptText:
            score += 1
    f.close()
    return score

def main(myMessage='', keyWordList='/root/Desktop/rockyou.txt'):
    """
    myMessage is the encrypted text that will be decrypted. keyWordList is a string
    of the location for the dictionary to use for keys.
    Attempts to decrypt encryted text.
    Prints the length of time taken.
    Prints the 10 best keys and the respective decrypted text
    """
    bestKeys = {}
    startTime = time.time()
    bestKeys = attempt_keys(myMessage, bestKeys, keyWordList)

    print 'the best keys are...\n'
    for key in bestKeys:
        print 'Key: %s' % key
        print 'Message: %s' % decryptMessage(key, myMessage)
    print '\n'
    endTime = time.time()
    hour = (endTime-startTime)/3600 #3600 seconds in an hour
    minute = ((endTime-startTime)/60) % 60 #60 seconds in a minute
    second = (endTime-startTime) % 60
    print 'Time elapsed: %i hour(s) %i minute(s) %i second(s)' % (hour, minute, second)


def translateMessage(key, message):
    """
    key is a string representing the key being used to decrypt encrypted text.
    message is a string of the encrypted text to be decrypted.
    Returns the decrypted plaintext
    """
    try:
        translated = [] # stores the encrypted/decrypted message string

        keyIndex = 0
        key = key.upper()

        for symbol in message: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

                num %= len(LETTERS) # handle the potential wrap-around

                # add the encrypted/decrypted symbol to the end of translated.
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1 # move to the next letter in the key
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # The symbol was not in LETTERS, so add it to translated as is.
                translated.append(symbol)

        return ''.join(translated)
    except IndexError:
        print 'There was an error'
        return ''


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    myMessage = "YHTEQAPSSQWLTLSILYPENZIZSJLVPVIPVWLKDLZRCWZXGEZEWCDHDBRCSIEXHLWKRKTOYIUPVFCLBRDIWULGSPOIYKLHZMMYBLLVPVQGXAYEDXILWGWDVRPMPOWNKDAIHSQSLLEESAMSQAIEMPALPEJKAXIPOEHEPLZRTWYTZJPOMPSNSD"
    main(myMessage)
