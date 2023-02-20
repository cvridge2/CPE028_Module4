class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__ (self):
        return f"{self.name}({self.age})"

person1 = Student("Christian Vridge Labado", 16)
person2 = Student("Jebron Lames", 101)

print(person1)
print(person2)

print("Name: ", person1.name)
print("Age: ", person1.age)
print("Name: ", person2.name)
print("Age: ", person2.age)