class myBird:
    def __init__(self):
        print('myBird class constructor in executing')
        
    def whatType(self):
        print("I am a bird")
        
    def canSwim(self):
        print("I can Swim")
        
class penguin(myBird): # penguin class inherits parent class myBird
    def __init__(self):
        super().__init__()
        print('penguin class constructor in executing')
        
    def whoIsThis(self):
        print("I am penguin")
    
    def canRun(self):
        print('I can run faster')
        
pg1 = penguin()
pg1.whatType() # Parent/Base class
pg1.whoIsThis()
pg1.canRun()
pg1.canSwim() # Parent/Base class
