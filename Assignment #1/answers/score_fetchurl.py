'''
Created on Sep 4, 2013

@author: Chaitu
'''
#Fetching arguments from user
#Displaying the number of arguments given by user
#Second argument as number of seconds , condition to display number of minutes according to the number of seconds passed
#Defining a function to parse the argument i.e. URL
#User's input for the week's number , condition to check if it between 0 and 3 else display invalid week
#If True , open the url using urlopen function
#Downloads the source code of the url
#Using beautiful soup to parse the HTML and extracting only the text
#Removing noisy data using indexing and fetching the required text
#Format according to the text and store it in a list
#Formatting according to the output like the team score and team with which it played
#Searching the list with the user provided argument team name
#Fetch the result
#Remove invalid data
#Display the output
#Refresh the page every 30 seconds until user has terminated.

import sys
from bs4 import BeautifulSoup
import urllib.parse
import time
from urllib.request import urlopen

print ('Number of arguments:', len(sys.argv[1:]), 'arguments.') #argv[0] name of the script
#Printing Number of minutes according to the number of seconds provided at the cli argument
if int(sys.argv[2]) == 60:
    print("It is one Minute")
else:
    res = float(sys.argv[2])/60
    print("%s Number of Minutes " %res)
#Defining a function to fetch url and print the scores    
def main():
    #User's input on the week number i.e. 1 & 2 
    week = int(input("Please enter which week's result you would like to see: ") )    
    param = urllib.parse.urlencode({'conf':'all','week':week})
    #If true execute this
    if (0 < week < 3 ):
        #Loop to refresh page
        while True:
            raw_url = sys.argv[3]                        #Taking url
            url = raw_url + '?' + param                  #concatenating the exact URL
            print("Score retrieved from",url)            #displaying the URL
            page = urlopen(url)                          #opening the url , which downloads the html code
            soup = BeautifulSoup(page)                   #Parsing the html code
            clean = ''.join(soup.findAll(text=True))     # removing tags , displaying the text
            clean_cut = clean[17552:23765]               #Indexing just the games, removing everything else
            lines = clean_cut.split('\n')                #Formatting accordingly
            clean_lines = [l.strip() for l in lines]     #Creating a list and storing
            #Removing the invalid data
            a = ['Final','','Friday, September 6','Saturday, September 7','Final OT','7:00 PM EDT','Stetson','@','Florida Tech'
                 'Monday, September 2','Thursday, August 29','Friday, August 30','Southwestern Athletic', 'Weeks:',
                  '1','2', '3', '4','5', '6', '7','8', '9', '10','11', '12', '13','14', '15', 'Bowls/Postseason','Home', 'Score', 'Away','Saturday, August 31','Final 2OT']
            new_clean =[x for x in clean_lines if x not in a]
           
            #Formatting accordingly with scores and teams
            games = [new_clean[i:i+3] for i in range(0, len(new_clean), 3)]
            #print(games)
            #searching for the string , if true print this
            if any(sys.argv[1] in s for s in games):
                matching = [s for s in games if sys.argv[1] in s]
                full_clean = str(matching)[2:-2]
                result = full_clean.replace("'","")
                print(result.replace(",",""))
                time.sleep(30)    #Refreshing Page 30 seconds
            else:
                print("No matches/scores found")
                break
    #If false , print this       
    else:
        print("Invalid week")
        main()


main()
print ('Argument List:', str(sys.argv[1:]))
#prints all the arguments
