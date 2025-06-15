from random import randint 

class Die:
    # class representing a single die 
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        # return a random value betweeen 1 and number of sides 
        return randint(1, self.num_sides)
    

dice = Die()
results = []
for x in range(100):
    result= dice.roll()
    results.append(result) # this result variable is every time getting stored in results through appends 

print(result)

frequencies = []

for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#print(frequencies)

    


