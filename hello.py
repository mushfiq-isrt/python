# print
print("Hello,World")


# taking inputs
#print("What's your name?")
#input()
#print("Hello")
"""
# making it more beautiful
    # ask user for their name
name = input("What is your name? ")
print("Hello")
print(name)
"""
"""
This is
a multi line 
comment
"""

"""
# use of concatination
name = input("What is your name? ")
print("Hello, " + name) # notice there's a space after hello,

# understanding print fucntion
name = input("What's your name? ")
print("Hello, ", end="")
print(name)

# how do you quote in python then?
print('hello,"friend"')

print("Hello,\"friend\"") # used escape character "\"

# final solution?
name = input("What's your name? ")
# removing blank space from str
name = name.strip()

# capitalizing name
#name = name.capitalize() # only the first name gets capitalized
name = name.title()

print(f"Hello, {name}")
"""
# taking input
name = input("What's your name? ").strip().title().strip()

# printing 
print(f"Hello, {name}")

