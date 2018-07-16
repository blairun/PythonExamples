# Branching; If statements

x = int (input('enter an integer: '))
if x%2 == 0:
    print('')
    print('even')
else:
    print('')
    print('odd')
print('Done with conditional 1')

if x%2 == 0:
    if x%3==0:
        print('divisible by 2 and 3') 
    else:
        print('divisible by 2 not 3')
elif x%3==0:
    print('divisible by 3 not 2')    
print('Done with conditional 2')