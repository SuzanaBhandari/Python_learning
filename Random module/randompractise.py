import random
#random() returns floating number between 0 and 1
value = random.random()
print("so random() is", + value )


#randrange(1,10)
randrangevalue = random.randrange(1,10)
print("so randrangevalue is", + randrangevalue )

#here value comes between 1-10 and step count will be 2  , where 1 can be included but not 10
randrangevaluestep = random.randrange(1,10,2)
print("so randrangevaluestep is", + randrangevaluestep )

randrangevaluestep = random.randrange(1,2)
print("so randrangevaluestep is", + randrangevaluestep )


#default example  , here values are displayed between 0-20

randomdefault = random.randrange(20)
print("so randomdefault is", + randomdefault )

#this display both 1-10
value = random.randint(1,10)
print(value)

#shuffle, This method takes a sequence (list, string or tuples): Syntax: random.shuffle(sequence,function)
listtry = [1,2,3,4,5]
examl = random.shuffle(listtry)
print(random.shuffle(listtry))

#seed , If we want to fix the generation of thr random variabke

random.seed(10)
print(random.random())

random.seed(10)
print(random.random())


greetings = ["hello","Hi","Hey"]
value = random.choice(greetings)
print(value + ', Sujana')

colors = ['Red','Black','Green']
results = random.choices(colors,weights=[18,18,2] ,k=10)
print(results)

