class Dog:
    """One of the objects to be returned"""
    
    def speak(self):
        return 'Woof!'
    
    def __str__(self):
        return 'Dog'
    
class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Return a Dog object"""
        return Dog()
    
    def get_food(self):
        """Return a DogFood object"""
        return "Dog Food"
    
class PetStore:
    """PetStore houses an instance of our Abstract Factory"""
    
    def __init__(self, pet_factory=None) -> None:
        """_pet_factory is our Abstract Factory which contains an instance of our concrete factory"""
        self._pet_factory = pet_factory
    
    def show_pet(self):
        """Utility method to display details of the object return by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print(f'Our pet is {pet}')
        print(f'Our pet says hello by {pet.speak()}')
        print(f'It eats {pet_food}')
        
# Create a concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show details of our pet:
shop.show_pet()