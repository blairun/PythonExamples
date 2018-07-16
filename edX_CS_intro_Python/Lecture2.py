str1='hello'
str2=','
str3='world'
str4=str1 + str3

str4[0:10:2]

str4[::-2]

print(str1[-1])

print(len(str1))
# str1[len(str1)]

print('HELLO'==str1)


##########

x=5
if x != 5:
    print('I am here')
else:
    print('nope')



#########
varA = 'A'
varB = 1
knownString = 'A'

if type(varA) == type(knownString)  or type(varB) == type(knownString):
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')


# ############

n=0
while n < 10:
    n += 2
    print(n)
print('Goodbye!')


###############

print('Hello!')
n=10
while n > 0:
    print(n)
    n -= 2

##########

end = 6
n = end
while n > 0:
    n -= 1
    end += n
print(end)


# ############

n=0
for n in range(2,11,2):
    print(n)
print('Goodbye!')


###############

print('Hello!')
for n in range(10,0,-2):
    print(n)
    
##########

end = 6
for n in range(end-1,0,-1):
    end += n
print(end)


num = 10
for num in range(5):
    print(num)
print(num)



#############
s = 'azcbobobegghakl'
v = 0
for n in range(len(s)):
    if s[n] == 'a' or s[n] == 'e' or s[n] == 'i' or s[n] == 'o' or s[n] == 'u':
            v += 1
print('Number of vowels: ' , v)
            


#############
#s = 'azcbobobegghakl'
#s = 'bobobobobobobobobobobobobobob' #14
s = 'bmhobobtoboobobbob' #3
#s = 'bobbxbobobbobbnjobobloboboobobooboojebooobobobbob' #10
v = 0
for n in range(len(s)-2):
#    print(s[n:n+3])
#    print(s[n])
    if s[n:n+3] == 'bob':
            v += 1
print('Number of times bob occurs is: ' , v)


##############

s = 'azcbobobegghakl'
s = 'cbcczzb'
abc = 'abcdefghijklmnopqrstuvwxyz'
pos = 0
strLen = 0
#matchLength = 0
matchString = ''
longestString = ''
stringLenth = 0

# check first letter of s against each letter in abc 
# record postion of match in abc
# move to next letter in s
# check agains abc[postion:]
# if there is a match, then add to matchString

for n in range(len(s)):
    
    # reset position if string hasn't grown
    if strLen < n:
        pos = 0
        matchString = ''

    for i in range(len(abc[pos:])):
        if s[n] == abc[pos+i:pos+i+1]:
            pos = pos + i
            matchString = matchString + s[n]
            
            if len(matchString) > len(longestString):
                longestString = matchString
                strLen += 1

print('Longest substring in alphabetical order is: ' , longestString)



































