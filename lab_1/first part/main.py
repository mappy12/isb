from  vigenere import *

def read_text(filename: str) -> str:

    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()

def main():

    key = "собака"
    input_text = read_text("user_texts/cipher_text.txt")

    print(vigenere_cipher(input_text, key))


if __name__ == "__main__":
     main()