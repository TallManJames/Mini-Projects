
'''
#1
#1 2
#1 2 3
for x in range(1,4):
    for y in range(1, x+1):
        print(y, end=' ')    #this end function tells code to put a space instead of a new line
    print()


#1 2 3
#4 5 6
for i in range(1,3):
    if i == 1:
        for j in range(i, i+3):
            print(j, end=' ')
    elif i == 2:
        for j in range(i+2, i+5):
            print(j, end=' ')
    print()

#better version of ↑
for i in range(1,7):
    print(i, end=' ')

    if i == 3:
        print()

#    *
#  * *
#* * *
for i in range(1,4):
    spaces = ' '*2*(4-i)    #needed the *2 so it would soace properky
    stars = '* '*i
    print(spaces+stars)


#multiplication table
n=4     # nxn table
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j, end=' ')
    print()


# This is to match pairs of numbers that add to the target
numbers = [2, 4, 3, 5, 7, -1, 0, 6]
target = 6
print()
for i in numbers:
    for j in numbers:
        if (i+j) == target:
            print(f"({i},{j})")

'''

