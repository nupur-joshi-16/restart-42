print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_other = 3
extra_cheese_price = 1


if size == "S":
	if pepperoni == "Y" and extra_cheese == "Y":
		print(f"Your final bill is: {small_pizza + pepperoni_small + extra_cheese_price}.")
	elif pepperoni == "Y" and extra_cheese == "N":
		print(f"Your final bill is: {small_pizza + pepperoni_small}.")
	elif pepperoni == "N" and extra_cheese == "Y":
		print(f"Your final bill is: {small_pizza + extra_cheese_price}.")	
	else:
		print(f"Your final bill is: {small_pizza}.")

elif size == "M":
	if pepperoni == "Y" and extra_cheese == "Y":
		print(f"Your final bill is: {medium_pizza + pepperoni_other + extra_cheese_price}.")
	elif pepperoni == "Y" and extra_cheese == "N":
		print(f"Your final bill is: {medium_pizza + pepperoni_other}.")
	elif pepperoni == "N" and extra_cheese == "Y":
		print(f"Your final bill is: {medium_pizza + extra_cheese_price}.")
	else:
		print(f"Your final bill is: {medium_pizza}.")

elif size == "L":
	if pepperoni == "Y" and extra_cheese == "Y":
		print(f"Your final bill is: {large_pizza + pepperoni_other + extra_cheese_price}.")
	elif pepperoni == "Y" and extra_cheese == "N":
		print(f"Your final bill is: {large_pizza + pepperoni_other}.")
	elif pepperoni == "N" and extra_cheese == "Y":
		print(f"Your final bill is: {large_pizza + extra_cheese_price}.")	
	else:
		print(f"Your final bill is: {large_pizza}.")
