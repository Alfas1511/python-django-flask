## Polymorphism

class myParrot:
    def canFly(self):
        print("Parrot can fly")
    
    def canSwim(self):
        print('Parrot can not swim')
        
class myPenguin():
    def canFly(self):
        print("Penguin can not fly")
    
    def canSwim(self):
        print('Penguin can swim')
        
        
# common interface
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwim()
    
bird_parrot = myParrot()
bird_penguin = myPenguin()

flying_bird_test(bird_parrot)
print()
flying_bird_test(bird_penguin)