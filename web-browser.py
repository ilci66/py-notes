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
# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# Using BeautifulSoup

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# # Enter this ==> http://www.dr-chuck.com/page1.htm
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))


# ==> Processing XML

# import xml.etree.ElementTree as ET
# data = '''<person>
# <name>Chuck</name>
# <phone type="intl">
# </phone>
# <email hide="yes"/>
# </person> '''


# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:' ,tree.find('email').get('hide'))


# ==> Processing JSON
# import json
# data = '''{
#     "name": "Chuck",
#     "phone": {
#         "type": "intl",
#         "number": "+1 734 303 4456"
#     },
#     "email": {
#         "hide": "yes"
#     }
# }'''

# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])

# Interacting with APIs
# This one will ask for an api key but wrote it here for demostration
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    # Enter location: Ann Arbor, MI
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js: None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)