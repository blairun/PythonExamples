
# iterate
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result  = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

iterPower(3,3)


# recursion
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp ==0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)

recurPower(3,0)


# Greatest common denominator
# iterate
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        small = b
        smaller = b
        large = a
    else:
        small = a
        smaller = a
        large = b
     
    while smaller > 0:
        if large % smaller == 0 and small % smaller == 0:
            return smaller
        smaller -= 1
    return 1

gcdIter(9,12)


# Greatest common denominator
# recursion
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # gcd(a, b) is the same as gcd(b, a % b)
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

gcdRecur(3,6)



# Is character in string
# recursion
# doesn't fully work; see actual assignment for correct def
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here    
    if char == aStr[len(aStr)//2]:
        return True
    elif len(aStr) == 1:
        return False
    elif char > aStr[len(aStr)//2]:
        aStr = aStr[len(aStr)//2:len(aStr)]
        return isIn(char, aStr[len(aStr)//2:len(aStr)])
    else:
        aStr = aStr[0:len(aStr//2)]
        return isIn(char, aStr[0:len(aStr)//2])


isIn('a', 'abc')


################
# practice problem
import math
def polysum (n, s):
    area = 0.25 * n * s ** 2 / (math.tan(math.pi / n))
    perim = n * s
    ps = round(area + perim ** 2, 4)
    return ps

polysum(4, 5)

