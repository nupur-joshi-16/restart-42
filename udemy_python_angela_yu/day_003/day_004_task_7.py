print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
user_choice = input('Type "left" or "right" : ')

if user_choice == "left":
   print("You've come to a lake. There is an island in the middle of the lake.")
   user_choice = input('Type "wait" to wait for a boat. Type "swim" to swim across. : ')
   if user_choice == "wait":
      print("You arrive at the island unharmed. There is a house with 3 doors.")
      user_choice = input('One red, one yellow and one blue. Which colour do you choose? : ')
      if user_choice == "red":
         print("Burned by fire. Game Over.")
      elif user_choice == "blue":
         print("Eaten by beasts. Game Over.")
      elif user_choice == "yellow":
         print("You win!")
      else:
         print("Game over")
   elif user_choice == "swim":
      print("Attacked by trout. Game Over")
elif user_choice == "right":
   print("Fall into a hole. Game Over.")
else:
   print("Please choose valid input.")