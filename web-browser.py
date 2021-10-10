# import socket

# # This was the given example seemed interesting so I copied here

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if(len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# ==>> Using urllib
# There is a library that does all the socket work for us and makes web pages look like a file
# Retrieving and reading network resources
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# # Printing all the lines
# # for line in fhand:
# #     print("printing ==>",line.decode().strip())


# # Counting the words 
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# ==> Reading Web Pages with urllib
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())