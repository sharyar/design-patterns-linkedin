class Subject(object):
    '''Represents the observed'''
    def __init__(self) -> None:
        super().__init__()
        self._observers = []
        
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
        
    def notify(self, modifier=None):
        for observer in self._observers:
            # Only notify an observer if it isnt the one updating the subject. 
            if modifier != observer:
                observer.update()
                
class Core(Subject):
    
    def __init__(self, name = '') -> None:
        super().__init__()
        self._name = name
        self._temp = 0
        
    @property #Getter that gets the core temp
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, temp):
        self._temp = temp
        # Notify the observer whenever somebody cahnges the core temparature
        self.notify()
    
class TempViewer:
    
    def update(self, subject):
        print('Temperature Viewer: {} has tempareture {}'.format(subject._name, subject._temp))
        
# Create subjects
c1 = Core('Core 1')
c2 = Core('Core 2')

# Create observers
v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c2.attach(v2)

c1.temp = 80
c1.temp = 90