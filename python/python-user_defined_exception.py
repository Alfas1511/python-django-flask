class VotersEligibility(Exception):
    def __init__(self):
        super()
        
try:
    age = int(input("Enter age: "))
    if age<18:
        raise VotersEligibility
    else:
        print("Voting allowed")
    
except VotersEligibility:
    print("Voting not allowed, age restriction is 18")
    
except ValueError:
    print("Enter number value")
    
finally:
    print("Voting eligibility checked")