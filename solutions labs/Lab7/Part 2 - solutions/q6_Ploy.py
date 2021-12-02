class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def info(self):
        print(f"I am a cat. My name is {self.name}. My color is {self.color}")
    def make_sound(self):
        print("Cat_sound")
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def info(self):
        print(f"I am a dog. My name is {self.name}. My color is {self.color}")
    def make_sound(self):
        print("Dog_sound")

cat1 = Cat("Kitty", "black")
dog1 = Dog("Fluffy", "white")

# Write common interface function using Polymorphism concept to excute make_sound method in both classes 

def test_sound (test):
	test.make_sound()

test_sound(cat1)

test_sound(dog1)