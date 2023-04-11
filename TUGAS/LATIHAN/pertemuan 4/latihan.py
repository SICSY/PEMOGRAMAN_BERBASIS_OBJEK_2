class Pekerja:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
class Perusahaan:
    def __init__(self, nama, pekerja):
        self.nama = nama
        self.pekerja = pekerja
    def daftar_pekerja(self):
        for pekerja in self.pekerja:
            print(pekerja.nama, pekerja.umur)
pekerja1 = Pekerja("Andi", 25)
pekerja2 = Pekerja("Budi", 30)
perusahaan = Perusahaan("ABC", [pekerja1, pekerja2])
perusahaan.daftar_pekerja()

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
class Item:
    def __init__(self, name):
        self.name = name
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
player = Player("John")
sword = Item("Sword")
shield = Item("Shield")
player.inventory.add_item(sword)
player.inventory.add_item(shield)
player.inventory.items

class Menu:
    def __init__(self, dishes=None):
        if dishes is None:      
            self.dishes = []
        else:
            self.dishes = dishes
    def add_dish(self, dish):
        self.dishes.append(dish)
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
dish1 = Dish("Nasi Goreng", 15000)
dish2 = Dish("Mie Goreng", 12000)
menu = Menu([dish1, dish2])
restaurant = Restaurant("Warung Padang", menu)
restaurant.menu.dishes # output: [dish1, dish2]


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
song1 = Song("Lose Yourself", "Eminem")
song2 = Song("Someone Like You", "Adele")
playlist = Playlist()
playlist.add_song(song1)
playlist.add_song(song2)
media_player = MediaPlayer(playlist)
print(media_player.playlist.songs) # output: [song1, song2]

class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
ram = RAM(8)
storage = Storage(500)
computer = Computer(ram, storage)
print(computer.ram.capacity) # output: 8
print(computer.storage.capacity) # output: 500

class Wheel:
    def __init__(self, size):
        self.size = size
class Engine:
    def __init__(self, power):
        self.power = power
class Car:
    def __init__(self, wheels, engine):
        self.wheels = wheels
        self.engine = engine
wheel1 = Wheel(17)
wheel2 = Wheel(17)
wheel3 = Wheel(17)
wheel4 = Wheel(17)
engine = Engine(150)
car = Car([wheel1, wheel2, wheel3, wheel4], engine)
print(car.wheels[0].size) # output: 17