from random import randint

twos = 0
threes = 0
fours = 0
fives = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

print("""Welcome to the dice rolling simulator.
      Get ready to roll dem bones! 
      How many rolls should we simulate? """)

simulations = int(input())

for roll in range(simulations):
    die1 = randint(1,6)
    die2 = randint(1,6)
    total = die1 + die2
    
    if total == 2:
        twos += 1
    elif total == 3:
        threes += 1    
    elif total == 4:
        fours += 1
    elif total == 5:
        fives += 1
    elif total == 6:
        six += 1
    elif total == 7:
        seven += 1
    elif total == 8:
        eight += 1
    elif total == 9:
        nine += 1    
    elif total == 10:
        ten += 1    
    elif total == 11:
        eleven += 1    
    elif total == 12:
        twelve += 1    
        
print("Simulation Outcome")
print("-" * 30)

print(f"{'Twos:':12}{'|' * twos}")        
print(f"{'Threes:':12}{'|' * threes}")
print(f"{'Fours:':12}{'|' * fours}")
print(f"{'Fives:':12}{'|' * fives}")
print(f"{'Sixes:':12}{'|' * six}")
print(f"{'Sevens:':12}{'|' * seven}")
print(f"{'Eights:':12}{'|' * eight}")
print(f"{'Nines:':12}{'|' * nine}")
print(f"{'Tens:':12}{'|' * ten}")
print(f"{'Elevens:':12}{'|' * eleven}")
print(f"{'Twelves:':12}{'|' * twelve}")
        
        
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
