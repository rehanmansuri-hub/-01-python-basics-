marks = {
    "john": 85,
    "jane": 92,
    "bob": 78,
    0: "zero"
}
# print(marks.items()) 
# print(marks.keys())  
# print(marks.values())
# marks.update({"jane": 95, "renuka": 88})  # Updating an existing key
# print(marks)

print(marks.get("jane2")) # prints None
print(marks.get("jane2", "Key not found")) # prints "Key not found"


# some example in chat gpt

student = {
    "name": "Rehan",
    "age": 20,
    "course": "BA"
}

print(student.keys())          # Saari keys
print(student.values())        # Saari values
print(student.items())         # Key + Value
print(student.get("name"))     # Value lena

student.update({"city": "Indore"})  # Data add/change

student.pop("age")             # Specific key delete
student.popitem()              # Last item delete

student.setdefault("city", "Indore") # Key nahi hai to add

student2 = student.copy()      # Dictionary ki copy

student.clear()                # Puri dictionary empty