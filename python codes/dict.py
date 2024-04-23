##Dictionary or dict can contain anything integers,strings,lists
student = {
    "name": "dheeraj",
    "age": 23,
    "courses": ["math", "physics"],
}  #'name','age' are keys they can be string or integer
print(student)
print(student["name"])
print(student.get("name"))  # it works same as above
print(student.get("phone"))  # since phone key doesnt exist it gives none
print(student.get("phone", "Not Found"))  # it gives not found instead of None
##updating dict
student["phone"] = "7995311865"
student["name"] = "jane"
print(student)  # it adds phone and updates name to dict
student.update({"name": "sam", "age": 25, "phone": "741258963"})
print(student)

# Delete
del student["age"]
print(student)

# pop
student.update({"name": "sam", "age": 25, "phone": "741258963"})
age = student.pop("age")
print(student)
print(age)

# length
student = {"name": "dheeraj", "age": 23, "courses": ["math", "physics"]}
print(len(student))  # gives no.of keys in dict
print(student.keys())  # gives keys in dict i.e name age courses
print(student.values())  # gives values in dict i.e dheeraj,23 etc
print(
    student.items()
)  # dict_items([('name', 'dheeraj'), ('age', 23), ('courses', ['math', 'physics'])])

for key in student:
    print(key)
for key, value in student.items():
    print(key, value)
