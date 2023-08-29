'''
The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.

'''
# Program to print the values except for the value 5
number = 0
for number in range(10):
    if number == 5:
        continue    # continue here
    print('Number is ' + str(number))
print('Out of loop')

# program to print odd numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)

#
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)