class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        return f"{self.name} says hello!"
    
    def __str__(self):
        return f"Person: {self.name}"
    
person = Person("Bob")
print(person.talk())
print(person)


    
