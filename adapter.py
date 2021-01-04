class Korean:
    def __init__(self):
        self.name = 'Korean'
        
    def speak_korean(self):
        return 'An-neyong?'
    
class British:
    def __init__(self) -> None:
        self.name = 'Britsh'
        
    def speak_english(self):
        return 'Hello'

class Adapter:
    def __init__(self, object, **adapted_method):
        self._object = object
        
        # Adds a new dict item that establishes the mapping between the generic method name: speak() and the concrete method
        # for example, speak() will be translated to speak_korean() if the mapping says so. 
        self.__dict__.update(adapted_method)
        
    def __getattr__(self, attr):
        return getattr(self._object, attr)
    
# list to store speaker objects
objects = []

korean = Korean()
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print('{} says {}\n'.format(obj.name, obj.speak()))