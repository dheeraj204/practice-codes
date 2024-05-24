message = "Hello World"
print(len(message))  # length of string
print(message[0])  # indexing
print(message[0:5])  # slicing
print(message[:5])  # slicing
print(message[4:])  # slicing
print(message.lower())  # changes all characters in string to lower cases
print(message.upper())  # changes all characters in string to upper cases
print(message.count("l"))  # counts no.of times the given character appears in string
print(
    message.count("Hello")
)  # counts no.of times the given character appears in string gives 1 because it takes whole word as a count
print(message.find("l"))  # it gives the index where the character appears first
print(
    message.find("World")
)  # it gives the index where the character appears first irrespective of character or word
print(message.find("universe"))  # it gives -ve since the given word is not in string
new_message = message.replace("World", "universe")
print(
    message
)  # doesnt replace world with universe we have to create a new variable to do so
print(
    new_message
)  # here it replaces the world with universe  it is not neccesary to create entirely new variable we can do message=message.replace('','')
# combining strings
greeting = "Hello"
name = "Dheeraj"
say = greeting + name
print(say)  # simply combines both strings without space b/w them
say = greeting + " " + name
print(say)  # it overcomes the problem above
say = greeting + " " + name + ".welcome!"
print(say)
say = "{}, {}.welcome!".format(greeting, name)
print(say)
say = f"{greeting}, {name}.welcome!"  # f strings are used to replace the format method like above
print(say)
say = f"{greeting.lower()}, {name.upper()}.welcome!"  # f strings are used to replace the format method like above
print(say)
# print(dir(name)),print(help(str)),print(help(str.lower))
