'''
Here’s what’s falsy in Python:

False
None
Zero in any numeric type: 0 0.0
Empty sequences or collections:
'' (empty string)
[] (empty list)
() (empty tuple)
{} (empty dictionary)
range(0) (empty range)
'''

# print(7 == 7)
# prints: True
# 7 is equal to 7

# print(7 == "7")
# prints: False 
# 7 is an integer, and "7" is a string

# print(7 != 7)
# prints: False
# 7 is equal to 7

# print(7 != "7")
# prints: True 
# 7 is an integer, and "7" is a string; therefore, they cannot be equal

# print(8 > 8)
# prints: False 
# 8 is not greater than 8

# print(8 >= 8)
# prints: True 
# 8 is greater than or equal to 8 (equal)

# print(8 < 8)
# prints: False 
# 8 is not less than 8

# or
# returns the first truthy operand, or the last operand

# print(True or False)
# prints: True

# print(False or True)
# prints: True

# print(False or False)
# prints: False

# print('hello' or 0)
# prints: 'hello'

# print(0 or 'hello')
# prints: 'hello'

# print('hello' or 'tacos')
# prints: 'hello'

# and
# returns the first falsy operand, or the last operand

# print(True and False)
# prints: False

# print(False and True)
# prints: False

# print('hello' and 0)
# prints: 0

# print(0 and 'hello')
# prints: 0

# print('hello' and 'tacos')
# prints: 'tacos'

# or
# returns the first truthy operand, or the last operand

# print(True or True or True)
# prints: True

# print(True or True or False)
# prints: True

# and
# returns the first falsy operand, or the last operand

# print(True and True and True)
# prints: True

# print(True and True and False)
# prints: False

# print(False or True and True)
# prints: True

# print(not False)
# prints: True

# print(not 'hello')
# prints: False


floor = "sticky"
walls = "clean"

# notice the colon ':' after the conditional expression
# it indicates the start of the if block
# if floor == "sticky":
    # print("Clean the floor! It's sticky!")
    # this is where you would add more lines of code related to the condition
    # each line must be indented to be part of the 'if' block

# unindented code indicates that we have returned to normal code execution
# print("This will always print, it's not inside of an if block!")

# parentheses are not required around the conditional expression
# if walls == "sticky":
    # print("Clean the walls! They're sticky!")

# val = 3

# # if path
# if val == 1:
#     print('val is one')
# # else path
# else:
#     print('val is not one')
#     # prints: val is not one
#     # since val is not 1, the else path is taken

# val = 3

# if val == 1:
#     print('val is one')
# elif val == 2:
#     print('val is two')
# elif val == 3:
#     print('val is three')
#     # prints: val is three
#     # since val is 3, this elif path is taken
# else:
#     print('not one, two, or three')
# if val == 3:
#     print('This also prints, because its another block')

# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')

# if color == 'green':
#     print('Go!')
# if color == 'yellow':
#     print('Slow Down!')
# if color == 'red':
#     print('Stop!')
# else:
#     print('Bogus!')

# names = ["Emily", "Jack", "Sophia", "Ethan"]

# for name in names:
#     print(name)

# num = 1

# while num <= 10:
#     print(num)
#     # prints the numbers 1 through 10
#     num += 1
# while loops keep looping until all possible are ran. Can be infinite

# things = ["computer", "g-g-ghost", "chair", "spider", "desk"]

# for thing in things:
#     if thing == "g-g-ghost":
#         print("Oh, that's just my ghost friend, carry on.")
#         continue
#     elif thing == "spider":
#         print("Nope. Burn it down, no more.")
#         break
#     print(f"There is a {thing} in the room.")
'''
In for and while loops, the continue statement will end the current iteration  
of a loop and continue to the next iteration as long as the condition of the loop
is still truthy or there are still items to iterate through.
'''

# while True:
#     color = input('Enter "green", "yellow", "red": ').lower()
#     print(f'The user entered {color}')

#     if color == 'green':
#         print('Go!')
#     elif color == 'yellow':
#         print('Slow Down!')
#     elif color == 'red':
#         print('Stop!')
#     elif color == 'quit':
#         print('Time to quit')
#         break
#     else:
#         print('Bogus!')
        

# // With a ternary expression
# let timeOfDay = 9
# let morning = timeOfDay < 12 ? true : false;

# // Without a ternary expression
# let timeOfDay = 9
# let morning;
# if (timeOfDay < 12) {
#   morning = true;
# } else {
#   morning = false;
# }

# time_of_day = 9
# morning = True if time_of_day < 12 else False
# print(morning)
# # prints: True

# for num in range(5):
#     print(num)
#     # prints the integers: 0, 1, 2, 3, 4

# for even in range(4, 12, 2):
#     print(even)
#     # prints the integers: 4, 6, 8, 10

# nums = list(range(10))
# print(nums)
# # prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for num in range(5, 0, -1):
#     print(num)
#     # prints the integers: 5, 4, 3, 2, 1
