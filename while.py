'''
while loop can execute a set of statements as long as given condition is true.
'''

#Program 1
i = 1
while i < 10:
  print(i)
  i += 1


#Program 2 to calculate the sum of numbers, until the user enters zero
total = 0
number = int(input('Enter a number: '))
# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    # take integer input again
    number = int(input('Enter a number: '))
print('total =', total)