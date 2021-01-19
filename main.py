"""
This is the main menu for the program
"""
##### Standard funcations section #####
def blank(): #Adds a blank line
  print("")

def clear(): #Clears the screen
  print("\n"*99)

##### Menu #####
clear()
exit = False
while exit == False:
  print("Story box generator main menu")
  blank()
  print("1) Manual generator")
  print("2) Automatic generator (Currently unavalible")
  print("3) View your previously made stories")
  print("4) To exit the story box")
  blank()
  answer = input("Please select an option from the list above: ")
  if answer == "1":
    import story_manual #Just loads manual generation as no other option is avalible
  if answer == "2":
    clear()
    import story_auto
    clear
  elif answer == "3":
    clear()
    import view_stories
    clear()
  elif answer == "4":
    clear()
    exit = True
  else:
    clear()
    print("That wasn't a valid option, please try again")
    clear()