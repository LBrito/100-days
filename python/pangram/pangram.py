def is_pangram(sentence):
    letters = set()
    for char in list(sentence):
        if 122 >= ord(char.lower()) >= 97:
            letters.add(char.lower())
    return len(letters) == 26
