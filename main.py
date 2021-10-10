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
# print(22 not in nums)
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
# r for reading, w for writing, a for appending
# fhand = open('lorem.txt', 'r')
# print(fhand)
# print(fhand.name)

# for word in fhand:
#     print(word)

# count = 0
# for word in fhand:
#     if word == 'iste':
#         print('found it')
#         count += 1
# print(count)

# turns out it's necessary to close the file when you are done with it
# fhand.close()

# This is apparently called a context manager
# with open('lorem.txt', 'r') as fhand:
#     pass

# print(fhand.closed) # returns true 

# ===>>>> there are lots of context manager methods, did a quick search chose something to read later
# with open('lorem.txt', 'r') as fhand:
#     fhand_contents = fhand.read()
#     # print(fhand_contents)
#     # had to split otherwise loops through the letters, it's really fun :D
#     spl = fhand_contents.split(" ")
#     for x in spl:
#         print(x)

# with open('lorem.txt', 'r') as fhand:
    # getting both the first and the second line 
    # fhand_contents = fhand.readline()
    # print(fhand_contents)
    # fhand_contents = fhand.readline()
    # print(fhand_contents)

    # Or I could just loop through like this
    # for line in fhand:
    #     print(line, end=' ') # Keeping end here as an example



# with open('lorem.txt', 'r') as fhand:
#     # with the first read method we read until 100 charachters
#     fhand_contents = fhand.read(100)
#     print("until 100 ==> ",fhand_contents, end=' ')
#     # The second one start from where it was left off 
#     fhand_contents = fhand.read(100)
#     print("more than 100 ==>", fhand_contents, end=' ')

# the input thing is very useful in python, an example:
# fname = input('Enter the file name: ')
# fhand = open(fname)


# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print("File can't be opened: ", fname)
#     # without the quit it weould keep going and mess up the rest
#     # of the code because fhand would be undefined
#     quit()
#     # It will terminate the python program without a traeback silently

# count = 0
# for line in fhand:
#     if line.startswith('Subject:') :
#         count += 1
# print("There were ", count, "subject lines in", fname)


# Strings are Immutable, just a reminder, the methods usually 
# make a copy and alter it 

# ==> The order in which the following is written was interesting 
# that's why I'm adding it
# Pretty obvious what it does, after the input is given checks if it's 
# equal to done before going thorugh the rest of the code
# total = 0 
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Average:', average)



# ==> Splitting stuff
# like in javascript mostly
# test_string = 'gonna be doing some tests on this string'
# etc = test_string.split()
# print(etc)
# test_string = 'first;second;third'
# thing = test_string.split()
# print(thing)
# print(len(thing))
# thing = test_string.split(';')
# print(thing, len(thing))

# ==> dict stuff

# counts = dict()
# names = ['to', 'ta', 'ke', 'ka', 'te', 'ke', 'ta', 'ke']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print("counts ==> ",counts)

# The pattern of checking to see if a key is in a dictionary and
# assuming a default value if the key is not there is so common that 
# there apparently is a method called get() that does this for us

# ==> x = counts.get(name, 0)
# Using with the example above
# for name in names:
#     x = counts.get(name, 0)
#     print(name,':',x)

# ==> Using toget her for simplicity <==
# counts = dict()
# names = ['to', 'ta', 'ke', 'ka', 'te', 'ke', 'ta', 'ke']
# for name in names: 
#     # setting a default if there is no value
#     counts[name] = counts.get(name, 0) + 1 
# print(counts)

# when I wrote k,v instead of just v; k became the first and the v 
# became the second value as in [0] and [1] of the keys
# for k in counts:
#     print(k, counts[k])

# Another probably python only iteration, using with items() method 
# don't forget
# print(counts.items())
# for k,v in counts.items():
#     print(k, v)

# print(counts)

# ==> Using the new stuff on a File <===== Nice Stuff 
# file_name = input('Enter file: ')
# handle_file = open(file_name)

# counts = dict()
# for line in handle_file:
#     words = line.split()
#     for word in words:
#         # print("word ==> ", word)
#         # get the word from dictionary, if it's not there create one with the given default value
#         counts[word] = counts.get(word, 0) + 1

# big_count = None
# big_word = None
# print("Atfer the loop to populate", counts.items())
# for word, count in counts.items():
#     print("word ==> ", word, '-' ,"count ==> ", count)
#     if big_count is None or count > big_count:
#         big_word = word
#         big_count = count
#         print("big word =>>", big_word)
#         print("big count =>>", big_count)

# print(big_word, big_count)


# ==> Tuples are like lists but they are IMMUTABLE
# contents of a tuple can't be altered, kinda like a string
# z = ('kek', 'lol', 'jump')
# z[0] = 'hello' # this would throw an error
# This is the error ==> 'tuple object does not support item Assignment'

# n = (3, 2, 1)
# n.sort() # Also throws an error
# n.append(4) # Also throws an error
# n.reverse() # Also throws an error


# this is possible and the paranthesis can be omitted
# (x, y) = (4, 'fred') # ==> x, y = 4, 'fred' <== same as that one
# print(x)
# y = 6
# print(y)

# The items() method in dictionaries returns a list of tuples (key value pairs)

# Tuples are al so comparable
# If the first item is equal it goes to the next one (and so on), until it find an element that differ

# (0, 1, 2) < (3, 4, 5) # This is true
# (0, 1, 3) < (0, 1, 5) # also true
# ('kek', 'lol') > ('kek', 'bob') # also true
# etc.

# ==> Sorting Tuples <==

# dictionaries can be turned into tuples using items() method and those tuples can be sorted easily
# d = { 'a': 10, 'c': 1, 'b': 22 }
# d.items()
# print(d.items())
# sorted_d = sorted(d.items())
# # print(d.items(), sorted_d)

# tem_list = list()
# for k,v in sorted_d:
#     # print(k, v)
#     tem_list.append( (v,k) )

# print(tem_list, type(tem_list))

# # Now sorting, reserve=True means keys and values will change place 
# tem_list = sorted(tem_list, reverse=True)
# # Now sorted according to the new keys 
# print(tem_list)

# Now rewriting and sorting my word count with all this info
# file_name = input('Enter file: ')
# handle_file = open(file_name)

# counts = dict()

# for line in handle_file:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# lst = list()

# for key, value in counts.items():
#     # create the new tuples with these key value pairs, reversed here 
#     newtup = (value, key)
#     # append the tuples to the lists, example: (5, 'sit')
#     lst.append(newtup)

# # reversing again (it was reversed up there once) to get the word as key
# lst = sorted(lst, reverse=True)

# # don't need to get all 
# for val, key in lst[:10]:
#     print(key, val)


# Even Shorter Version
# c = {'a': 10, 'b':2, 'c':22}
# Flips keys and values and sorts them inside a list ( "[]" i meant square brackets ) and bascially returns the same result
# print( sorted( [ (v,k) for k,v in c.items() ] ))


# >>>>>>>Simple Note<<<<<<<<<<<<

# g = [('a', 2),('b',1)]
# print(sorted(g))
# # Simple reminder, when reverse true is added it sorts according to the values not keys, doesn't swap keys and values 
# print(sorted(g, reverse=True))

# >>>>>>>>>>Note Ends<<<<<<<


# ==> Regular expressions in python
# hand = open('lorem.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('enim') >= 0:
#         print(line)

# Gonna do the same using regular expressions
# import re 

# hand = open('lorem.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('enim', line):
#         print(line)

# I could add the stuff the I have been using in javascript too such as ^, $, ?, ., *, etc. An example for startswith:

# import re 

# hand = open('lorem.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^voluptatem', line):
#         print(line)

# Or ends with: 

# import re 

# hand = open('lorem.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('sit$', line):
#         print(line)

# ==> Findall 
import re 

str = 'An example string for regular 22 expressions an 333 example strin 12 g for regular 55 expressionsn example string for regular expressionsn example string for regular expressions'
x = re.findall('example', str)
n = re.findall('[0-9]+', str)
y = re.findall('[AEIOU]+', str)
e = re.findall('s\w+g', str)

print("x ==>",x, "--" ,"n ==> ", n, "--","y ==> ", y)
print(e)
        