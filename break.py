'''
The break statement is used to terminate the loop when a certain condition is met.
'''
# Program to exit out of the loop when i values equals to 3
for i in range(5):
    if i == 3:
        break
    print(i)

# Program to print all the letters until the string letter  is "n" or "e" 
s = 'Pathaneni'
for letter in s:
    print(letter)
    # break the loop as soon it sees 'n' or "e" 
    if letter == 'n' or letter == 'e':
        break
print("Out of for loop")

