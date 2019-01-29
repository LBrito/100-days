import re


def abbreviate(phrase):
    return "".join(word[:1].upper() for word in re.split(r"[\W-]+", re.sub(r"[_']+", "", phrase)))
