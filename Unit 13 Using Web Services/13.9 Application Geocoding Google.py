import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
#api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
#Right now, we don’t have a real googlemaps API key. Therefore, api_key variable is False. 

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    #NOTE: This serviceurl has a static subset of Google Data. 
    #py4e.com/code3/geodata/README.txt
    #Basically, this serviceurl is acting like a Google API because it has a lot of data that a Google API would have but it doesn’t have everything. Just a subset of the data. 
    #This serviceurl is good because it doesn’t require an authentic google API, a google account, or access to Google. 
    #You can also run this unlimited times. 

else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#Since we don’t have a real API key, we are using a random api_key and a service_url that isn’t Google
#If we had a real API key, we could use google’s website. 
#Note: The api that's commented 'AIzaSy...' is not a real API. 
#Note: These serviceurl s do not link to any websites currently. 


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#Note on SSL 
#An SSL certificate is a digital certificate that authenticates a website's identity and enables an encrypted connection. 
#SSL stands for Secure Sockets Layer, a security protocol that creates an encrypted link between a web server and a web browser.
#Companies and organizations need to add SSL certificates to their websites to secure online transactions and keep customer information private and secure.
#In short: SSL keeps internet connections secure and prevents criminals from reading or modifying information transferred between two systems. 
#When you see a padlock icon next to the URL in the address bar, that means SSL protects the website you are visiting.
#Why ctx = ssl.create_default_context() ssl — TLS/SSL wrapper for socket objects — Python 3.12.0 documentation
 
 
#Basically, ssl_create_default_context() generates generic security settings for the website. 

while True:
#Note, this while loop will allow you to continue adding different locations without stopping the program. 
    address = input('Enter location: ')
    if len(address) < 1: break
#If you don’t add an address, you exit out of the while loop. 

    parms = dict()
#Forms an empty dictionary called parms. Parms stands for parameters. 

    parms['address'] = address
#Adds a key-value pair. The key is called ‘address’ and the value is the input from (‘Enter location:’) 

    if api_key is not False: parms['key'] = api_key
#Adds a key-value pair. The key is called ‘key’ and the value is the api_key, which is currently 42. 

    url = serviceurl + urllib.parse.urlencode(parms)
#urllib.parse is a module 
#Part of this module is urlencode. So you are calling urlencode from the urllib.parse module. 
#urllib.parse.urlencode takes a dictionary of key-value pairs (the query parameters) and returns a URL encoded string 
#Can refer to this for info about urlencode() [SOLVED] Python URL Encode? Using urllib.parse Functions (ioflood.com)
#Then you take the URL encoded string and join it to the end of the serviceurl. That’s how you get the website. 

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
#urlopen from urllib.request module opens a url, which can be either a string containing a valid, properly encoded URL, or a Request object. 
#urllib.request — Extensible library for opening URLs — Python 3.12.0 documentation


    data = uh.read().decode()
#Reads and decodes the url from byte objects to strings. 

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
#Makes sure that the data is in JSON format and can be read as a JSON. Returns a Python dictionary (Python object). 
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
#Used to make sure that the JSON data is good for usage. 
# #Also printed out when the wrong API key is used.  
#The status will say other things if it doesn’t work out. Geocoding request and response  |  Geocoding API  |  Google for Developers

    #print (js)
    print(json.dumps(js, indent =4))
    #print ('This is the type of js', type(js))
    #Note: js is still in dictionary form even after the json.dumps printing.  

#Converts Python object into JSON and prints it out. 
#The indent as a parameter changes how the printing is done. 
#Python JSON (w3schools.com)
#You need json.dumps printing statement to print out the JSON in a nice, spaced out format. 
#If you don't have this, then you'll print out the dictionary as it is, which can be messy to read. 
#With the json.dumps(js) printing, the lines are more spaced out and you can see how the "branches work"
#indent helps space out the characters more. 
#Later code of lat = and lng= would still work even if print(json.dumps(js, indent = 4)) wasn't there. 
#This is because the later cod eof lat = and lng = could still easily access the Python dictionary. 
#However, the printing of js as a Python dictionary would look ugly. 



    lat = js['results'][0]['geometry']['location']['lat']
    #Accesses the first index of results, which there is only one. 
    #Accesses the geometry -> location -> lat value 

    lng = js['results'][0]['geometry']['location']['lng']
    #Accesses the first index of results, which there is only one. 
    #Accesses the geometry -> location -> lng value 

    print('lat', lat, 'lng', lng)
#Print out the latitude and longtitude 

    location = js['results'][0]['formatted_address']
    #Accesses the first index of results, which there is only one. 
#Accesses the formatted address value. 

    print(location)

    #Prints out the location that was inputted initially but formatted better. 
