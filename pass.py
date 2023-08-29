'''
Pass keyword is used as a placeholder.When the user does not know what code to write, So user simply places a pass at that line. 
Sometimes, the pass is used when the user doesn’t want any code to execute.
So users can simply place a pass where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. 
So using a pass statement user avoids this error.
'''

# example 1
for x in [0, 1, 2]:
  pass

# example 2
a = 10
b = 20
if(a>b):
    pass
else:
    print("b is lesser than a")

# example 3
word = "Stechiess"
for value in word:
    if value == 'e':
        pass
    else:
        print("Value: ",value)
