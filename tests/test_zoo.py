import unittest
from unittest import TestCase
from src.zoo import Animal, Fence, Zoo, ZooKeeper

class TestZoo(TestCase):
# inizializza dei valori della quale abbiamo necessità in ogni funzione
    """
    def setUp(self) -> None:
        self.zoo_1: Zoo = Zoo()
        self.zookeper_1: ZooKeeper = ZooKeeper(name="Giovanni", surname="Perrella", id=1)
        self.fence_1 : Fence = Fence(area=100, temperature= 25.0, habitat="savana")
        self.animal : Animal = Animal(name="pippo", species="canide", age=5, height=50.0, width=1, preferred_habitat="savana")
"""

    def test_animal_dimension(self):
        """
Questo test controlla che animali troppo grandi non vengano aggiunti alla fence
"""
        zookeeper_1: ZooKeeper= ZooKeeper(name="Giovanni", surname="Perrella", id=1)
        fence_1 : Fence = Fence(area=100, temperature=25.0, habitat="savana")
        animal_1: Animal = Animal(name="pippo", species="canide", age=5, height=50.0, width=1, preferred_habitat="mediterrano")
        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message : str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"

        self.assertEqual(result, 0, message)

    def test_animal_habitat(self):
        zookeeper_1: ZooKeeper= ZooKeeper(name="Giovanni", surname="Perrella", id=1)
        fence_1 : Fence = Fence(area=100, temperature=25.0, habitat="savana")
        animal_1: Animal = Animal(name="pippo", species="canide", age=5, height=50.0, width=1, preferred_habitat="mediterrano")
        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message : str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"

        self.assertEqual(result,0,message)

    def test_feed_animal(self):
        zookeeper_1: ZooKeeper= ZooKeeper(name="Giovanni", surname="Perrella", id=1)
        fence_1 : Fence = Fence(area=100, temperature=25.0, habitat="savana")
        animal_1: Animal = Animal(name="pippo", species="canide", age=5, height=50.0, width=1, preferred_habitat="mediterrano")
        zookeeper_1.feed(animal_1, fence_1)
        result: int = (animal_1.health)
        message : str = f"Error: the function feed is not working"

        self.assertEqual(result,animal_1,message)

        
