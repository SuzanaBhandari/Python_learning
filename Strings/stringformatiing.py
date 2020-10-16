#string concatenation
a = "sujana"
b = "bhandari"
c = a + b
print(c)

age = 23
name = "sujana"

print("My age is " + str(age))
#manually insert 
print("My age is " + str(age) +" " + "years")

#format(), dynamic procedure 
print("My age is {0} years".format(age))






print ("My name is %s and My age is %d" % (name,age))

print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}".format(31,"Jan","May","Mar","July","August","October","December"))
print("""
	Feb:{0}
	March:{2}
	Jan:{0}
	April:{2}
	may:{0}
	Jun:{1}
	""".format(28,230,31))

print("My age is %d %s %d %s" %(age ,"years",6,"month"))