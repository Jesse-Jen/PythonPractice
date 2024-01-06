def frequency(lst, search_term):
    count = 0
    for num in lst:
        if num == search_term:
            count += 1
    return count

# using count method 
# def frequency(lst, search_term):
#     return lst.count(search_term)





    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """