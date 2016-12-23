Cryptography Scripts
====================

`caesershift.py`
------------------------------------------------

Decrypt an input caesar cipher by shifting it a number of characters.

Example:
```bash
python3 ./caesarshift.py "WKH TXLFN EURZQ IRA"
...
Shift 23: THE QUICK BROWN FOX
...
```

```bash
usage: caesarshift.py [-h] text [shift]

Decrypt an input caesar cipher.

positional arguments:
  text        input text to decrypt
  shift       how many characters to shift by (shows all by default)

optional arguments:
  -h, --help  show this help message and exit
```
