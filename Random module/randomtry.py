#example 1

import random
#Display 10 random numbers from interval [0,1)

for i in range(10):
    print(random.random())
#Example 2
#Uniform distribution , ie probability of choosing the number are equally spreaded in interval.
#Generate random numbers from intervals [3,7)
for i in range(3,7):
    print(random.uniform(3,7))


#Normal distribution(Mean and deviation)

for i in range(20):
    print(random.normalvariate(0,0.2))

#Discrete probability distribution , like rolling of die

for i in range (5):
    print (random. randint(1,6))

#Game for rock, paper , scissor

outcomes = ['rock', 'paper', 'scissor']
for i in range(5):
    print(random.choices(outcomes))
