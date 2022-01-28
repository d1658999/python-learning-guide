def search4vowel(phrase: str) -> set:
    return set('aeiou').intersection(set(phrase))

def search4letters(phrase: str, letters: str='aeiou') -> set:
    return  set(letters).intersection(set(phrase))