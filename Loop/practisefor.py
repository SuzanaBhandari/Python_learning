#Program to print,skip or exit 
# inputnumber = int(input("Enter the value")) 


# for i in range(inputnumber):

#     choose_option = input("skip,print or exit")
#     if choose_option == 'print':
#         print(i) 
#     elif choose_option == 'skip':
#         continue
#     elif choose_option == 'exit':
#         break

# print("Completed")

#Print the pattern , Nested for loop example

# 1         1
# 22        12
# 333       123
# 4444      1234
# 55555     12345
# 666666    123456

inputnum = int(input("Enter the number"))
i = 1 
for i in range(1,inputnum+1):
    for j in range(1,i+1):
        print(j,end="") 
    
    print()



