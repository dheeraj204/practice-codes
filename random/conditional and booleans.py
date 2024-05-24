if True:
    print("conditional is true")

#
language = "python"
if language == "python":
    print("conditional is true")

# Comparisons:
# Equal:............. ==
# NOt Equal:......... !=
# Greater Than:......  >
# Less Than:.........  <
# Greater or Equal:..  >=
# Less or Equal:.....  <=
# Object identity:...  is

##
language = "java"
if language == "python":
    print("language is python")
elif language == "java":
    print("language is java")
elif language == "javascript":
    print("language is javascript")
else:
    print("No match")
##
# and
# or
# not

user = "Admin"
logged_in = True
if user == "Admin" and logged_in:
    print("admin page")
else:
    print("Bad creds")

#
user = "Admin"
logged_in = True
if not logged_in:  ##it changes logged_in true as false
    print("please log in")
else:
    print("welcome")

##
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)  # though both list are same theyre id's are different so gives false
print(id(a))
print(id(b))
##
a = [1, 2, 5]
b = a
print(a is b)  # since b shares same id as a it gives true
print(id(a) == id(b))

##False values:
# False
# None
# Zero of any numeric type
# Any empty sequence.For example, '',(),[].
# Any empty mapping.For example, {}.

condition = False  # same for none,0,'',()etc
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

##
condition = True  # same for any numeric value except 0 and a filled string like 'test'
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
