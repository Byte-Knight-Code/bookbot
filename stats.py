

def read_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):

    count = []
    word_count = 0

    count = text.split()
    word_count = len(count)

    return word_count

def sorting_characters(text):

    characters = {}

    for char in text.lower():
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1

    characters_list = [{"char": char, "num": count} for char, count in characters.items()]

    def get_num(entry):
        return entry["num"]

    characters_list.sort(key=get_num, reverse=True)

    final_list = []

    for char in characters_list:
        final_list.append(f"{char.get('char')}: {char.get('num')}")

    return final_list
