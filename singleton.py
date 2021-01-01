class Borg:
    """Borg class making class attributes global"""
    _shared_state = {} # Attribute dictionary
    
    def __init__(self):
        self.__dict__ = self._shared_state # Make it an attribute dictionary
        
class Singleton(Borg): #Inherits from the Borg Class
    """This class now shares all its attributes among its various instances"""
    # This essentially makes the singleton object a global variable in OOP
    
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)
        
    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)
    
x = Singleton(HTTP = 'Hyper Text Transfer Protocol')
print(x)
y = Singleton(yellow = 'Color')
print(x == y)