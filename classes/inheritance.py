class Animal:
    def walk(self):
        return "The animal is walking."

class Dog(Animal):
    def bark(self):
        return "Woof!"

    
class Cat(Animal):
    def meow(self):
        return "Meow!"

cat = Cat()
cat.meow()
print(cat.walk())

