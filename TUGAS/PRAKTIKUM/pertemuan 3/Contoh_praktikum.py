class animal :
    def makesound(self):
        print('the animal make a sound')
class dog (animal):
    def makesound(self):
        print('the dog barks')
class cat(animal):
    def makesound(self):
        print('the cat meows')
def animalsound(animal):
    animal.makesound()

Animal = animal()
Dog = dog()
Cat = cat()

animalsound(Animal)
animalsound(Dog)
animalsound(Cat)
