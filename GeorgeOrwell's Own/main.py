class Animal:
    def __init__(self, name, age, species, diet, habitat):
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet
        self.habitat = habitat

    def make_sound(self):
        print("I am animal")

    def eat(self):
        print(f"{self.name} likes to eat {self.diet}")

    def sleep(self):
        print(f"{self.name} sleeps in the {self.habitat} ")

class Mammal(Animal):
    def __init__(self, name, age, species, diet, habitat, fur, legs):
        super().__init__(name, age, species, diet, habitat)
        self.fur = fur
        self.legs = legs

    def give_birth(self):
        print(f"{self.name} gives birth to infants without any shells")

    def make_sound(self):
        print("I'm a mammal grrr")

class Reptile(Animal):
    def __init__(self, name, age, species, diet, habitat, scale, cold_blooded):
        super().__init__(name, age, species, diet, habitat)
        self.scale = scale
        self.cold_blooded = cold_blooded

    def lay_eggs(self):
        print(f"{self.name} lays soft-shelled eggs")

    def make_sound(self):
        print("I'm a reptile ssss")

class Bird(Animal):
    def __init__(self, name, age, species, diet, habitat, wingspan, can_fly):
        super().__init__(name, age, species, diet, habitat)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.name} takes to the skies!")
        else:
            print(f"{self.name} is ground-bound")

    def make_sound(self):
        print("I'm a bird ca-caw")

class Fish(Animal):
    def __init__(self, name, age, species, diet, habitat, fin, water):
        super().__init__(name, age, species, diet, habitat)
        self.fin = fin
        self.water = water

    def swim(self):
        print(f"With its {self.fin} fin, it swims through {self.water} water!")

    def make_sound(self):
        print("Ey! I'm swimming 'ere!")

class Zookeeper:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def feed_animal(self, animal):
        animal.eat()

    def clean_habitat(self, animal):
        print(f"Man, that {animal.habitat} was tough to clean")

class Zoo:
    def __init__(self, name, animals = None, zookeepers = None):
        self.name = name
        if animals:
            self.animals = animals
        else:
            self.animals = []

        if zookeepers:
            self.zookeepers = zookeepers
        else:
            self.zookeepers = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_zookeeper(self, zookeep):
        self.zookeepers.append(zookeep)

    def daily_routine(self):

        print(f"--- Daily Routine at {self.name} ---")

        for zookeeper in self.zookeepers:
            for animal in self.animals:

                zookeeper.feed_animal(animal)
                zookeeper.clean_habitat(animal)
                animal.make_sound()
                animal.eat()
                animal.sleep()

                if isinstance(animal, Mammal):
                    animal.give_birth()

                elif isinstance(animal, Reptile):
                    animal.lay_eggs()

                elif isinstance(animal, Bird):
                    animal.fly()

                elif isinstance(animal, Fish):
                    animal.swim()


if __name__ == "__main__":
    # Create some animals
    mammal1 = Mammal("Leo", 5, "Lion", "Meat", "Savanna", "Golden", 4)
    reptile1 = Reptile("Lizzy", 10, "Lizard", "Insects", "Desert", "Scaly", True)
    bird1 = Bird("Polly", 2, "Parrot", "Seeds", "Jungle", 24, True)
    fish1 = Fish("Finny", 1, "Goldfish", "Flakes", "Aquarium", "Flowing", "Freshwater")

    # Create a zookeeper
    zookeeper1 = Zookeeper("Bob", 5)

    # Create a zoo
    zoo1 = Zoo("My Zoo")
    zoo1.add_animal(mammal1)
    zoo1.add_animal(reptile1)
    zoo1.add_animal(bird1)
    zoo1.add_animal(fish1)
    zoo1.add_zookeeper(zookeeper1)

    # Simulate a day at the zoo
    zoo1.daily_routine()