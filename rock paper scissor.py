import random

while True:
   user_input = input("enter your choice(rock/paper/scissor) :")
   pass_choice = ["rock","paper","scissor"]
   com_input = random.choice(pass_choice)
   print(f"you choose {user_input} and computer choose {com_input}")


   if user_input == com_input:
      print("it will be tie")
   elif user_input == "rock":
        if com_input == "scissor":
            print("user win")
        else:
            print("user lose")


   elif user_input == "paper":
      if com_input == "rock":
        print("user win")
      else:
         print("user lose")


   elif user_input == "scissor":
      if com_input == "paper":
         print("user win")
      else:
         print("user lose")

   play_again = input("do you want to play again : (yes/no)")
   if play_again.lower() != "yes":
    break
 
print("Game Over")