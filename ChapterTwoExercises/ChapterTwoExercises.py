#the following are exercises from chapter two from the book Python Crash Course

#2-1: print a message

message = "Hello World\n"
print(message)

#2-2: print a message, reassign it, then print again

oldMessage = "This is message 1\n"
print(oldMessage)

oldMessage = "This is message 2, but it reassigned message 1\n"
print(oldMessage)

#2-3: personal message, use a variable to print a persons name, and print it

name = "Nick a."
message = "Hello " + name + " How are you\n"

#2-4: name cases, print a name in lowercase, uppercase, and titlecase

#reusing name

#upper

print(name.upper())

#lower

print(name.lower())

#title

print(name.title())

#2-5/6: printf/ format strings

val1 = "Home Depot"
val2 = "Garden"

message2 = f"Hello I Work at {val1} in {val2}\n"
print(message2)

#2-7: stripping strings of spaces 

str = "     this is a test string with a lot of spaces      "

print(str + "\n")
print(str.lstrip())
print(str.rstrip())#cuts spaces of the right side
print(str.strip())#cuts off both left and right spaces

