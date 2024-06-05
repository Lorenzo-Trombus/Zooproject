"""
class Animal:
    def __init__(self,name:str,species:str,age:int, height:float, width:float, preferred_habitat:str, health:float ):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.health=round(100 * (1 / age), 3)
        self.area_animal=height*width
        self.incremento_area= self.area_animal*0.02
        self.incremento_salute=self.health*0.01
    
    


class Fence:
    def __init__(self,area:float,temperature:float,habitat:str):
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.area_occupata=0
        self.area_rimanente= self.area - self.area_occupata
        self.animals=[]

    


class ZooKeeper:
    def __init__(self,name: str, surname:str, id:int ):
        self.name=name
        self.surname=surname
        self.id=id
    
    def add_animal(self,animal:Animal,fence:Fence):
        if fence.area_rimanente>=animal.area_animal and  animal.preferred_habitat==fence.habitat:
            fence.animals.append(animal.name)
            fence.area_occupata += animal.area_animal
        
        else:
            return f"l'animale non puo essere aggiunto al recinto perchè troppo grande"


    def remove_animal(self,animal: Animal, fence: Fence):
        if animal.name in fence.animals:
            fence.animals.remove(animal.name)
            fence.area_occupata -= animal.area_animal
        else:
            return f"l'animale da rimuovere non è presente nel recinto"   

    def feed(self,animal: Animal,fence:Fence=None):
        if fence.area_rimanente>=animal.incremento_area:
            animal.area_animal+=animal.incremento_area
            animal.health+=animal.incremento_salute
        else:
            return f"l'animale non puo' essere nutrito perchè troppo grasso"

    def clean(self,fence: Fence):
        if fence.area_rimanente != 0:
            return fence.area_occupata/fence.area_rimanente
        else:
            return fence.area_occupata
        
        
        
class Zoo:
    def __init__(self):
        pass
    def describe_zoo(self,zookeeper:ZooKeeper,fence:Fence,animal:Animal):
        print(f" Guardians:\n {zookeeper.__class__.__name__}(name={zookeeper.name}, surname={zookeeper.surname},id={zookeeper.id}) \n"
            f"Fences:\n {self.__class__.__name__}(area={fence.area}, temperature={fence.temperature},habitat={fence.habitat})\n"
            f"with animals:\n {animal.__class__.__name__}(name={animal.name},species={animal.species}, age={animal.age} ")
        """


#SOLUZIONE ZOO

class Animal:
    
    def __init__(self, name: str, species: str, age: float, height: float, width:float, preferred_habitat:str) -> None:
        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = min(round(100 * (1/self.age), 3), 100)
        self.fence: Fence = None
        
    def area(self):
        return self.height * self.width
    
    def become_bigger(self, factor: float = 0.02) -> tuple[float, float]:
        height = self.height + self.height * factor
        width = self.width + self.width * factor
        return height, width
        
    def become_healthier(self, factor: float = 0.01):
        self.health = min(self.health + self.health * factor, 100)
        
    def __str__(self) -> str:
        return f'Animal(name={self.name}, species={self.species}, age={self.age}, height={round(self.height,3)}'\
            + f', width={round(self.width,3)}, habitat={self.preferred_habitat})'
    
class Fence:
    
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []
        
    def same_habitat(self, animal: Animal) -> bool:
        return animal.preferred_habitat.lower() == self.habitat.lower()
    
    def enough_space(self, animal_area: float) -> bool:
        return animal_area <= self.area
    
    def update_area(self, new_animal_area: float, old_animal_area: float):
        self.area += old_animal_area
        self.area -= new_animal_area
        
    def add_animal(self, animal: Animal):
        animal_area: float = animal.area()
        if self.same_habitat(animal) and self.enough_space(animal_area)\
            and animal not in self.animals:
            self.animals.append(animal)
            # elimino lo spazio del recinto che l'animale occupa
            self.area -= animal_area
            animal.fence = self
            
    def remove_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
            animal_area: float = animal.area()
            # ripristino l'area occupata dall'animale
            self.area += animal_area
            animal.fence = None
            
    def feed(self, animal: Animal):
        new_height, new_width = animal.become_bigger()
        if self.enough_space((new_height * new_width) - animal.area()):
            # ripristina l'area vecchia occupata dall'animale
            self.area += animal.area()
            # faccio diventare l'animale più grande
            animal.height = new_height
            animal.width = new_width
            # levare al recinto l'area dell'animale più grande
            self.area -= animal.area()
            # incrementa la salute dell'animale
            animal.become_healthier()  
            
    def __str__(self) -> str:
        s: str = f"Fence(area={round(self.area,3)}, temperature={self.temperature}, habitat={self.habitat})"
        s += "\nWith Animals:\n"
        for animal in self.animals:
            s += animal.__str__() + "\n"
        return s[:-1]

class ZooKeeper:
    
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
        
    def add_animal(self, animal: Animal, fence: Fence):
        fence.add_animal(animal)
        
    def remove_animal(self, animal: Animal, fence: Fence):
        fence.remove_animal(animal)
                
    def feed(self, animal: Animal):
        fence: Fence = animal.fence
        if fence:
            fence.feed(animal)
            
    def clean(self, fence: Fence) -> float:
        occupied_area: float = 0
        for animal in fence.animals:
            occupied_area += animal.area()
            
        if fence.area == 0:
            return occupied_area
        else:
            return occupied_area / fence.area
                
    def clean_all(self, zoo) -> float:
        cleaning_time = 0
        for fence in zoo.fences:
            cleaning_time += self.clean(fence)
        return cleaning_time
            
            
    def __str__(self) -> str:
        return f'ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})'
    
class Zoo:
    
    
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]):
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers
        
    def describe_zoo(self):
        print("Guardians:")
        for zoo_keeper in self.zoo_keepers:
            print(zoo_keeper)
        print("Fences:")
        for fence in self.fences:
            print(fence)
            print("#" * 30)
    
    
    
simba = Animal(name="Simba", species="Leone", age=5, height=2, width=3, preferred_habitat="Savana")
simba1 = Animal(name="Simba", species="Leone", age=5, height=2, width=2, preferred_habitat="Giungla")

savana = Fence(area=100, temperature=27, habitat="Savana")
zoo_keeper = ZooKeeper(name="Bardh", surname="Prenkaj", id="PRNBDH95M09Z160W")

print(f"L'area del fence Savana è {savana.area}")
zoo = Zoo(fences=[savana], zoo_keepers=[zoo_keeper])
zoo_keeper.add_animal(simba, savana)
zoo_keeper.add_animal(simba1, savana)
print(f"L'area del fence Savana è {savana.area}")
old_area = 0
for i in range(1000):
    zoo_keeper.feed(simba)
    if old_area == round(simba.area(), 3):
        break
    print(f"It={i+1} --> L'area residua del recinto è {round(simba.fence.area, 3)}")
    print(f"It={i+1} --> Simba è diventato grande = {round(simba.area(), 3)}")
    old_area = round(simba.area(), 3)
    
pumba = Animal(name="Pumba", species="Porco", age=25, height=2, width=5, preferred_habitat="Savana")