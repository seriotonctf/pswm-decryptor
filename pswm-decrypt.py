import cryptocode
import argparse
from prettytable import PrettyTable

class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=50)

def bf(encrypted_text, wordlist):
    with open(wordlist, "r", encoding="utf-8") as f:
        for password in f:
            decrypted_text = cryptocode.decrypt(encrypted_text, password.strip())
            if decrypted_text:
                print("[+] Master Password: %s" % password.strip())
                print_decrypted_text(decrypted_text)
                return
    print("[-] Password Not Found!")

def print_decrypted_text(decrypted_text):
    table = PrettyTable()
    table.field_names = ["Alias", "Username", "Password"]
    for line in decrypted_text.splitlines():
        alias, username, password = line.split("\t")
        table.add_row([alias.strip(), username.strip(), password.strip()])
    table.align = "l"
    print("[+] Decrypted Data:")
    print(table)

def main():
    parser = argparse.ArgumentParser(description="pswm master password cracker", formatter_class=CustomHelpFormatter)
    parser.add_argument("-f", "--file", required=True, help="Path to the encrypted file")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        encrypted_text = f.read().strip()
    
    bf(encrypted_text, args.wordlist)

if __name__ == "__main__":
    main()