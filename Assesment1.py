
'''Sample input:
enter a 1 sentence quote, non-alpha separate words: Wheresoever you go, go with all your heart

Sample output:

WHERESOEVER
YOU
WITH
YOUR
HEART '''

string= input("enter a 1 sentence quote, non-alpha separate words: ")
word= string.split(" ")

for i in word:
  if (i[0].lower()>= "h") :
    comma_index= (i.find(","))
    fullstop_index= (i.find("."))
    exc_index= (i.find("!"))
    
    if (comma_index != -1):
      print (i[:comma_index])
      
    elif (fullstop_index != -1):
      print (i[:fullstop_index])
    
    elif (exc_index != -1):
      print (i[:exc_index])
    
    else: 
      print (i)

	  











		



