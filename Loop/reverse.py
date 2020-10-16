usernumber= int(input("""Enter the number
"""))
reversenumber = 0

while usernumber%10!=0: 

    c = usernumber%10 
    
    
    reversenumber = reversenumber*10 + c   

    usernumber =usernumber//10 


print(reversenumber)