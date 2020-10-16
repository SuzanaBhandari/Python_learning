# #Block of code ,which run it is called and can pass data ,known as paramater
# #Example1

# def play():
    
#     print("I play football")

# play()

# #Argument : An argument is the value that is sent to the function when it is called.
# #Parameter :A parameter is the variable listed inside the parentheses in the function definition.

# def function2(firstname):
#     print(firstname)

# function2("Sujana")    

# def function3(firstname,lastname):
#     print(firstname + " " + lastname)
# function3("sujanaa","bhandari")

#  Arbitrary arugument , Important topic, *args

# If we do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
#Kati ota argument send garney tha navayako bela *
# def function4(*myintrest):
#     for i in myintrest:
#         print("My intrest are" + i)

# function4("Dancing","Singing","Reading")

# def function4(*myintrest):
#         print("My intrest are" + myintrest[2])
# function4("Dancing","Singing","Reading")

# # key , value pair 


# def function6(intrest1,intrest2,intrest3):
#     print("lets try" + intrest1)

# function6(intrest1="Dancing",intrest2="Sing",intrest3="read")

#Arbitrary key word arguments **kwargs
#Arbitrary argument *args 
#key and value

# def function7(**intrests):
#     print("lets try" + intrests["intrest1"])

# function7(intrest1 = "Dancing", intrest2="Singing")

#Default parameter value 

# def function8(intrest="Dancing"):
#     print("My intrestis"+intrest)
# # function8("singing")
# # function8("Reading")
# # function8("kdj")
# function8()

#Passing a list as an argument

# def function9(interest_list):
#     for i in interest_example:
#         print(i)
# interest_example = ["Dancing","Singing","Dancing","Singing"]
# function9(interest_example)


#Return values 
# def function10(a,b):
#     return a*b

# print(function10(8,5))

#Pass Statement 
def pass_function():
    pass