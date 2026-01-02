# Multiple Inheritance, Multiple base classes and 1 child class

# class Base1:
#     pass
# class Base2:
#     pass
# class MultiDerived(Base1, Base2):
#     pass

class Base1:
    def functionBase1(self):
        print("class Base1 function 1 is executing")
        
class Base2:
    def functionBase2(self):
        print("class Base2 function 1 is executing")
        
class Base3:
    def functionBase3(self):
        print("class Base3 function 1 is executing")
        
class MultiDerived(Base1, Base2, Base3):
    def functionMultiderived1(self):
        print('class MultiDerived Function1 is executing')
        
md1 = MultiDerived()
md1.functionBase1()
md1.functionBase2()
md1.functionBase3()
md1.functionMultiderived1()