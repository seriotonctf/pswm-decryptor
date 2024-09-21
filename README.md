# pswm-decryptor
A tool to bruteforce the pswm master password and decrypt the password vault

# Usage
```bash
python3 pswm-decrypt.py -f <path to the pswm encrypted file> -w <path to the wordlist file>
```
# Example
```bash
python3 pswm-decrypt.py -f ~/.local/share/pswm/pswm -w /usr/share/wordlists/rockyou.txt
```
