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
        


