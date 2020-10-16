#if condition

a = 20
b = 20
if b>a:
	print("b is greater than a")
elif a==b:
	print("both are equal")
else:
	print("a is greater than b")

#One line conditional statment
print("yes") if a > b else print("B")
 

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#And(Logical operator and used to combine conditional statements)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")


#Nested if : if statement inside if statement
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if b>a :
	pass
