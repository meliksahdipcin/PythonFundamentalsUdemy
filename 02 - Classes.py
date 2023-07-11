#CLASSES
class Dog():
    
    #Class object attribute
    #Same for any instance of a class
    species = "Animal"

    def __init__(self,my_breed,name,spots):
        
        #Attributes
        #Take the argument
        #Assign using self.attribute_name
        self.my_attribute = my_breed
        self.name = name
        
        #Boolean
        self.spots = spots

    #Operations/Actions --> Methods
    def bark(self,number):
        print("Woof! My name is {} and the number is {}".format(self.name,number))

my_dog = Dog(my_breed="Lab",name="Sammy",spots=True)
my_dog = Dog("Lab","Sammy",True)

print(my_dog.my_attribute)

print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)

print(type(my_dog))

my_dog.bark(10)


class Circle():

    #Class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    #Method
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30) #override the radius
print(my_circle.radius)
print(my_circle.pi)

#INHERITANCE
class Animal():

    def __init__(self):
        print("Animal created.")

    def who_am_i(self):
        print("I am an animal.")

    def eat(self):
        print("I am eating.")

my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog.")

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

#POLYMORPHISM
class Dog():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " sayf woof!"
    
class Cat():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow!"
    
niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())
    
pet_speak(niko)
pet_speak(felix)

#SPECIAL METHODS
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self): #special functions that returns string from a class
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book subject has been deleted.")
        
b = Book("Python rocks","Jose",300)
print(b)
str(b)
len(b)

del b #deletes the item from the class



































