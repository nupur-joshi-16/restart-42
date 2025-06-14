# Figure out how to pick a random name from the list of

# As per suggested by Angela

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First solution
print(random.choice(friends))

# Second solution
random_index = random.randint(0,4)
print(friends[random_index])