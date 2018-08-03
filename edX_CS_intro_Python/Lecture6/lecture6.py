animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for i in aDict.values():
        result += len(i)
    return result


print(how_many(animals))


big = {'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = 0
    most = 0
    for i in aDict.keys():
        most = len(aDict[i])
        if most > result:
            result = most
            key = i
    return key

print(biggest(big))