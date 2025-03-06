alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def get_encrypted_symb(old_sym: str, key_sym: str) -> str:

    current_idx = alphabet.index(old_sym.lower())
    key_sym_idx = alphabet.index(key_sym.lower())

    if current_idx + key_sym_idx > len(alphabet):

        encrypt_idx =  current_idx + key_sym_idx - len(alphabet)

    else:

        encrypt_idx = current_idx + key_sym_idx

    return alphabet[encrypt_idx]

