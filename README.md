# pswm-decryptor
A tool to bruteforce the pswm master password and decrypt the password vault https://github.com/Julynx/pswm
## Prerequisites
```
pip3 install cryptocode prettytable
```
## Usage
```
python3 pswm-decrypt.py -f <path to the pswm encrypted file> -w <path to the wordlist file>
```
```
usage: pswm-decrypt.py [-h] -f FILE -w WORDLIST

pswm master password cracker

options:
  -h, --help                        show this help message and exit
  -f FILE, --file FILE              Path to the encrypted file
  -w WORDLIST, --wordlist WORDLIST  Path to the wordlist file
```
## Example
```
➜  python3 pswm-decrypt.py -f ~/.local/share/pswm/pswm -w /usr/share/wordlists/rockyou.txt

[+] Master Password: <REDACTED>
[+] Decrypted Data:
+------------+----------+----------------------+
| Alias      | Username | Password             |
+------------+----------+----------------------+
| pswm       | aleks    | <REDACTED>           |
| aleks@down | aleks    | <REDACTED>           |
+------------+----------+----------------------+
```
