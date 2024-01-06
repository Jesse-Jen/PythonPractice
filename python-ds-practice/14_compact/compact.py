def compact(lst):
    results = []
    for elements in lst:
        if elements:
            results.append(elements)
    return results

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """