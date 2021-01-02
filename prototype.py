import copy

class Prototype:
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
        
    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        
        # update the attributes of the object cloned. 
        obj.__dict__.update(attr)
        return obj
        
        
class Car:
    def __init__(self) -> None:
        super().__init__()
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self) -> str:
        return f'{self.name} | {self.color} | {self.options}'
    
c = Car()
protoype = Prototype()
protoype.register_object('Skylark', c)

clone1 = protoype.clone('Skylark')
print(clone1)

clone2 = protoype.clone('Skylark', **{'color':'steel'})
print(clone2)