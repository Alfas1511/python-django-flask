class myBird:
    def __init__(self):
        print("myBird class constructor is executing")
        
    def whatType(self):
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
        
class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print("myPenguin is ready")
        
    def whoIsThis(self):
        print("I am Penguin")
        
    def canRun(self):
        print("Penguin can run faster")
        
mp1 = myParrot("MyParrot1", 10)
mp2 = myParrot("MyParrot2", 15)

# accessing class attributes
print(f"mp1 is a {mp1.__class__.species}")
print(f"mp2 is a {mp1.__class__.species}")

# accessing instance attributes
print(f"{mp1.name} is {mp1.age} years old")
print(f"{mp2.name} is {mp2.age} years old")
print(mp1.canSing("Chirp"))

pg1 = myPenguin()
pg1.whoIsThis()
pg1.canSwim()
pg1.canRun()
        