#There are 2 types of functions:
# 1. User Defined Functions
# 2. Lamda Functions(Unnamed Functions). Used only Once

#User Defined Function

def Average(x,y):
    avg = (x + y)/2
    print("Average of ",x, "and ",y, "is", avg)
#Here i have defined a function called Average that finds the average of two numbers
#A user Defined Function can be used more than once until the pthon memory is erased
    
Average(3,4)

Average(5,6)

#Lets define a function that finds the max number

def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1,"is greater")
    elif num2 > num1 and num2 > num3:
        print(num2,"is greater")
    else:
        print(num3,"is greater")
        
max_num(2,5,6)

max_num(100,2,1)

#Example
#Lets define a function to find the square of a number
def square(x):
    return x*x
    
square(6)
square(3)


#Lambda Functions
#It is not stored in the python memory
#This function can be used to execute a code only once

#the syntax for lambda function is as follows

variable name = lambda x : (function/condition) #This is just a syntax. #Dont run this line

#lets see an example

g = lambda x:x*x*x #this is a function to find cube
g(2)

#Filter Function for lambda

list1 = [3,2,6,77,85,96] #I have created a list
final_list = list(filter(lambda x: x%2 !=0,list1)) #This will create a new list which will contain values of list1 whose remainder is not equal to 0 when divided by 2

#Map Function

final_list1 = list(map(lambda x: x*2,list1)) #This will multiple each element of list1 with 2

