class House(object):
    def accept(self, visitor):
        ''' The interface to accept a visitor '''
        # Triggers the visiting operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, 'worked on by', hvac_specialist) 
        # This creates a reference to the HVAC specialist within the house object. 
        
    def work_on_electricity(self, electrician):
        print(self, 'worked on by', electrician)
        
    def __str__(self) -> str:
        return self.__class__.__name__
    
class Visitor(object):
    ''' Abstract Visitor '''
    def __str__(self) -> str:
        '''Simply returns the class name when visitor object is printed'''
        return self.__class__.__name__
    
class HVACSpecialist(Visitor):
    # Concrete class fro HVACSpecialist
    def visit(self, house):
        house.work_on_hvac(self)
        # now the visitor has a reference to the house object
        
class Electrician(Visitor):
    '''Concrete visitor: electrician'''
    def visit(self, house):
        house.work_on_electricity(self)
        
hvac1 = HVACSpecialist()
elec1 = Electrician()

h1 = House()

# House accepting visitors
h1.accept(hvac1)
h1.accept(elec1)

# The visitors visiting the house. 
hvac1.visit(h1)
elec1.visit(h1)