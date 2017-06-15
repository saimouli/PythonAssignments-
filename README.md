# PythonAssignments-

#Strings
Negative Indexing string  
 
Ex: Student_name= “Joana”
       print(Student_name[-1]) will give “a” 
Index from reverse order (last first letter) 
 
Index slicing
Ex: Student_name= “Joana”
       print(Student_name[:2]) will give “Jo” 
Notice 2 in not inclusive, whereas [2:4] is [2 to 4)
 
Ex: Student_name[::2] (start value:stop value:step size) will give “Jn”
 
Ex: Student_name[3::-1] will give start value is 3 and -1 so backwards, “naoJ”
 
For loop strings
 
Ex: word= “what”
For letter in word: 
	print (letter) will print “w” “h” a t ..
 
str = "this";  # No space & digit in this string
print str.isalpha()

str = "this is string example....wow!!!";
print str.isalpha()
 
.isalpha 1st one returns true as it contains only strings without spaces 
 
List Sequences 
Empty_list =[]
mixed_list= [“who”, 1, 2, “this is a list]
 
.append() will add and expand the lists 
Ex: A= [1,2,3]
A= A.append(4) will give A=[1,2,3,4]
 
To replace list item
Ex: party_list= [“Joana”, “Alton”, “Tobias”]
Party_list[1] = “Colete” will give [“Joana”, “Colete”, “Tobias”]
 
 
To insert an item 
Ex: party_list[1] = party_list[1] + “ Doresoa”
Will give [“Joana”, “Alton Doresoa”, “Tobias”]
 
.insert() 
Ex: party_list.insert (index #, “something”)
party_list.insert(1,”dora”)  will insert dora at index 1 without replacing the existing one 
 
Del
Ex: del party_list[0]
Will delete Joana
 
.pop()
.pop() method default is last item in a list
last_item = party_list.pop()
first_item = party_list.pop(0)
Ex: num= [11,12,34,56,76,12,10]
num1= num.pop() -> will give [11,12,34,56,76,12]
num2= num.pop() -> will give [11,12,34,56,76]
 
num1+num2-> 10+12= 22
 
Empty list is false
Ex: while party_list:
	Party_list.pop -> will pop all items in list and stops when the list is empty 
 
.remove() (don’t need to index)
Ex: dog_type =[“Lab”, “Pug”, “Poodle”]
 
If “pug” in dog_type:
	dog_type.remove(“Pug”) will remove pug from list 
 
 
 
 
 
 
 
 
 
 
 
 
