class Component(object):
    '''Abstract Class'''
    def __init__(self, *args, **kwargs) -> None:
        pass
    
    # Interface function
    def component_function(self):
        pass
    
class Child(Component):
    '''Concrete Class'''
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # We store the name of our child item here. 
        self.name = args[0]
        
    def component_function(self):
        # Print the name of your child item here!
        print(f'{self.name}')
        
class Composite(Component):
    '''Concrete Class and maintains the recursive tree structure'''
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # This is where we store the name of the composite object
        self.name = args[0]
        
        # this is where we keep the child items
        self.children = []
        
    def append_child(self, child):
        self.children.append(child)
        
    def remove_child(self, child):
        self.children.remove(child)
        
    def component_function(self):
        # Print the name of the composite object 
        print(f'{self.name}')
        
        # iterate through all child objects and print their names. 
        for i in self.children:
            i.component_function()
            
# build a composite submenu 1
sub1 = Composite('submenu1')
# child of submenu1
sub11 = Child('sub_submenu 11')
sub12 = Child('sub_submenu 12')
sub1.append_child(sub11)
sub1.append_child(sub12)
top = Composite('top_menu')
sub2 = Child('submenu2')
top.append_child(sub1)
top.append_child(sub2)
top.component_function()