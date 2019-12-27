# Classical OOP in Python

class PlayerCharacter:
    # Class Object Attribute
    # This is a static attribute which remains true always
    membership = True
    constructor function

    def __init__(self, name, age):
        # access membership using self or PlayerCharacter.membership
    if self.membership:
        self.name = name
        self.age = age

    # Methods
    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print('run run run')
        return 'done'


player1 = PlayerCharacter('Cindy', 24)
player2 = PlayerCharacter('Michael', 39)

# print(player1)
# print(player1.run())

# inspect the class using help()
help(player1)

# help(list)

print(player1.shout())
# ====================================================

# EXERCISE

# Given the below class:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('tom', 3)
cat2 = Cat('bill', 6)
cat3 = Cat('ray', 9)

# 2 Create a function that finds the oldest cat

# Find the oldest cat


def get_oldest_cat(*args):
    print(args)
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")

# ===============================================================

# @classmethod and static methods


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def shout(self):
        print(f'my name is {self.name}')

    # classmethod is the method on the class itself and can be invoked using the classname().

    # The first arg is always the 'cls' which stands for class and using that cls object we can instantiate a new object just like earlier using the class name itself.

    # class method is rarely used but is used when we want to modify the class state i.e the attributes within the constructor function.

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    # static method is different from classmethod only because it doesn't have default arg 'cls' available to it.

    # Static method is used when we don't care about the class state. Class state is what was defined within constructor function
    @staticmethod
    def adding_stuff(num1, num2):
        return num1 + num2


# instantiating a new player1 object using the @classmethod decorator
player1 = PlayerCharacter.adding_things(2, 3)
print(player1.name)
print(player1.age)


# ===========================================================

# classical OOP structure

class NameOfClass:
    class_attribute = 'value'

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
    # code

    @classmethod
    def cls_method(cls, param1, param2):
     # code

    @staticmethod
    def stc_method(param1, param2):
    # code

# =========================================================

# 4 Pillars of OOP

# 1. Encapsulation

# --- Encapsulation is the binding of data and functions which manipulate that data. We encapsulate into one big object which would contain the data (in the form of attributes) and functions (in the form of methods) which can use/modify that data within the object.

# 2. Abstraction

# --- Hiding information or abstracting information and only give access to what is necessary. So, a user sees only what they need to see and the other stuffs remain hidden under the hood.

# --- for e.g: the string or array methods are instantly available on the editors however the user doesn't need to worry about how they're being implemented under the hood.

# --- use private variables to indicate variable shouldn't be reassigned.

# 3. Inheritance

# --- Inheritance allows new objects to take on the property of existing objects so can inherit classes.

# Inheritance Example

# no constructor when our class doesn't have or need attributes.


class User():
    def sign_in(self):
        print('logged in')

# user could have a separate attack method however this gets overridden by the attack methods in subclasses.
    def attack(self):
        print('do nothing...')

# subclass or derived class or children class

# just pass the parent class from which you want to inherit

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # original attack() method of parent class can be called this way.
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows {self.num_arrows}')


wizard1 = Wizard()
# wizard class inherited sign_in method from the parent class.
print(wizard1.sign_in())

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

# Now, the wizard and archer has the same inherited sign_in method. But their attack method is separate for each of them.

# wizard1.attack()

# Check if an object is an instance of another

print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))   # True becoz Wizard is a subclass of User

# object is the base class from where everything comes from.
print(isinstance(wizard1, object))

# 4. Polymorphism (means many forms)

# Ability to redefine methods for derived classes and based on the instantiated object, the methods would act respectively.

# Example

def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

# another example
for char in [wizard1, archer1]:
    char.attack()

# ===============================================================
# ===============================================================

# EXERCISE


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add another Cat
class Minny(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Minny('Minny', 1)]

# help(Simon('Simon', 4))

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

# ====================================

# use of Super()

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing...')


class Wizard(User):
    def __init__(self, name, power, email):
        # first solution
        # User.__init__(self, email)
        # better solution with Super()
        # super doesn't need self. It allows us to refer to User class this way and not have to worry about passing self.
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
# problem
print(wizard1.email)  # wizard object has no atribute email

# Though the wizard1 has access to the parent class and it can be verified by calling sign_in method. When called email, it doesn't work, it gives error since the Wizard has its own constructor function

# ==============================================================

# Introspection

# dir() needs instance as argument and it'll show all the methods associated with that instance
# print(dir(wizard1))

# =============================================================

# Dunder Methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

# ================================================================

# Extend dunder method functionalities

# Task

# 1. Make a custom list so that it returns 1000 when len() function is called on it

# 2. Make the existing list functionalities available to our custom list so that we can use predefined methods like .append() etc on it


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))  # 1000

# use predefined functionalities of parent list
super_list1.append(5)

# make sure list is passed into the SuperList() to make it a subclass of list
print(super_list1[0])  # 5

# check if the SuperList is subclass of list
print(issubclass(SuperList, list))  # True


# ==================================================================

# Multiple Inheritance

# Multiple Inheritance forces us to look into the Method Resolution Order based on which the python traverses through the classes looking for the inherited methods. MRO implements Depth First Search

# Method Resolution Order

http: // www.srikanthtechnologies.com/blog/python/mro.aspx
