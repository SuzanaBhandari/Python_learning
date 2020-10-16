#Multiline string 
intro = """My name is sujana and 
I am currently working as a software developer. 
I live in pokhara """

print(intro)


# strings in Python are arrays of bytes representing unicode characters.

example = "Hello,world "
print(example[2])

#Slicing ,Returns a range of characters by using the slice syntax.

print(example[2:5])
print(example[-5:])
print(len(example))

#strip() removes whitespace

example1 = " Hello, World! "
print(example1.strip())

#turns strings in lower case
print(example1.lower())

#turns strings in lower case
print(example1.upper())

#Replacing the characters
print(example1.replace("H","J"))

#Split , IT splits string , if it finds any seperator .
print(example1.split("."))
print(example1)

#Check string 

search_string = "I am sujana"
x = "rr" in search_string
print(x)