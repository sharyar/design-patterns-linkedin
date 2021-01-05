class DrawingAPIOne(object):
    '''Implementation specific abstraction: concrete class one'''
    def draw_circle(self, x, y, radius):
        print(f'API 1 Drawing a circle at {x}, {y} with radius {radius}')

class DrawingAPITwo(object):
    '''Implementation specific abstract: concrete class two'''
    def draw_circle(self, x, y, radius):
        print(f'API 2 Drawing a circle at {x}, {y} with radius {radius}')

class Circle(object):
    '''implementation independent abstraction: for example, a rectangle class'''
    
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api
        
    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)
        
    def scale(self, percent):
        self.radius *= percent
        
circle1 = Circle(1,2,3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(1, 2, 3, DrawingAPITwo())
circle2.draw()