import random
#seed, fix random number generate every time 
#randrange (start,stop,step)start+2
#default range  starts from 0
# value = random.randrange(1,100)
# print(value)

#suffle  Sequence , = List , string or tuple 

# listtry = [1,2,3,4,5]
# random.shuffle(listtry)
# print(listtry)



# greeting = ["hello","Hi","Hey"]
# userinput = input("Enter your name: ")
# # print(userinput)
# value = random.choice(greeting)
# print( value + userinput )

#Choices random.choices(sequence, weights=None, cum_weights=None, k=1)
balls = ["red","green","yellow"]
chocieresult = random.choices(balls,weights=[0,0,2],k =10)
print(chocieresult)


random.shuffle(balls)
print(balls)



#uniform distribution and discrete 