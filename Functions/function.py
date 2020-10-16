#Function is a block of code which runs when it is called and can pass data ,known as parameter

#example 1
# def my_fuction1():
# 	print("Hello this is  fucntion block")
# my_fuction1()

# #Arguments: Information can be passed into functions as arguments
#We also call arguments as args

# def my_function2(fname):
# 	print(fname + 'Try block')

# my_function2("Email")
# my_function2("Sujana")
# my_function2("Facebook")
# 

#Parameters and Agruments
""" 
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

#Example of Argument 
# def my_function3(fname,lname):
# 	print(fname+ " " + lname)
# my_function3("Sujana","Bhandari")

#Arbitrary arguments, *args
"""
If we do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

# def my_function4(*myintrest):
	
# 	for i in myintrest:
# 		print("My intrest are" +" " + i)

# my_function4("Dancing","Singing","Watching")


# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#   #kids[2]="suja"
# my_function("Emil", "Tobias", "Linus")



#Keyword Arguments ie Key , value pairs
# def my_function5(intrest1,intrest2,intrest3):
# 	print("Let's try" + intrest2)

# 	my_function5(name)
# my_function5(intrest1="Dancing",intrest3="Singing",intrest2="Watching")


#Arbitrary Keyword Arguments, **kwargs
# def my_function6(**intrests):
# 	print("My intrests are" + intrests["intrest1"])
# my_function6(intrest1 = "Dancing", intrest2="Singing")

#Default parameter value 

# def my_function7(intrest = "Dancing"):
# 	print("My intrest is" + intrest)
# my_function7("Singing")
# my_function7("Dancing")
# my_function7()

# passing a list as an Argumnet
# def function8(intrest_list):
# 	for x in myintrest:
# 		print(x)
# myintrest = ["Dancing","Singing","Reading"]

# function8(myintrest)


# #Return values
# def function9(return_value):
# 	return 5*return_value

# print(function9(5))
# print(function9(10))
# print(function9(11))
# print(function9(12))

#pass statement:function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# def pass_function():
# 	pass
"""
Python also accepts function recursion, which means a defined function can call itself.
 It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

"""

def trecursion(k):
	if(k>0):
		result = k + trecursion(k-1)
		print(result)
	else:
		result = 0
	return result
print("Recursion example result")
trecursion(5)
