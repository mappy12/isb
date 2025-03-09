from idlelib.iomenu import encoding

from  vigenere import *

def read_text(filename: str) -> str:

    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()\

def write_encrypted_text(filename: str, text: str) -> None:

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():

    key = "собака"
    input_text = read_text("user_texts/input_text.txt")
    encrypted_text = vigenere_cipher(input_text, key)
    output_text = "user_texts/output_text.txt"

    write_encrypted_text(output_text, encrypted_text)

if __name__ == "__main__":
     main()