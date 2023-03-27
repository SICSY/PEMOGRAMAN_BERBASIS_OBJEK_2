class gameobject:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class drawble:
    def draw(self):
        print('drawing object at :', self.x , self.y)

class movable:
    def move (self,dx,dy):
        self.x += dx
        self.y += dy

class Player(gameobject,drawble,movable):
    def __init__(self,x,y):
        super().__init__(x,y)
    def update(self):
        self.move(1,1)
        self.draw()
    
