#import random module 
import random 
randomnumber  = random.randint(1000,9999)  
# print(randomnumber)
inputnumber = int(input("Enter 4 digit number"))


#while loop: We use whileloop when we don't know how long we have to execute the block of code  eg for 'n' number of time

while inputnumber!=0:
    num = randomnumber
    correct = 0 
    while num%10==0:
        lastnumber = num%10
        guessednum = inputnumber%10
        num  = num // 10
        inputnumber = inputnumber // 10
        if lastnumber == guessednum :
            correct = correct + 1 
    if correct == 4:
        print("Congrats")
        break
    else:
        #%d , dynamically take a integer values ,%s takes string
        print("%d digit are wright" %correct)
        inputnumber = int(input("Enter the 4 digit value"))
else:
    print("You quit the game")






