Cryptography Scripts
====================

Any of the scripts in this directory can be called using `main.py`, but there may be additional options available for each script by calling it manually.

`main.py`
---------

Decrypt an input caesar cipher by shifting it a number of characters.

Example:
```bash
python3 ./main.py caesar "WKH TXLFN EURZQ IRA"
```

```bash
usage: main.py [-h] [--wordlist WORDLIST]
               {caesar,substitution,transposition,vigenere} text

Use a script in this folder to decrypt text using the default options.

positional arguments:
  {caesar,substitution,transposition,vigenere}
                        Choose which cipher to use
  text                  Encrypted text to decrypt

optional arguments:
  -h, --help            show this help message and exit
  --wordlist WORDLIST, -w WORDLIST
                        optional wordlist for some ciphers
```


`caeser.py`
-----------

Decrypt an input caesar cipher by shifting it a number of characters.

Example:
```bash
python3 ./caesar.py "WKH TXLFN EURZQ IRA"
...
Shift 23: THE QUICK BROWN FOX
...
```

```bash
usage: caesar.py [-h] text [shift]

Decrypt an input caesar cipher.

positional arguments:
  text        input text to decrypt
  shift       how many characters to shift by (shows all by default)

optional arguments:
  -h, --help  show this help message and exit
```
