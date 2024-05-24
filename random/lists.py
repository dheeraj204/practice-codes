# Lists are mutable means we can change
# lists are given in []
courses = ["History", "math", "physics", "compsci"]
print(courses)  # prints entire lists
print(len(courses))  # Prints length of list
print(courses[0])  # index of list (history)
print(courses[3])  # index of list (compsci)
print(courses[-1])  # comes from left or comes from last
##  0  1  2  3
## -4 -3 -2 -1
print(courses[0:2])  # print indexes from 0 to 2 but not 2
print(courses[:2])  # prints from beginning to 2 but not 2
print(courses[2:])  # prints upto end from index 2
##add an item to list
##APPEND
courses.append("art")  # adds at end of list
print(courses)
##INSERT
courses = ["History", "math", "physics", "compsci"]
courses.insert(0, "art")  # adds at location index 0
print(courses)
##
courses = ["History", "math", "physics", "compsci"]
courses_2 = ["art", "education"]
courses.insert(0, courses_2)  # inserts entire 2nd list in 1st list in 0th location
print(courses)
print(courses[0])
##EXTEND
courses = ["History", "math", "physics", "compsci"]
courses_2 = ["art", "education"]
courses.extend(courses_2)  # it concatinates both lists internally
print(courses)
##REMOVE
courses = ["History", "math", "physics", "compsci"]
courses.remove("math")  # removes math from the list
print(courses)
##POP
courses = ["History", "math", "physics", "compsci"]
courses.pop()  # removes last  from the list
popped = courses.pop()
print(popped)
print(courses)
##
courses = ["History", "math", "physics", "compsci"]
popped = courses.pop()  # prints popped value
print(popped)
print(courses)
##REVERSE
courses = ["History", "math", "physics", "compsci"]
courses.reverse()  # reverses the list
print(courses)
##sort
courses = ["history", "math", "physics", "compsci"]
num = [1, 5, 3, 7, 2]
courses.sort()  # sorts alphabetical order in the list
num.sort()  # if list contain numbers it sorts in ascending order
print(courses)
print(num)
##reverse sort
courses = ["history", "math", "physics", "compsci"]
num = [1, 5, 3, 7, 2]
courses.sort(reverse=True)  # sorts alphabetical order in the list
num.sort(reverse=True)  # if list contain numbers it sorts in descending order
print(courses)
print(num)
##sortted
courses = ["history", "math", "physics", "compsci"]
num = [1, 5, 3, 7, 2]
sorted_courses = sorted(courses)
sorted_num = sorted(num)
print(sorted_courses)
print(sorted_num)
##
num = [1, 5, 3, 7, 2]
print(max(num))
print(min(num))
print(sum(num))
##index
courses = ["history", "math", "physics", "compsci"]
print(courses.index("compsci"))
##boolean
courses = ["history", "math", "physics", "compsci"]
print("art" in courses)  # gives false since art is not in list
print("math" in courses)  # gives true since math is in the list
##
courses = ["history", "math", "physics", "compsci"]

for course in courses:
    print(course)
##
courses = ["history", "math", "physics", "compsci"]
for course in enumerate(courses):
    print(course)  # gives both index and corse
    ##
courses = ["history", "math", "physics", "compsci"]
for index, course in enumerate(courses, start=1):
    print(index, course)  # gives both index and course index counting from 1
##
courses = ["history", "math", "physics", "compsci"]
course_str = "-".join(courses)
new_list = course_str.split("-")
print(course_str)  # history-math-physics-compsci
print(new_list)  # ['history', 'math', 'physics', 'compsci']
