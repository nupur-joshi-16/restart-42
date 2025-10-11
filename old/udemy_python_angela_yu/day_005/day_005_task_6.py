# FizzBuzz

for number in range (1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print(f"{number}\t: FizzBuzz")
  elif number % 3 == 0 and not number % 5 == 0:
    print(f"{number}\t: Fizz")
  elif number % 5 == 0 and not number % 3 == 0:
    print(f"{number}\t: Buzz")
  else:
    print(f"{number}\t: {number}")

