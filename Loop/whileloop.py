#Python has two primitive loop commands:1) while loops 2)for loops

#While loop: we can execute a set of statements as long as a condition is true.

# i = 1
# while i <= 8 :
# 	print(i)
# 	i += 1

# #With the break statement we can stop the loop even if the while condition is true

# i = 1
# while i<6:
# 	print(i)
# 	if i==3:
# 		break
# 	i += 1


#With the continue statement we can stop the current iteration, and continue with the next:
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

j = 1
while j < 6:
  print(j)
  j += 3
else:
  print("i is no longer less than 6")