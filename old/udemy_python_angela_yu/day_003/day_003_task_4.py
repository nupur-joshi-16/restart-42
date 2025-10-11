weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
	print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
	print("normal weight")
elif bmi >= 25:
	print("overweight")
else:
	print("Something went wrong")
