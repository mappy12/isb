import json


russian_freq = {
    'о': 0.1097, 'е': 0.0845, 'а': 0.0801, 'и': 0.0735, 'н': 0.0670,
    'т': 0.0626, 'с': 0.0547, 'р': 0.0473, 'в': 0.0454, 'л': 0.0440,
    'к': 0.0349, 'м': 0.0321, 'д': 0.0298, 'п': 0.0281, 'у': 0.0262,
    'я': 0.0201, 'ы': 0.0190, 'ь': 0.0174, 'г': 0.0170, 'з': 0.0165,
    'б': 0.0159, 'ч': 0.0144, 'й': 0.0121, 'х': 0.0097, 'ж': 0.0094,
    'ш': 0.0073, 'ю': 0.0064, 'ц': 0.0048, 'щ': 0.0036, 'э': 0.0032,
    'ф': 0.0026, 'ъ': 0.0004, 'ё': 0.0004
}


def save_freq_to_json(filename: str, d: dict) -> None:

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False)


def load_freq_from_json(filename: str) -> dict:

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def calculate_freq(text: str) -> dict:

    sym_counts = {}

    lower_text = text.lower()

    for sym in lower_text:

        if sym in sym_counts:

            sym_counts[sym] += 1

        else:

            sym_counts[sym] = 1

    total_symbs_count = sum(sym_counts.values())

    sym_freq = {}

    for char, count in sym_counts.items():

        freq = round(count / total_symbs_count, 4)

        sym_freq[char] = freq

    sorted_freq_list = sorted(sym_freq.items(), key=lambda item: item[1], reverse=True)

    sorted_freq = dict(sorted_freq_list)

    return sorted_freq

