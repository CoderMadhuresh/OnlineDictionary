# application programming interface
# javascript object notation
import requests # import 'requests' module for pulling online requests
text = input('Enter the word - ') # enter the word from user, to find the meaning of that word
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+text # use dictionary api for getting the meaning of that word 
meaning = requests.get(url).json() # now convert that requests into json format
txtMeaning = str(meaning[0]['meanings'][0]['definitions'][0]['definition']) # fetch meaningful keywords from json format
print('Meaning -',txtMeaning) # print meaning of that word.

