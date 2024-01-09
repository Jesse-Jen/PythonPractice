def same_frequency(num1, num2):


def num_counter(numbers):
    counts = {}
    for num in numbers:
       counts[num] = counts.get(num, 0) + 1
    return counts

"""Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """