'''
Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.
'''

import random

random_number = random.random() * 10

if random_number >=0 and random_number < 5:
   print("Heads")
else:
   print("Tails")