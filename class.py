#class
class Person:
    # class attributes
    address = 'no information'

    
    
    # constructor (yapıcı metod)
    def __init__(self, name, year):

        # object attributes
        self.name = name
        self.year = year

    # instance methods
    def intro(self):
        print('Hello There. I am ' + self.name)
    
    def calculateAge(self):
        return 2019 - self.year

# object (instance)
p1 = Person('ali', 1999)
p2 = Person('yağmur', 1998)

p1.intro()

# accessing object attributes
print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')

# update
# p1.name = 'Ahmet'
# p1.address = 'Kocaeli'



