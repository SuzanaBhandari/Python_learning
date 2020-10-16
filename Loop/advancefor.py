

# #Program to print,skip or exit 
# inputnumber = int(input("Enter the value")) 


# for i in range(inputnumber):

#     choose_option = input("skip,print or exit")
#     if choose_option == 'print':
#         print(i) 
#     elif choose_option == 'skip':
#         continue
#     elif option == 'exit':
#         break

# print("Completed")

# print the pattern

1
22
333
4444
5555

inputnum = int(input("Enter the number"))
i =1 #number of rows 
#inputnum + 1 because range includes(1,6) as 1-5
for i in range(1,inputnum+1):
#this for column
    for j in range(1,i+1):
        print(i,end="")
    #for new line 
    print()

print the pattern
1
12
123
1234
12345

inputnum = int(input("Enter the number"))
i =1 #number of rows 
#inputnum + 1 because range includes(1,6) as 1-5
for i in range(1,inputnum+1):
#this for column
    for j in range(1,i+1):
        print(j,end="")
    #for new line 
    print()


# presentPrices = []
# for i in range(5):
#     price = input("How much did this present cost in pounds")
#     price = float(price)
#     presentPrices.append(price)
#     print(presentPrices)

# #total up the list 
# print("Total:",sum(presentPrices))
# print("Total:",sum(presentPrices))
