
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
  if (i.isalpha()== True) and (i[0].lower()>= "h"):
    print (i.upper())


	  











		



