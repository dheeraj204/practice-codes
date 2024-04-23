##Tuples are immutable means we cant change
# TUuples are in ()
# mutable lists
list_1 = ["history", "math", "physics", "compsci"]
list_2 = list_1
print(list_1)
print(list_2)
##
list_1[0] = "art"
print(list_1)
print(list_2)

# To create empty list
empty_list = []
empty_list = list()

##immutable
# tuple_1=('history', 'math', 'physics', 'compsci')
# tuple_2=tuple_1
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0]='art'
# print(tuple_1)
# print(tuple_2)

# To create empty tuple
empty_tuple = ()
empty_tuple = tuple()

## SETS
# sets are in {}
# unlike lists and tuples sets doesnt have indexing which gives random order each time we execute
# it remove duplicate values
cs_courses = {"history", "math", "physics", "compsci", "math"}
print(cs_courses)
##
cs_courses = {
    "history",
    "math",
    "physics",
    "compsci",
}
art_courses = {
    "history",
    "math",
    "art",
    "design",
}
print(cs_courses.intersection(art_courses))  # gives common items
print(cs_courses.difference(art_courses))  # gives non common items
print(cs_courses.union(art_courses))  # combines both sets


# To create empty sets
empty_set = {}  # this is dict not empty set
empty_set = set()
