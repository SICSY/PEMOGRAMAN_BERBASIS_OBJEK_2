class animal:
    def __init__(self,nama):
        self.nama = nama
    def speak(self):
        print('the animal speaks')

class dog(animal):
    def __init__(self,nama,breed):
        super().__init__(nama)
        self.breed = breed
    def speak(self):
        print('the dog barks')
    
class buldog(dog):
    def __init__(self,nama,breed,origin):
        super().__ini__(nama,breed)
        self.origin = origin
    def speak(self):
        print('the buldog growls')
print(buldog.mro())
print(buldog.__mro__)