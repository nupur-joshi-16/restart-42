# Logical Operator and, or, not


user_height = int(input("Please enter your heaight in centimeters: "))


if user_height > 120:
	print(f"Your height is: {user_height}, yes you can ride")
	user_age = int(input("Please enter your age: "))
	if user_age < 12:
		print(f"Your age is: {user_age}, your ticket amount is: $5")
	elif user_age >= 12 and user_age< 18:
		print(f"Your age is: {user_age}, your ticket amount is : $7")
	elif user_age >= 18 and user_age < 45:
		print(f"Your age is: {user_age}, your ticket amount is : $12")
	elif user_age >= 45 and user_age <= 55:
		print(f"Your age is: {user_age}, your ticket is free")
	elif user_age > 55:
		print(f"Your age is: {user_age}, sorry, you are not allowed")
	else:
		print("Please enter valid age.")
else:
	print(f"Your height is: {user_height}, Sorry, you cannot ride")


 