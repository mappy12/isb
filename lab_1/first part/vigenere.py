from Tools.scripts.generate_re_casefix import alpha

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def repeat_key(key: str, length: int) -> str:

    repeated_key = ""

    while len(repeated_key) < length:

        repeated_key += key

    return repeated_key


def get_encrypted_symb(old_sym: str, key_sym: str) -> str:
    if old_sym.isalpha():
        current_idx = alphabet.index(old_sym.lower())
        key_idx = alphabet.index(key_sym.lower())

        if current_idx + key_idx >= len(alphabet):

            encrypt_idx =  current_idx + key_idx - len(alphabet)

        else:

            encrypt_idx = current_idx + key_idx

        if old_sym == old_sym.upper():

            return alphabet[encrypt_idx].upper()

        return alphabet[encrypt_idx]

    else:

        return old_sym


def get_decrypted_symb(encrypted_sym: str, key_sym: str):

    if encrypted_sym.isalpha():

        encrypted_idx = alphabet.index(encrypted_sym.lower())
        key_idx = alphabet.index(key_sym.lower())

        if encrypted_idx - key_idx < 0:

            decrypted_idx = encrypted_idx - key_idx + len(alphabet)

        else:

            decrypted_idx = encrypted_idx - key_idx

        if encrypted_sym == encrypted_sym.upper():

            return alphabet[decrypted_idx].upper()

        return alphabet[decrypted_idx]

    else:

        return encrypted_sym


def vigenere_cipher_encrypt(input_text: str, key: str) -> str:

    encrypted_text = ""

    repeated_key = repeat_key(key, len(input_text))

    for i in range(len(input_text)):

        text_sym = input_text[i]
        key_sym = repeated_key[i]

        encrypted_text += get_encrypted_symb(text_sym, key_sym)

    return encrypted_text

def vigenere_cipher_decrypt(encrypted_text: str, key: str) -> str:

    decrypted_text = ""

    repeated_key = repeat_key(key, len(encrypted_text))

    for i in range(len(encrypted_text)):

        encrypted_sym = encrypted_text[i]
        key_sym = repeated_key[i]

        decrypted_text += get_decrypted_symb(encrypted_sym, key_sym)

    return decrypted_text