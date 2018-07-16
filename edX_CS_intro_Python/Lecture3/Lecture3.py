# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l

lo = 0
hi = 100
ans = (hi - lo)/2
putin = 'a'
print('Please think of a number between 0 and 100!')
guess = 42

# while int(ans) != guess:
while putin != 'c':
    
    print('Is your secret number' , round(ans), '?')

    print('Enter ''h'' to indicate the guess is too high.', end=' ')
    print('Enter ''l'' to indicate the guess is too low.', end=' ')
    print('Enter ''c'' to indicate I guessed correctly.', end=' ')
    putin = input()

    if putin == 'l':
        lo = ans
    elif putin == 'h':
        hi = ans
    elif putin == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')        

    ans = (hi + lo)/2

print('Game over. Your secret number was:' , round(ans))


    
