from abc import ABC, abstractmethod


class AnimalError(Exception):
    pass


class Animal(ABC):
    def __init__(self, name: str, age: int):
        if not name or not isinstance(name, str):
            raise AnimalError("Nama hewan tidak valid.")
        if not isinstance(age, int) or age < 0:
            raise AnimalError("Usia hewan tidak valid. Harap masukkan usia yang benar.")
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        if not value:
            raise AnimalError("Nama hewan tidak boleh kosong.")
        self.__name = value        
    
    @property
    def age(self):
        return self.__age
        
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise AnimalError("Usia hewan tidak valid. Harap masukkan usia yang benar.")
        self.__age = value  
    
    @abstractmethod
    def make_sound(self):
        pass
        
    def __str__(self):
        return f"{self.__class__.__name__} bernama {self.name} berusia {self.age}"

class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp chirp!"

def main():
    animals = []
    
    try:
        dog = Dog("Buddy", 3)
        cat = Cat("Kitty", 2)
        bird = Bird("Tweety", 1)
        animals.extend([dog, cat, bird])
    except AnimalError as e:
        print("Error saat menambahkan hewan:", e)
    
    for animal in animals:
        print(animal)
        print("Sound:", animal.make_sound())
        print("-" * 40)
        
    try:
        invalid_animal = Dog("", -1)
    except AnimalError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
