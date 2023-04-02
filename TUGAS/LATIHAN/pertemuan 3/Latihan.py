#contoh 1
print(len('hello'))
print(len([1,2,3]))
print(len((1,2,3)))

#contoh 2
print(2+3) 
print('hello'+ 'world')
print([1,2]+[3,4])

#contoh 3
print(max(2,5))
print(max([1,2,3]))
print(max('hello'))

#contoh 4
a = [ 3,1,2]
a.sort()
print(a)

b = ['c', 'a', 'b']
b.sort()
print(b)


#polymorphism dinamis(overriding)

class matematika:
    def add (self,a,b):
        return a + b
    def add(self,a,b,c=0):
        return a + b + c
mat =  matematika()
b = mat.add(5,3,6)
print(b)

mut = matematika()
c = mut.add(7,3)
print(c)

# implementasi polymorphism pada perilaku objek saat runtime

class shape :
    def area(self):
        pass
class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area (self):
        return self.width * self.height
class circle (shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
shapes = [ rectangle(3,4), circle(5)]
for shape in  shapes:
    print(shape.area)

# implementasi polymorphism dinamis pada pewarisan dan pengikatan dinamis


class animal :
    def make_sound(self):
        print('the animal make a sound')
class dog(animal):
    def make_sound(self):
        print('the dog bark')
class cat(animal):
    def make_sound(self):
        print('the cat  meow')
class chihuahua(dog):
    def make_sound(self):
        print('the cihuahua yaps')
class anggora(cat):
    def make_sound(self):
        print('the siamese purss')
def animal_sound(animal):
    animal.make_sound()


anim = animal()
anjing = dog()
kucing = cat()
Chihuahua = chihuahua()
Anggora = anggora()

animal_sound(anim)
animal_sound(anjing)
animal_sound(kucing)
animal_sound(Chihuahua)
animal_sound(Anggora)

# implementasi polymorphism dinamis pada abstract class
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print('starting car ...')
class bus(vehicle):
    def start(self):
        print('starting motorcycle...')
class motorcycle(vehicle):
    def start(self):
        print('starting motorcycle...')
vehicle = [ car(), motorcycle(), bus()]

for vehicle in vehicle:
    vehicle.start()

# implementasi polymorphismm dinamis dalam duck typing

class kucing:
    def bersuara(self):
        print('meow')
class anjing :
    def bersuara(self):
        print('gug')
def cetak_suara(objek):
    objek.bersuara()
Kucing = kucing()
Anjing = anjing()

cetak_suara(Kucing)
cetak_suara(Anjing)