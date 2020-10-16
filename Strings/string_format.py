#string formating
# age = 23
# name = "sujana"
# print("My age is {0} years".format(name))

# #example of literal , %s , %d
# print("My name is %s and my age is %d" % (name,age))


# stringexample = "There are {0} days in {1},{2},{3},{4},{5},{6} and {7}"
# print(stringexample.format(7 ,"jan","feb","march","feb","jan","feb","jan"))

# print("""
# 	Feb:{0}
# 	March:{2}
# 	Jan:{0}
# 	April:{2}
# 	may:{0}
# 	Jun:{1}
# 	""".format(28,230,31))

# stringexample2 = """
# 	Feb:{0}
# 	March:{2}
# 	Jan:{3}	
# 	April:{4}
# 	may:{5}
# 	Jun:{6}
# 	"""
# print(stringexample2.format(28,29,30,88,89,56,89)
# 	)

#for loop

# for i in range(1, 12):
# 	print("No. %4d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))
   

# print("Pi is approximately %-12f" % (22 / 7))


for i in range(1, 12):
	# 0 is place value and 2 is padding 
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# for i in range(1, 12):
#     print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# print("Pi is approximately {0:12.50f}".format(22 / 7))
# print("Pi is approximately {0:52.50f}".format(22 / 7))
# print("Pi is approximately {0:62.50f}".format(22 / 7))
# print("Pi is approximately {0:72.50f}".format(22 / 7))

# for i in range(1, 12):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
