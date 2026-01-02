def findMax(a, b):
    if a>b:print(a, 'is greater') 
    else:print(b, 'is greater')
    
findMax(12, 100)


def findMin(a, b):
    if a<b:return a
    else: return b
    
print(findMin(123, 14) ,"is smaller")


def greeting(name, msg = "how are you"):
    print("Hello", name, msg)
    
greeting("Alfas", "good evening")
greeting("Ansal")



def sumOfNumbers(*args):
    sum = 0
    for i in args:
        sum = sum + i
        
    return sum

print(sumOfNumbers(2,4,6,10))


def defaultArgs(a = 50, b = 20, c = 100):
    print('a = {}, b = {}, c = {}'.format(a,b,c))
    
defaultArgs(b=2, c =5, a = 100)