class myBird:
    def __init__(self):
        print("myBird class constructor is executing")
        
    def type(self):
        print('I am a bird')
    
    def canFly(self):
        print('myBird can fly')
    
    def canSwim(self):
        print('myBird can swim')
        
    
class myParrot:
    species = "bird"
    
    def __init__(self, name, age):
        print("myParrot class constructor is executing")
        self.name = name
        self.age = age
        
    def canSing(self, thisSong):
        print(f"{self.name} can sing {thisSong}")