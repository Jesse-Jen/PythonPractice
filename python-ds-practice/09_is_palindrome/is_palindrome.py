def is_palindrome(phrase):
    lower_case_no_space = phrase.lower().replace(' ','')
    backwards = lower_case_no_space[::-1]
    if backwards == lower_case_no_space:
        return True
    else:
        return False

    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
