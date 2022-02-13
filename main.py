'''
inheritance 
'''
from animal import Dog, Cat

maxis= Dog(name='maxis', age=3)
baxter = Cat(name='baxter', age=25)

print(maxis.speak())
print(baxter.speak())

'''
Multiple inheritance 
'''
from app import Resident

resident = Resident(name='Tank', age=23 , id=67)
resident.print_name()
resident.print_age()
resident.print_id()

resident.title()   # Method resolution order - defaults to first title def print
print(resident.title()) # ''

print(Resident.__mro__) # Method Resolution order-  shows order in which things are called
print(Resident.mro()) # same thing without dunder
print('Resident gets called first')