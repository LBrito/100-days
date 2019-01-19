def abbreviate(phrase):
    acronym = ""
    for words in phrase.replace("_", "").replace("-", " ").split():
        acronym += words[0].upper()
    return acronym
