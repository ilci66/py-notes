# print('atta boy!')

## a simple input example
# inp = input('Europe floor? ')
# usf = int(inp) + 1
# print('US floor', usf)


# print('hello')

# def lyrics_random():
#     print('some random song lyrics that I can\' t really remember now')
#     print('some random song lyrics that I can\' t really remember now')

# print('hi!')

# lyrics_random()


# prints ran before the lyrics_random function, like in javascript

# def greet():
#     return "What up"

# print(greet(), "bro")



# this would ask me until I gave the input value 'done'
# break is to get out of the loop and continue is to stop what else you 
# were planning to do for that value and continue the loop with the next value

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done')

nums = [22, 3, 4, 12, 9, 43, 7, 8, 2, 1, 78, 98, 65, 45, 21, 23, 24, 5 ]

# print('before the loop')
# for x in nums:
#     # print(x)
#     if x < 10:
#         print(f'{x} be lowa')
# print('after the loop')

smallest = None
print('before')
for num in nums:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(smallest, num)
print('after, smallest ==>', smallest)