def multiple_letter_count(phrase):
    letter_count = {}
    phrase = phrase.lower()
    for char in phrase:
        #checking if letter
        if char.isalpha():
            letter_count[char] = letter_count.get(char,0) + 1
    return letter_count


    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """