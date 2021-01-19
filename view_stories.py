##### Standard funcations section #####
def blank(): #Adds a blank line
  print("")

def clear(): #Clears the screen
  print("\n"*99)


import os
looping = True
while looping == True:
  list_files = os.listdir("./stories")
  print("Here is a list of your stories: ")
  count = 0
  for i in list_files:
      count = count + 1
      number = str(count)
      print(number + ") " + i)
  count = count + 1
  number = str(count)
  print(number + ") Return to the main menu")
  answer = int(input("To select a file, enter its number from the list above: "))
  if answer < len(list_files) + 1:
    position = answer - 1
    file_title = list_files[position]
    file_path = os.path.join("./stories", file_title)
    story_file = open(file_path,"r")
    content = story_file.readlines()
    for line in content:
      print(line)
    story_file.close
    input("Press ENTER to return to the main menu: ")
    looping = False
  elif answer == count:
    looping = False
  else:
    print("The file you requested doesn't exist")
    print(" please make sure you are entering a number between 1 and " + str(len(list_files)+1))
    clear()