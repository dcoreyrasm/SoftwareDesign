#sample menu

#clear screen
import os
os.system('clear')

print("Welcome to my program!\n\n\n")

def print_menu():
   print("\n\n\n1. Option 1\n")
   print("2. Option 2\n")
   print("3. Option 3\n")
   print("4. EXIT\n\n\n\n")
    
user_selection = True
while user_selection:
  print_menu()
  user_selection=raw_input("Please select an option>>>")
  if user_selection =="1":
      import nameinput
  elif user_selection =="2":
      import numbers
  elif user_selection =="3":
      import raining
  elif user_selection =="4":
      user_selection = False
  elif user_selection !="":
      print("\nSorry! That is not a valid selection!")
