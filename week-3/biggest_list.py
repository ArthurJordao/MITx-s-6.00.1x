animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey']}

animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest = None
    biggest_value = 0
    for key, value in aDict.items():
        if biggest_value < len(value):
            biggest_value = len(value)
            biggest = key
    return biggest


print(biggest(animals))
