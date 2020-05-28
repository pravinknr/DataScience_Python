#Nameerror - not defined to Python
#Syntax Error - there is an syntax error

#Indexing #Accessing Vlaues in a file

Name = "PRAVIN" #Assigning a value to the variable Name
print(Name) #To print the value of the vriable

print(Name[2]) #Prints the value of the variable Name with index 2

Name #This also prints the value of the variable Name

Name[3:5] #Slicing #this prints the value of variable from index 3 to 4. the upper limit index is ignored

Name[1:] #This prints the value with index 1 till the last index as the upper limit is not mentioned

#Negative index is used to access the data from the last

Name[-1] #Tjis will return the last value of the variable. 

 Name[-5:-1] #This will print the values having index -5 till -1 but excludes the -1 index as upper limit is excluded
 
#Update Strings
 
 variable = "Hello People" #Creating a variable
update = variable + ", How are you" #Creating a new variable that contains other variable data 

print("Updated", update)

#String Formating
#%s = String
#%d = Integers
#%f = float values #%.(no. of decimals)f
  
print("My name is %s and my weight is %d and i have completed %s"%("pravin",60,"B.Sc")) #This is an example of String Formatting


Number = 30 #This is called HardCoding where the variable value is pre defined as 30

Number1 =, ,input("Enter Number: ") #This is called Softcodig where the value is taken from the user
,,
Nu,mber1 = eval(input("Enter Number:")) #The eval function automatically evaluates the data type of the value. here it is a integer
#Example
Name = input("Enter Name") #String
Weight = eval(input("EnterWeight:")) #Float or Integer
(Name,Weight) #Prints the values of Name and weight

#Statement #Triple quotes
Statement = """Hello, My name is "Pravin".""" #triple quotes is used to write statements
Statement


name = "Pravin"
name.upper() #It Converts the value into upper case

name.lower() #It converts the values into Lower case

name.center(50) #It prints the value in the center. It gives the specified number of spacing

#Count Function

name.count("Pravin") #Counts the number of times Pravin has appeared in the data

name.count("P")

string = "pravinpravinpravin"
substring = "a"
string.count(substring) #This will count the number of times a has appeared in the variable string

string.isalnum() #or .isdigit() #This checks if all the characters are numeric or not

string.isalpha() #Check if all the characters are alphabetic. It will return false if there is atleast 1 blankspace

#Replace function

string = "Hello, welcome to my GitHub Profile"
string.replace("Hello","Good Morning")#This replaces Hello with Good Morning

split="line1, line2, line3, line4"
split.split(",") #This will replace the values of the string with respect to ","

#Lists and Tuples
#List is represented by [""] . It is Mutable. Changes can be made.
#Tuple is represented by ("") . It is Immutable. Changes cant be done.

list1=["pravin","mandar",2018,2019] #Creating a list
list2=[1,2,3,4,5]
list3=["a","b","c","d"]

listn=[list1,list2,list3] #creating lists inside a list

id(list1) #returns the id value of the list assigned by the python

list2[0] #returns the value of list2 with index 0

list1.pop() #removes the last value of the list. we can also specify the index value in the bracket

list1[0]="Pravin" #This will replace the value of list1 with index 0 with the specified value

del(list3[1]) #This deletes the value of list3 with index 1

list3.append("b") #this will add the element "b" to the list3 at the last

list3[1:4] #Slicing  #returns the values with index 1,2,3. the upper limit is excluded

list1.insert(0,"bhupend")#This will insert the element in the list into the specified index.

alist = [1,2,3]
blist = ["a","b"]
alist.extend(blist) #Extend function is used to add two lists

alist.reverse() #this will reassign the elements of the list into reverse manner

list5 = [99,5,40,63,1,7,2]
list5.sort() #This will sort the values of list in ascending order. (reverse=True) will give descending order

list5.count(99) #Counts the value 99 in the list

#Tuples

#Creating Tuples
tup1 =("a","b","c")
tup2 = (1,2,3)
tup3 = ("pravin","bhupend",2018)

id(tup1) #To get the id of the tuple

#Accessing values in tuple
tup1[0] #Returns the value of tup1 with index 0

tup2[-2]

tup3[1:3] #Slicing

#Updating a tuple
tup1=(1,2) #This overwrites the variable with new elements. The previous elements are deleted.

#creating a new tuple with existing tuples. #Adding two tuples
tup = tup1 + tup2

len(tup1) #Gives the length of the tuple

tup1.index(2) #This will give the index number of the specified value
tup3.index("bhupend")

del(tup1) #Deletes the specified tuple

tup2*2 #This will print tup 2 twice

3 in tup2 #membership operator

max(tup2) #The max function will give the maximum or highest element of the tuple

min(tup2) #The min function will givethe minimum or lowest element of the tuple



#Dictionary
#Dictionaries are represented with curly barckets {}

dict1 = {"Name":"Pravin","Age" : 22, "Weight" : 60} #":" is used to assign values to the elements of the dictionary
print(dict1) #Prints the entire Dictionary 

dict1["Name"] #prints the value of the element of the dictionary

dict1["Age"]

dict1["Weight"]

#Updating the Dictionary
dict1["Name"] = "Pravin Konar"#Updates the value of Element Name

#Add a new Entry
dict1["Address"] = "Thane" #This will add the element Address with the value Thane

del(dict1["Address"])#This will delete the Element from the dictionary

#creating list inside Dictionary

dict2 = {"Name" : ["Pravin","Konar"],"Age" : [23,22]} #Here we have created a Dictionary that contains Elements that are represented as lists

dict2["Name"][0] #This will return the Name value with index 0 inside the dictionary
dict2["Age"][1]
