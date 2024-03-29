def find_factors(num):
    results = []
    for i in range(1, num + 1):
        if num % i == 0:
            results.append(i)
    return results
        
        
        

    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
