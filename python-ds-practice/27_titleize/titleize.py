def titleize(phrase):
    words = phrase.split
    for word in words:
       titles = word.capitalize()
    return ' '.join(titles)


    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
