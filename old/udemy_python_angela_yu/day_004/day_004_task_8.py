# Rock, Paper, Scissors game

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
computer_choice = random.randint(0,2)

if user_choice == 0 and computer_choice == 0:
   print(f"User choice \t: Rock\nComputer choice : Rock")
   print("User and computer both choose the same shape. Match Draw.")
elif user_choice == 0 and computer_choice == 1:
   print(f"User choice \t: Rock\nComputer choice : Paper")
   print("Paper covers rock. Computer win.")
elif user_choice == 0 and computer_choice == 2:
   print(f"User choice \t: Rock\nComputer choice : Scissors")
   print("Rock crushes scissors. User win.")
elif user_choice == 1 and computer_choice == 0:
   print(f"User choice \t: Paper\nComputer choice : Rock.")
   print("Paper covers rock. User win.")
elif user_choice == 1 and computer_choice == 1:
   print(f"User choice :\t Paper\nComputer choice : Paper")
   print("User and computer both choose the same shape. Match Draw.")
elif user_choice == 1 and computer_choice == 2:
   print(f"User choice :\t Paper\nComputer choice : Scissors.")
   print("Scissors cuts paper. Computer win.")
elif user_choice == 2 and computer_choice == 0:
   print(f"User choice :\t Scissors\nComputer choice : Rock.")
   print("Rock crushes scissors. Computer win.")
elif user_choice == 2 and computer_choice == 1:
   print(f"User choice :\t Scissors\nComputer choice : Paper.")
   print("Scissors cuts paper. User win.")
elif user_choice == 2 and computer_choice == 2:
  print(f"User choice :\t Scissors\nComputer choice :\t Scissors")
  print("User and computer both choose the same shape. Match Draw.")
else:
   print("Something went wrong")