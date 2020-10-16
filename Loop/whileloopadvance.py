
#we use while loop when we need to execute for n or unknown number of times where n is know at the run time ,

i = 1
while i<=5:
    print("Sujana")
    i = i + 1

i = 5
while i>=1:
    print("Sujana")
    i = i-1

i = 1

while i<=5:
    print("You", end="")
    j=1
    while j<=5:
        print("rocks", end="")
        j = j+1

    i = i+1
    print()

Some questions 
1 sum of first natural numbers
i = 1
sum = 0
while i<=10:
    sum = sum + i
    i = i + 1
print(sum)

#sum of even number 
i =1
sum = 0
while i<=10:
    if i%2 == 0:
        sum = sum + i 
    i = i +1
print(sum)  
    

usernumber= int(input("Enter the number "))
reversenumber = 0
while usernumber%10!=0:
    c = usernumber%10
    reversenumber = reversenumber*10 +c 
    usernumber =usernumber//10 # here now result would be integer ie if 5689 then 568.9 but it makes interger it 568
print(reversenumber)


calculate the lenght of list without using len function
we use IndexError because after 3rd position in the list there is no any element

x = [1,2.3,"Lengthofstring"]


length = 0
i = 0
try:
    while x[i]:
        length = length + 1
        i = i + 1
except IndexError:
    print(length)





Simple game to guess the number
import random
randomnumber = random.randint(1000,9999)
inputnumber = int(input("Enter the 4 digit number"))


while inputnumber!=2:
    num = randomnumber
    correct= 0 
    #Lets extract each number, continue till there is no number, while doing n%10
    while num%10 :
        lastnumber = num%10
        guessednum = inputnumber%10
        num = num // 10
        inputnumber = inputnumber//10
        if lastnumber == guessednum:
            correct = correct+1
    if correct == 4:
        print("congrats")
        break #if all the guessed numbers are wright
    else :
        print("%d digits are wright" %correct)
        inputnumber = int(input("Enter the 4 digit number"))

else:
    print("You quit the game")
















