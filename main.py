# print('atta boy!')

## a simple input example
# inp = input('Europe floor? ')
# usf = int(inp) + 1
# print('US floor', usf)


# print('hello')

# def lyrics_random():
#     print('some random song lyrics that I can\' t really remember now')
#     print('some random song lyrics that I can\' t really remember now')

# lyrics_random()

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

# smallest = None
# print('before')
# for num in nums:
#     if smallest is None:
#         smallest = num
#     elif num < smallest:
#         smallest = num
#     print(smallest, num)
# print('after, smallest ==>', smallest)


# ==> String Stuff
s = 'A Nice String Example'
# print(s[4:5])
# print(s[:])
# print(s[6:])
# print(s[6:10000000])
# print('nice' in s)
# print(' ' in s)
# print('true' in s)

# # creates a lower case copy so original is unchanged
# ls = s.lower()
# us = s.upper()
# print("original ==> ",s, "lowered ==> ",  ls, "uppercase ==> ", us)

# cs = s.center(200)
# print("takes up 200 spaces with the string example in the middle")
# print(cs)
# print(s)

# replaced = s.replace('A Nice', 'An Awesome')

# print(s, replaced)

# ==> There are multiple ways to get rid of whitespace in python
greeting = '  Hello Stranger  '

# print(greeting.lstrip())
# print(greeting.rstrip())
# print(greeting.strip())

# ==> Also startswith method exists, just a reminder
# print(s.startswith('A'))

# data_text = "From akbiyik.ilker7@gmail.com Fri Oct 8 13:41:22 2021"
# at_pos = data_text.find('@')
# print(at_pos)
# # This is how you get a value after another in python 
# sp_after_pos = data_text.find(' ', at_pos)
# print(sp_after_pos)
# # I don't wanna include the '@'
# host = data_text[at_pos+1 : sp_after_pos]
# print(host)

# ==> With \n you can start another line
# nl = "the first line\nsecond line"
# print(nl)


# ==> Reading a file
# fhand = open('C:/users/samsung/desktop/lorem.txt')
fhand = open('lorem.txt')
print(fhand)
# for word in fhand:
#     print(word)

count = 0
for word in fhand:
    if word == 'iste':
        print('found it')
        count += 1
print(count)