# Nested if/else

user_height = int(input("Please enter your heaight in centimeters: "))


if user_height > 120:
	print(f"Your height is: {user_height}, yes you can ride")
	user_age = int(input("Please enter your age: "))
	if user_age <= 18:
		print(f"Your age is: {user_age}, your ticket amount is: $7")
	else:
		print(f"Your age is: {user_age}, your ticket amount is : $12")
else:
	print(f"Your height is: {user_height}, Sorry, you cannot ride")

