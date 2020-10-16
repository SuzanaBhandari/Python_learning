# #forloop

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
  



# # Looping Through a String: 

# for x in "banana":
	# print(x)	

#Break statement


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#   	break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# #Continue statement : 

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# #Use of range function : The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
# for x in range(6):
#   print(x)
# for x in range(2, 6):
#   print(x)
# for x in range(2, 30,3):
#   print(x)
  
   

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")


#Nested loop
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjectives:
  for y in fruits:
    print(x, y)

# for x in [0, 1, 2]:
#   pass