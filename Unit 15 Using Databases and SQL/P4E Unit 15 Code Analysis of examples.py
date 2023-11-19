#Chapter 15: Using Databases and SQL 

#Since there are no exercises here, I have copied the code examples from the book and written down what each line/block of lines does 

#Code Block #1 
#Going through users and their friends, putting them into a database, and seeing how popular they are. 

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
#Connect to a database stored in file spider.sqlite. Will make one if it doesn’t exist. 

cur.execute('''CREATE TABLE IF NOT EXISTS Twitter(name TEXT, retrieved INTEGER, friends INTEGER)''')
#Make a table called twitter if it doesn’t exist. The table consists of columns titled “name” (text as value type), “retrieved” (integer as value type) and “friends” (integer as value type). 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#Ignore the security settings 

while True: #Holds up all the time until you stop it or it breaks 
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
    #If you just hit the enter button 
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        #From the table Twitter, SELECT a name from the names column WHERE an entry in that row has 	value of 0 in the “retrieved” column. You can only select one row. 
        try:
            acct = cur.fetchone()[0]
            #Account variable is now the first element from that selected row. In this case, it is the Name. 
            #fetchone() by itself outputs a tuple, but you only want the integer only. That’s why the [0] is added at the end. 
        except:
            print('No unretrieved Twitter accounts found')
            continue
            #loop back up so you have the option to put in another input

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
#Only counting 20 friends of the selected account. 

    print('Retrieving', url)

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    #This is all for accessing the website. You get the friends and statuses for that user. 
    #The bytes object is decoded into strings. 
    #You save the headers in a dictionary and use the .getheaders() function to get the headers. 

    print('Remaining', headers['x-rate-limit-remaining'])
    #For Twitter, the x-rate-limit-remaining is the number of times you have left for a given endpoint within a window (usually 15 requests per 15 minutes 

    js = json.loads(data)
    #Transforms the JSON data into a Python object (usually a dictionary) 

    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))
    #You update the table with the “retrieved” column value = 1 for the row WHERE the “name” column Value is the acct variable. 

    countnew = 0
    countold = 0
    for u in js['users']:
    #Going through each index of the  ‘users’ branch of the JSON dictionary. 
        friend = u['screen_name']
        #Obtainig the value in the key-value pair of (screen name-[actual screen name]). U is probably a dictionary as well

        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
        #From the Twitter table, SELECT from the column friends WHERE one of the rows has the screen name that we saved as the variable friend. You only get one friend in question with the limit statement. 
        try: #Try statement goes through if the screen name exists in the table Twitter already. 
            count = cur.fetchone()[0]
            #Get the current friends value for the individual. This is done because we are selecting From the friends column already, which is the count of how many friends they have. 
            #fetchone() by itself outputs a tuple, but you only want the integer only. That’s why the [0] is added at the end. 

            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend))
            #Update the Twitter table and SET the friends value to +1 of what it was once before For the row WHERE the name value is equal to the screen name. 

            countold = countold + 1
            #Since we have seen this screen name before, +1 is added to countold variable. 

        except: #Except statement goes through if the screen name doesn’t exist in the table Twitter. 
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)''', (friend, ))
            #Insert into table Twitter a new row into the columns name, retrieved, and friends with the values of the screen name (aka variable friend), 0, and 1, respectively. 
            countnew = countnew + 1
            #Since we have never seen this screen name, +1 is added to countnew variable.  

    print('New accounts=', countnew, ' revisited=', countold)
    #Prints out how many new accounts were added to the database and how many accounts from the database we went through. 

    conn.commit()
    #Save the database and commit to all the updates 

cur.close()


#Code Block #2. 
#A refined version of Code Block #1 
#going through users and their friends, putting them in a database, and detailing the connections between individiuals. 

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
#Makes database friends.sqlite if it doesn’t exist. 
#Connects to the friends.sqlite if it does exist. 

cur = conn.cursor()
#Basically a file handle for databases. 
#Allows us to perform operations on the data stored in the database

cur.execute('''CREATE TABLE IF NOT EXISTS People
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
    #Creates a table called People if it doesn’t exist. The People table will have the columns (in order) of id (type of integer primary key), name (type text that has to be unique within the table), and retrieved (type integer) 
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

    #Creates a table called Follows if it doesn’t exist. The Follows table will have the columns (in order) of from_id (type integer), to_id type integer, and the combination of from_id and to_id is UNIQUE. 


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
    #Accessed if you just press the enter key
        cur.execute('SELECT id, name FROM People WHERE retrieved=0 LIMIT 1')
	    #SELECT columns id and name FROM the People table WHERE the value in the retrieved column is equal to 0. You are selecting the first row that fulfills this condition. 
        try:
            (id, acct) = cur.fetchone()
	        #Fetching the tuple from columns id + name and storing them in the tuple (id, acct) 

        except:
            print('No unretrieved Twitter accounts found')
            continue
	        #Except statement accessed if none of the rows fulfilled the line of code above the try statement. 

    else:
    #Accesed if you did put in a name in the input section. 
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',(acct, ))
	    #SELECT from column id FROM the table PEOPLE WHERE the name is equal to your input. You are selecting the first row that meets this criteria. 

        try:
            id = cur.fetchone()[0]
	        #Storing the first element from that row’s id column as the id variable. You have to do this because fetchone() usually returns a tuple. 

        except:
	    #Accessed if the name you inputted isn’t in the database already. 

            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) VALUES (?, 0)''', (acct, ))
	        #INSERT a row INTO table People. In that row, to the columns name and retrieved, you will add the values of your input and 0, respectively. 
	        #The IGNORE is there so that all the names in People table are unique. You can ignore the INSERT to maintain the uniqueness of the values in the name column. 
            conn.commit()
	        #Save the changes to the database
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
		        #If the row wasn’t added properly, then a print statement saying the insertion didn’t go well occurs, and you’ll loop to the very beginning. 
            id = cur.lastrowid
	        #The id for the row is assigned by the database. You get the id by doing cur.lastrowid. 

    url = twurl.augment(TWITTER_URL, 
        {'screen_name': acct, 'count': '100'})
    #The url you will access will be the account you entered and a 100 of their top friends. 


    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
	    #Try to make the connection to the url. Trying to open the url. 
    except Exception as err:
        print('Failed to Retrieve', err)
        break
	    #If the connection doesn’t work, then you exit the whole while loop. 

    data = connection.read().decode()
    #Read the data and transform the data from bytes to strings. 
    headers = dict(connection.getheaders())
    #Stores the headers in that url in a dictionary called headers.  

    print('Remaining', headers['x-rate-limit-remaining'])
    #For Twitter, the x-rate-limit-remaining is the number of times you have left for a given endpoint within a window (usually 15 requests per 15 minutes 


    try:
        js = json.loads(data)
	    #Convert the JSON data into a Python object(a dictionary) 
    except:
        print('Unable to parse json')
        print(data)
        break
	    #if you can’t convert the JSON data into a Python object, then you break the while loop. 

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue
	    #If ‘users’ is not in the dictionary of JSON data, then you go to the beginning of the While loop. 

    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))
    #You UPDATE the people table’s column retrieved to 1 for the row WHERE the name is equal the account you entered. 

    countnew = 0
    countold = 0

    for u in js['users']:
    #Going through each index of the ‘users’ node of the JSON dictionary. 
        friend = u['screen_name']
	    #Obtianing the value in the key-value pair of (screen name-[actual screen name]). U is probably a dictionary as well. 

        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
	    #From the People table, SELECT from the id column WHERE one of the rows has the screen name that we saved as the variable friend. You only get one friend in question with the LIMIT condition. 
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
	        #This try statement goes through if the friend of the user we initially inputted is already in the database.
	        #You get the friend_id associated with the screen name. 
	        #Need to do fetchone()[0] because you are getting the value from the column id, and you don’t want a tuple. 
	        #By accessing someone already in the database, you add +1 to countold 

        except:
	    #This except statement is accessed if the friend is not present in the People table at all

            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                        VALUES (?, 0)''', (friend, ))
	        #Add a new row INTO People table with column values of friend variable and 0 for columns name and retrieved, respectively. 
	        #If the username is already in the database, then you ignore the addition so that you don’t have repeats. 

            conn.commit()
	        #Save the changes to the database. 
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
	 	    #If we could not add the row, then we print an error statement and go back to the beginning of the while loop 
            friend_id = cur.lastrowid
	        #You get the friend_id by obtaining the id from the last row you added. This id was assigned by the database. 
            countnew = countnew + 1
	        #Adding +1 to countnew because you are added a new account to the table. 
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
	    #You INSERT into Follows table columns from_id, to_id the values of variables (id, friend_id). You ignore the addition if the COMBINATION of id and friend_id already exists. Example, if (1,5) exists, then (5,1) wouldn’t be added. 

    print('New accounts=', countnew, ' revisited=', countold)
    #Tells us how many new accounts we added to the database and how many accounts we revisited that were already in the database

    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
    #Save your changes to the database. 
cur.close()


#Code Block #3 
#Joining the tables outputted from Code Block #2 based on matching characteristics 

import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()
#Connect to the database friends.sqlite
#Cursor() used so that you can perform operations on the data stored in the database. Analogous to a file handler. 

cur.execute('SELECT * FROM People')
count = 0
print('People:')
for row in cur:
    if count < 5: print(row)
    count = count + 1
print(count, 'rows.')
#Prints out the first rows from al the columns in the People table 
#Prints out how many rows exist in People table. 

cur.execute('SELECT * FROM Follows')
count = 0
print('Follows:')
for row in cur:
    if count < 5: print(row)
    count = count + 1
print(count, 'rows.')
#prints out the first 5 rows from all the columns in the Follows table 
#Prints out how many rows exist in the Follows table. 

cur.execute('''SELECT * FROM Follows JOIN People
            ON Follows.to_id = People.id
            WHERE Follows.from_id = 2''')

#Selects all the columns from both tables Follows and People. We are joining the columns ON the condition that the Follows.from_id (Follows table, from_id column value) is equal to the people_id value for the rows (WHERE) people_id = 2 (aka id in People table is equal to 2)  
#The order of the columns in the outputted table are from_id, to_id, id, name, and retrieved. 
#From_id and to_id are from the Follows table 
#id, name, and retrieved are from the People table 

count = 0
print('Connections for id=2:')
for row in cur:
    if count < 5: print(row)
    count = count + 1
print(count, 'rows.')
#Prints out the first five rows of the joined table. 
#Prints out how many rows exist in the joined table. 

cur.close()
