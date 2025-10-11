# Figure out how to pick a random name from the list of

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_num = random.randint(1, 100)

print(rand_num)

if rand_num >= 1 and rand_num <= 20:
   print(friends[0])
elif rand_num > 20 and rand_num <= 40:
   print(friends[1])
elif rand_num > 40 and rand_num <= 60:
   print(friends[2])
elif rand_num > 60 and rand_num <= 80:
   print(friends[3])
elif rand_num > 80 and rand_num <= 100:
   print(friends[4])
else:
   print("Something went wrong")
