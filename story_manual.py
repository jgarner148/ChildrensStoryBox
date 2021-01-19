""""
A program that allows the user to generate a story based on options they have picked.
The program is targeted at young children.
The user inputs their name and selects a location for the story to take place. 
They then input the name of their friend who will be coming along with them.
They then pick an activity to do at that location and the program randomly picks what will happen while they are doing that
"""
##### Imports section #####
import time #Imported for better user experience
import random #Imported to generate random numbers so that the story can vary each time
import datetime
import os


##### Standard funcations section #####
def blank(): #Adds a blank line
  print("")

def clear(): #Clears the screen
  print("\n"*99)

######################### CODE BEGINS HERE #########################
#####Funcations#####
def welcome_screen(): #First screen the user is met with when starting the program
  clear()
  print("Welcome to the Story Box story generator manual mode")
  time.sleep(1)
  blank()
  print("Today we can make a short story personal to you!")
  time.sleep(1)
  blank()
  input("Press ENTER to start ")

def find_name(): #Finds the name of the user
  clear()
  print("Hello!")
  time.sleep(1)
  print("Before you can hear the story I need to ask you a few questions...")
  time.sleep(1.5)
  blank()
  print("First question:")
  looping1 = True
  while looping1 == True: #Keeps looping until the user types in a valid name and confirms it is correct
    looping2 = True
    while looping2 == True: #Keeps looping until the user inputs a valid name
      user_name = input("What is your name: ")
      user_name = user_name.capitalize()
      all_alpha= user_name.isalpha()
      clear()
      if all_alpha == False:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you use only letters in your name, no special characters or numbers")
        input("Press ENTER to try again")
        clear()
      else:
        looping2 = False
    looping3 = True
    while looping3 == True: #keeps looping until the user enters either "yes" or "no"
      print("Is", user_name.upper(), "right?")
      correct = input("If it is type YES. If not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping3 = False
        looping1 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        time.sleep(2)
        looping3=False
        clear()
      else:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you are typing either YES or NO")
        input("Press ENTER to try again ")
        clear()
  print("Hello", user_name)
  time.sleep(1)
  input("Press ENTER to move on to Question 2 ")
  return user_name

def find_location(): #Asks to user to pick a location for their story
  clear()
  print("Question Number 2")
  time.sleep(1)
  blank()
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid location that they agree is correct
    looping2 = True
    while looping2 == True: #Loops until the user picks a valid location
      print("Pick one of the following locations for your story to be set in:")
      blank()
      print("1) Beach")
      print("2) Playground")
      print("3) Theme park")
      print("4) Zoo")
      print("5) Mountain")
      print("6) Lake")
      blank()
      location = input("Type the number that links with the location you want: ")
      clear()
      if location == "1":
        location = "beach"
        looping2 = False
      elif location == "2":
        location = "playground"
        looping2 = False
      elif location == "3":
        location = "theme park"
        looping2 = False
      elif location == "4":
        location = "zoo"
        looping2 = False
      elif location == "5":
        location = "mountain"
        looping2 = False
      elif location == "6":
        location = "lake"
        looping2 = False
      else: 
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you only enter the number of the location you'd like")
        input("Press ENTER to continue ")
        clear()
    looping3 = True
    while looping3 == True: #Loops until the user picks 'yes' or 'no'
      print("Is", location.upper(), "Right?")
      correct = input("If yes then type YES or if not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping1 = False
        looping3 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        looping3 = False
        time.sleep(2)
        clear()
      else:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you are typing either YES or NO")
        input("Press ENTER to try again ")
        clear()
  print("The location where your story will take place is at a", location + ".")
  input("Press ENTER to continue to the next question ")
  return location

def find_friend(): #Asks the user to name a friend who will be in the story with them
  clear()
  print("Question 3")
  time.sleep(1)
  blank()
  looping1 = True
  while looping1 == True: #Loops until the user has named a friend and confirmed it's correct
    print("You will need a friend to accompany you during this story")
    time.sleep(1)
    blank()
    looping2 = True
    while looping2 == True: #Loops until the user enters a valid friend name
      friend = input("What is your friends name?: ")
      clear()
      friend = friend.capitalize()
      all_alpha = friend.isalpha()
      if all_alpha == False:
        print("Sorry what you inputted was not valid")
        print("Make sure your friend's name doesn't contain any numbers or special characters")
        input("Press ENTER to try again ")
        clear()
      else:
        looping2 = False
    looping3 = True
    clear()
    while looping3 == True: #Loops until the user confirms if they have entered the correct name
      print("Is", friend.upper(), "correct?")
      correct = input("If it is type YES if it isn't type NO: ")
      correct = correct.lower()
      clear()
      if correct == "yes":
        looping3 = False
        looping1 = False
      elif correct == "no":
        print("Okay, lets try again")
        time.sleep(1)
        looping3 = False
        clear()
      else:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you are either entering YES or NO")
        input("Press ENTER to try again")
        clear()
  print("Your friends name is", friend)
  input("Press ENTER to move on to the next question ")
  return friend

def location_beach(): #Ask the user to pick an activity if they chose the beach as their location
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid activity from the options
    print("Pick an option for what activity you would like to do at the beach")
    blank()
    print("1) Build a sandcastle")
    print("2) Go swimming")
    print("3) Sunbathe")
    blank()
    activity1 = input("Pick a number that links with the activity you would like to do: ") #Alows the user to pick from 3 options
    if activity1 == "1":
      activity1 = "build a sandcastle"
      looping1 = False
      clear()
    elif activity1 == "2":
      activity1 = "go swimming"
      looping1 = False
      clear()
    elif activity1 == "3":
      activity1 = "sunbathe"
      looping1 = False
      clear()
    else:
      clear()
      print("Sorry, what you inputted wasn't a valid option")
      print("Make sure you have entered a number between 1 and 3")
      input("press ENTER to try again")
  return activity1

def location_playground(): #Asks the user to pick an activity if they chose the playground as their location
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid activity from the options
    print("Pick an option for what activity you would like to do at the playground")
    blank()
    print("1) Play on the swings")
    print("2) Play on the slides")
    print("3) Play on the see-saw")
    blank()
    activity1 = input("Pick a number that links with the activity you would like to do: ") #Alows the user to pick from 3 options
    if activity1 == "1":
      activity1 = "play on the swings"
      looping1 = False
      clear()
    elif activity1 == "2":
      activity1 = "play on the slides"
      looping1 = False
      clear()
    elif activity1 == "3":
      activity1 = "play on the see-saw"
      looping1 = False
      clear()
    else:
      clear()
      print("Sorry, what you inputted wasn't a valid option")
      print("Make sure you have entered a number between 1 and 3")
      input("press ENTER to try again")
  return activity1

def location_theme_park(): #Asks the user to pick an activity if they chose the theme park as their location
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid activity from the options
    print("Pick an option for what activity you would like to do at the theme park")
    blank()
    print("1) Ride on a big roller coaster")
    print("2) Ride on a smaller roller coaster")
    print("3) Ride on a water ride")
    blank()
    activity1 = input("Pick a number that links with the activity you would like to do: ") #Alows the user to pick from 3 options
    if activity1 == "1":
      activity1 = "ride on a big roller coaster"
      looping1 = False
      clear()
    elif activity1 == "2":
      activity1 = "ride on a smaller roller coaster"
      looping1 = False
      clear()
    elif activity1 == "3":
      activity1 = "ride a water ride"
      looping1 = False
      clear()
    else:
      clear()
      print("Sorry, what you inputted wasn't a valid option")
      print("Make sure you have entered a number between 1 and 3")
      input("press ENTER to try again")
  return activity1

def location_zoo(): #Asks the user to pick an activity if they chose the zoo as their location
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid activity from the options
    print("Pick an option for what activity you would like to do at the zoo")
    blank()
    print("1) See an African animal")
    print("2) See a farm animal")
    print("3) Go to the bug house")
    blank()
    activity1 = input("Pick a number that links with the activity you would like to do: ") #Alows the user to pick from 3 options
    if activity1 == "1":
      activity1 = "see an African animal"
      looping1 = False
      clear()
    elif activity1 == "2":
      activity1 = "see a farm animal"
      looping1 = False
      clear()
    elif activity1 == "3":
      activity1 = "go to the bug house"
      looping1 = False
      clear()
    else:
      clear()
      print("Sorry, what you inputted wasn't a valid option")
      print("Make sure you have entered a number between 1 and 3")
      input("press ENTER to try again")
  return activity1

def location_mountain():#Asks the user to pick an activity if they chose the moutain as their location
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid activity from the options
    print("Pick an option for what activity you would like to do at the mountain")
    blank()
    print("1) Hike up the mountain")
    print("2) Look for animals")
    print("3) Take photographs")
    blank()
    activity1 = input("Pick a number that links with the activity you would like to do: ") #Alows the user to pick from 3 options
    if activity1 == "1":
      activity1 = "go for a hike up the mountain"
      looping1 = False
      clear()
    elif activity1 == "2":
      activity1 = "look for animals"
      looping1 = False
      clear()
    elif activity1 == "3":
      activity1 = "take photographs"
      looping1 = False
      clear()
    else:
      clear()
      print("Sorry, what you inputted wasn't a valid option")
      print("Make sure you have entered a number between 1 and 3")
      input("press ENTER to try again")
  return activity1

def location_lake(): #Asks the user to pick an activty if they chose the lake as their location
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid activity from the options
    print("Pick an option for what activity you would like to do at the lake")
    blank()
    print("1) Rent a boat")
    print("2) Go fishing")
    print("3) go for a swim in the lake")
    blank()
    activity1 = input("Pick a number that links with the activity you would like to do: ") #Alows the user to pick from 3 options
    if activity1 == "1":
      activity1 = "rent a boat"
      looping1 = False
      clear()
    elif activity1 == "2":
      activity1 = "go fishing"
      looping1 = False
      clear()
    elif activity1 == "3":
      activity1 = "go for a swim in the lake"
      looping1 = False
      clear()
    else:
      clear()
      print("Sorry, what you inputted wasn't a valid option")
      print("Make sure you have entered a number between 1 and 3")
      input("press ENTER to try again")
  return activity1

def find_activity1(location): #Main hub funcation for having the user pick their activity
  clear()
  print("Question 4")
  time.sleep(1)
  blank()
  if location == "beach":
    activity1 = location_beach()
  elif location == "playground":
    activity1 = location_playground()
  elif location == "theme park":
    activity1 = location_theme_park()
  elif location == "zoo":
    activity1 = location_zoo()
  elif location == "mountain":
    activity1 = location_mountain()
  elif location == "lake":
    activity1 = location_lake()
  print("You chose to " + activity1)
  input("Press ENTER to continue to the next question ")
  return activity1

def gen_activity1_description(location, activity1, friend): #Randomly generates something that happens while the user is doing the activity they selcted
  random_number =  random.randint(0,4) #Generates a random number
  if location == "beach":
    if activity1 == "build a sandcastle":
      if random_number == 0:
        activity1_description = "You and " + friend + " build the sandcastle together and it has multiple towers and a large moat full of water."
      elif random_number == 1:
        activity1_description = "While building the sandcastle " + friend + " finds two crabs nearby that you crown king and queen of the castle."
      elif random_number == 2:
        activity1_description = "You build the sandcastle with really high walls that you then cover with shells you found."
      elif random_number == 3:
        activity1_description = "You remember that you forgot your bucket and spade so you have to go round to beach shop to buy some."
      elif random_number == 4:
        activity1_description = "You and " + friend + " build a sandcastle each and connect them by a small river."
      else:
        activity1_description = "You enjoy building your sandcastle." #The user should never get this option it is just there incase of error
    elif activity1 == "go swimming":
      if random_number == 0:
        activity1_description = "You and " + friend + " see lots of different types of fish while out swimming each a different colour."
      elif random_number == 1:
        sea_animals = ["a whale", "a dolphin", "a sea lion", "an otter", "a school of fish", "a group of turtles"]
        animal = random.choice(sea_animals)
        activity1_description = "While swimming you and " + friend + " spot " + animal + " out at sea."
      elif random_number == 2:
        activity1_description = "You dip your head under the water and see all of the interesting shells and plants that live in the sea."
      elif random_number == 3:
        activity1_description = "You and " + friend + " splash around together making sure not to get water in eachothers eyes."
      elif random_number == 4:
        activity1_description = "You swim around in the sea and ocasionally dunk your head under the water for a few seconds."
      else:
        activity1_description = "You enjoy swimming." #The user should never get this option it is just there incase of error
    elif activity1 == "sunbathe":
      if random_number == 0:
        activity1_description = "You lie on a beach towel by the water."
      elif random_number == 1:
        activity1_description = "You relax on a sunbed under the shade of an umbrella."
      elif random_number == 2:
        activity1_description = "You and " + friend + " enjoy the sun together in a quiet corner of the beach."
      elif random_number == 3:
        activity1_description = friend + " finds some rocks that the two of you can safely bathe on."
      elif random_number == 4:
        activity1_description = "You and " + friend + " both make sure to put lots of suncream on before you relax." 
      else:
        activity1_description = "You enjoy sunbathing." #The user should never get this option it is just there incase of error
  elif location == "playground":
    if activity1 == "play on the swings":
      if random_number == 0:
        time_swinging = str(random.randint(5,20))
        activity1_description = "You pick the swing on the far left and " + friend + " goes on the one next to you. You swing for " + time_swinging + " minutes."
      elif random_number == 1:
        activity1_description = "You try to swing as high as you can. Eventually, you swing high enough that you can see over the trees in the distance."
      elif random_number == 2:
        time_swinging = str(random.randint(15,30))
        activity1_description = "You and " + friend + " swing for " + time_swinging + " mintues. After this you feel dizzy so drink a big glass of water."
      elif random_number == 3:
        activity1_description = "Both of you swing slowly while chatting about what you did last weekend." 
      elif random_number == 4:
        activity1_description = friend + " pushes you for a while and then you push them for a while."
      else:
        activity1_description = "You enjoy your time on the swings" #The user should never get this option it is just there incase of error
    elif activity1 == "play on the slides":
      if random_number == 0:
        activity1_description = "You go for the biggest slide of them all and enjoy the slide down as it is really fast."
      elif random_number == 1:
        activity1_description = friend + " picks the biggest slide of them all and you feel proud of them as they zoom past you at the bottom."
      elif random_number == 2:
        size_options = ["small", "medium","huge"]
        size = random.choice(size_options)
        activity1_description = "You and " + friend + " decide to go down the " + size + " slide together."
      elif random_number == 3:
        activity1_description = "You choose to go down each slide starting from the smallest and finishing on the biggest."
      elif random_number == 4:
        win_options = [friend, "you"]
        winner = random.choice(win_options)
        if winner == "you":
          win = "win"
        else:
          win = "wins"
        activity1_description = "You both race eachother going down the slides and " + winner + " " + win + "."
      else:
        activity1_description = "You enjoy your time on the swings" #The user should never get this option it is just there incase of error
    elif activity1 == "play on the see-saw":
      if random_number == 0:
        activity1_description = "You take the red end of the see-saw and " + friend + " takes the blue end. You play for ages."
      elif random_number == 1:
        activity1_description = "While playing you try and get as high as you can when you're at the top. You make sure you are always holding the handle tight though."
      elif random_number == 2:
        time_playing = str(random.randint(15,45))
        activity1_description = "You and " + friend + " really enjoy the see-saw so spend " + time_playing + " minutes on it" 
      elif random_number == 3:
        conversation_topics = ["what you did last weekend", "what you're doing next weekend", "your favourite animal", "what job you want to do when you're older"]
        conversation = random.choice(conversation_topics)
        activity1_description = "You and " + friend + " sit on the see-saw and chat about " + conversation + "."
      elif random_number == 4:
        activity1_description = "After playing on the see-saw for a while you both go and rest on the grass next to it"
      else:
        activity1_description = "You enjoy your time on the see-saw" #The user should never get this option it is just there incase of error
  elif location == "theme park":
    if activity1 == "ride on a big roller coaster":
      ride_names = ["Thunderbolt", "Vortex", "Slingshot", "Goliath", "Whirlwind", "Phoenix", "Mantis", "Viper", "Tornado", "Speed"]
      ride = random.choice(ride_names)
      if random_number == 0:
        activity1_description ="You go on " + ride +  " the biggest roller coaster in the park. It's amazing."
      elif random_number == 1:
        wait_time = str(random.randint(35,60))
        if wait_time == "60":
          wait_time = "an hour"
        else: 
          wait_time = wait_time + " mintues"
        activity1_description ="You have to wait for " + wait_time + " to get on " + ride + " but it was worth the wait."
      elif random_number == 2:
        activity1_description ="You and " + friend + " really enjoy your ride so decide to buy the picture at the end." 
      elif random_number == 3:
        activity1_description = "There was no queue for " + ride + " so you decide to ride it twice."
      elif random_number == 4:
        activity1_description = friend + " recommends you ride " + ride + " you really enjoy it."
      else:
        activity1_description = "You enjoy your ride on the roller coaster" #The user should never get this option it is just there incase of error
    elif activity1 == "ride on a small roller coaster":
      ride_names = ["Corn", "There and back", "Around the world", "Adventurous", "Zipper", "Little dipper", "Comet"]
      ride = random.choice(ride_names)
      if random_number == 0:
        activity1_description = "You and " + friend + " ride " + ride + " and it was lots of fun."
      elif random_number == 1:
        times_ridden = str(random.randint(1,6))
        activity1_description = "After riding " + ride + " " + times_ridden + " times, you decide to take a break."
      elif random_number == 2:
        ride2 = random.choice(ride_names)
        looping = True
        while looping == True:
          if ride == ride2:
            ride2 = random.choice(ride_names)
          else:
            looping = False
        activity1_description = "After riding " + ride + " you decide to go and ride " + ride2 + "."
      elif random_number == 3:
        activity1_description = "After you and " + friend + " ride " + ride + " you take a break by sitting on a nearby bench"
      elif random_number == 4:
        activity1_description = "You were surprised to find a wait for " + ride + " so " + friend + " suggests you go for a walk around the park until the queue gets shorter"
      else:
        activity1_description = "You enjoy your ride on the roller coster" #The user should never get this option it is just there incase of error
    elif activity1 == "ride a water ride":
      ride_names = ["the log flume", "the river boat", "the water rapids boat", "the water slide"]
      ride = random.choice(ride_names)
      if random_number == 0:
        activity1_description = "You get really wet while on " + ride + " luckily " + friend + " manages to stay dry."
      elif random_number == 1:
        queue_time = str(random.randint(15,45))
        activity1_description = "After waiting " + queue_time + " minutes to get on " + ride + " you really enjoy it."
      elif random_number == 2:
        activity1_description = "You manage to ride all the water rides at the theme park however " + ride + " was your favourite."
      elif random_number == 3:
        activity1_description = "After riding " + ride + " you sit next to the log flume and " + friend + " gets soaked as it goes past."
      elif random_number == 4:
        times_ridden = str(random.randint(5,10))
        activity1_description = "You manage to ride " + ride + " " + times_ridden + " times." 
      else:
        activity1_description = "You enjoy riding the water ride" #The user should never get this option it is just there incase of error
  elif location == "zoo":
    if activity1 == "see an African animal":
      animal_list = ["elephants", "lions", "giraffes", "zebras", "wild dogs", "rhinos", "cheetahs", "monkeys", "leopards", "hippopotamus", "wild boars"]
      animal = random.choice(animal_list)
      if random_number == 0:
        activity1_description = "After walking around the zoo, " + friend + " suggests that you go and see the " + animal + "."
      elif random_number == 1:
        animal = animal[:-1]
        activity1_description = "You arrive at the " + animal + " exibit and the keeper is in the middle of feeding them which you enjoyed watching."
      elif random_number == 2:
        looping1 = True
        animal2 = random.choice(animal_list)
        while looping1 == True:
          if animal2 == animal:
            animal2 = random.choice(animal_list)
          else:
            looping1 = False
        looping2 = True
        animal3 = random.choice(animal_list)
        while looping2 == True:
          if animal3 == animal or animal3 == animal2:
            animal3 = random.choice(animal_list)
          else:
            looping2 = False
        activity1_description = "You go and see 3 animals: the " + animal + ", the " + animal2 + " and the " + animal3 + ". " + friend + " says that " + animal2 + " was thier favourite."
      elif random_number == 3:
        animal = animal[:-1]
        activity1_description = "You get to go on an tour of the " + animal + " enclosure. You made sure to follow all the keeper's instructions so you stayed safe."
      elif random_number == 4:
        animal = animal[:-1]
        activity1_description = "After seeing all the animals " + friend + " buys you a " + animal + " cuddly toy."
      else:
        activity1_description = "You enjoy seeing the animals" #The user should never get this option it is just there incase of error
    elif activity1 == "see a farm animal":
      animal_list = ["cows", "pigs", "chickens", "goats", "sheep", "ducks", "horses"]
      animal = random.choice(animal_list)
      if random_number == 0:
        activity1_description = "You and see the " + animal + " and really enjoy it."
      elif random_number == 1:
        animal2 = random.choice(animal_list)
        looping = True
        while looping == True:
          if animal2 == animal:
            animal2 = random.choice(animal_list)
          else:
            looping = False
        activity1_description = friend + " asks you if you think " + animal + " is better than " + animal2 + " after going to see them both. You find it too hard to choose."
      elif random_number == 2:
        activity1_description = "While visting the " + animal + " you get the opportunity to feed them."
      elif random_number == 3:
        waiting_time = str(random.randint(5,20))
        activity1_description = "After waitng " + waiting_time + "to see the " + animal + ", they finally come into sight."
      elif random_number == 4:
        activity1_description = friend + " suggests that you go and see the " + animal + " and you think it's a great idea."
      else:
        activity1_description = "You enjoy seeing the animals" #The user should never get this option it is just there incase of error
    elif activity1 == "go to the bug house":
      animal_list = ["spiders", "ants", "beetles","caterpillars", "butterflies", "millipedes", "scorpions"]
      animal = random.choice(animal_list)
      if random_number == 0:
        activity1_description = "You got to see all the bugs but the " + animal + " were your favourite"
      elif random_number == 1:
        if animal == "butterflies":
          animal = "butterfly"
        else: 
          animal = animal[:-1]
        activity1_description = "You were able to hold a " + animal + ". You thought it was great but " + friend + " was too scared to have a go."
      elif random_number == 2:
        time_looking = str(random.randint(3,9))
        activity1_description = "After staring for " + time_looking + " minutes, you finally notice the " + animal + " in its enclosure"
      elif random_number == 3:
        activity1_description = "You and " + friend + " spent ages looking at the " + animal + "."
      elif random_number == 4:
        looping = True
        animal2 = random.choice(animal_list)
        while looping == True:
          if animal2 == animal:
            animal2 = random.choice(animal_list)
          else:
            looping = False
        activity1_description = "After looking at all the bugs you think that " + animal + " are the best. However, " + friend + " thinks that " + animal2 + " are the best. You agree they are both great."
      else:
        activity1_description = "You enjoyed looking  at all the bugs" #The user should never get this option it is just there incase of error
  elif location == "mountain":
    if activity1 == "go for a hike up the mountain" :
      time_hours = str(random.randint(1,3))
      time_mins = str(random.randint(1,59))
      if time_hours == 1:
        time_total = time_hours, "hour and", time_mins, "minutes"
      elif time_hours == 1 and time_mins == 1:
        time_total = time_hours, "hour and", time_mins, "minute"
      elif time_mins == 1:
        time_total = time_hours, "hours and", time_mins, "minute"
      else:
        time_total = time_hours, "hours and", time_mins, "minutes"
      if random_number == 0:
        activity1_description = "You and " + friend + " walked for " + time_total + " and you managed to make it to the top"
      elif random_number == 1:
        activity1_description = "You and " + friend + " walked for " + time_total + ". You got slightly lost on the way but still made it to the top"
      elif random_number == 2:
        activity1_description = "You and " + friend + " walked for " + time_total + ". After you stopped to look at the amazing views you made it to the top"
      elif random_number == 3:
        activity1_description = "You and " + friend + " walked for " + time_total + ". You only made it halfway up before you got tired but still enjoyed yourself"
      elif random_number == 4:
        sky_options = ["sunrise", "sunset"]
        sky = random.choice(sky_options)
        activity1_description = "You and " + friend + " walked for " + time_total + ". you walk to the top during " + sky + " meaning the sky looked very pretty"
      else:
        activity1_description = "" #The user should never get this option it is just there incase of error
    elif activity1 == "look for animals" :
      animal_list = ["deer", "sheep", "foxes", "wolves", "cows"]
      if random_number == 0:
        animal_list = ["deer", "sheep", "fox", "wolf", "cow"]
        animal = random.choice(animal_list)
        activity1_description = "You spot a lone " + animal + " standing in a nearby field"
      elif random_number == 1:
        animal = random.choice(animal_list)
        activity1_description = "You and " + friend + " spot a large group of " + animal + "in the distance"
      elif random_number == 2:
        animal = random.choice(animal_list)
        animal2 = random.choice(animal_list)
        animal3 = random.choice(animal_list)
        looping1 = True
        while looping1 == True:
          if animal == animal2:
            animal2 = random.choice(animal_list)
          else:
            looping = False
        looping2 = True
        while looping2 == True:
          if animal3 == animal2 or animal3 == animal:
            animal3 = random.choice(animal_list)
          else:
            looping2 = False
        activity1_description = "You manage to spot quite a few " + animal + " plus some " + animal2 + " and a few " + animal3 + "."
      elif random_number == 3:
        activity1_description = "While you are looking at some fields " + friend + " spots a large group of birds in a nearby tree and calls you to look."
      elif random_number == 4:
        time_looking = random.randint(15,30)
        activity1_description = "After looking around for " + time_looking + " minutes you decide to stop looking."
      else:
        activity1_description = "You enjoy looking for animals" #The user should never get this option it is just there incase of error  
    elif activity1 == "take photographs" :
      if random_number == 0:
        animal_list = ["deer", "sheep", "fox", "wolf", "cow"]
        animal = random.choice(animal_list)
        activity1_description = "You manage to get an amazing picture of a " + animal
      elif random_number == 1:
        animal_list = ["deer", "sheep", "fox", "wolf", "cow"]
        animal = random.choice(animal_list)
        activity1_description = friend + " gets a great picture of " + animal + " you tell them how good it is."
      elif random_number == 2:
        nature_list = ["trees", "bushes", "rocks", "hills", "leaves"]
        nature = random.choice(nature_list)
        activity1_description = "You get a great picture of a group of " + nature + "."
      elif random_number == 3:
        nature_list = ["trees", "bushes", "rocks", "hills", "leaves"]
        nature = random.choice(nature_list)
        activity1_description = friend + " gets an amazing photo of " + nature + "."
      elif random_number == 4:
        number_photos = random.randint(10,30)
        activity1_description = "You manage to get " + number_photos + " pictures that you'll print off later."
      else:
        activity1_description = "You enojy taking photos" #The user should never get this option it is just there incase of error
  elif location == "lake":
    if activity1 == "rent a boat":
      if random_number == 0:
        time_rented = str(random.randint(1,3))
        activity1_description = "You rent a speedboat for " + time_rented + " hours."
      elif random_number == 1:
        time_rented = str(random.randint(1,3))
        activity1_description = "You rent a sailboat for " + time_rented + " hours."
      elif random_number == 2:
        time_rented = str(random.randint(1,3))
        activity1_description = "You rent a canoe for " + time_rented + " hours."
      elif random_number == 3:
        time_rented = str(random.randint(1,3))
        activity1_description = "You rent a rowing boat for " + time_rented + " hours."
      elif random_number == 4:
        time_rented = str(random.randint(1,3))
        activity1_description = "You rent a pedal boat for " + time_rented + " hours."
      else:
        activity1_description = "You enjoyed renting your boat" #The user should never get this option it is just there incase of error
    elif activity1 == "go fishing":
      fish_options = ["cod", "trout", "salmon", "carp", "bass","catfish"]
      fish = random.choice(fish_options)
      if random_number == 0:
        size = random.randint(20,40)
        activity1_description = "You catch a " + fish + "that is " + size + "cm long."
      elif random_number == 1:
        size = random.randint(45,70)
        activity1_description = "You catch a huge " + fish + " that is a massive " + size + "cm long."
      elif random_number == 2:
        size = random.randint(20,40)
        activity1_description = friend + "catches a " + size + "cm long " + fish + ". You congratulate them."
      elif random_number == 3:
        amount_caught = random.randint(3,7)
        activity1_description = "You manage to catch " + amount_caught + fish + " but " + friend + " only catches one. You both did great."
      elif random_number == 4:
        activity1_description = "All you seem to be able to fish is boots and water bottles but you still enjoy yourself."
      else:
        activity1_description = "You enjoy fishing" #The user should never get this option it is just there incase of error
    elif activity1 == "go for a swim in the lake" :
      if random_number == 0:
        time_swimming = random.randomint(15,45)
        activity1_description = "You spend " + time_swimming + " swimming in some shallow water."
      elif random_number == 1:
        time_swimming = random.randomint(15,45)
        activity1_description = "You spend " + time_swimming + " swimming in some deeper water."
      elif random_number == 2:
        activity1_description = "While swimming " + friend + "notices a group of small fish under the water"
      elif random_number == 3:
        activity1_description = "You and " + friend + " splash around together making sure not to get water in eachothers eyes."
      elif random_number == 4:
        activity1_description = "You swim far enough out that the water is up to your shoulders when you stand up"
      else:
        activity1_description = "You enojy swimming" #The user should never get this option it is just there incase of error
  return activity1_description

def food_beach(): #Asks the user to pick an eating location if they chose the beach as thier location
  clear()
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid location that they agree is correct
    looping2 = True
    while looping2 == True: #Loops until the user picks a valid location
      print("Pick one of the following locations that you'd like to eat in:")
      blank()
      print("1) Restaurant")
      print("2) Chip shop")
      print("3) Picnic")
      food = input("Type the number that links with the location you want: ")
      clear()
      if food == "1":
        food_options = ["a burger with chips.", "Soup with bread.", "a pizza with gralic bread."]
        food = "you go to a restaurant and have " + random.choice(food_options)
        location = "restaurant"
        looping2 = False
      elif food == "2":
        food_options = ["cod", "fish cake", "Sausage"]
        food = "you go to a chip shop and have " + random.choice(food_options) + " and chips."
        location = "chip shop"
        looping2 = False
      elif food == "3":
        food_options =["cheese", "ham", "egg"]
        food = "you go for a picnic and you have a " + random.choice(food_options) + " sandwich and crisps."
        location = "picnic"
        looping2 = False
      else: 
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you only enter the number of the location you'd like")
        input("Press ENTER to continue ")
        clear()
    looping3 = True
    while looping3 == True: #Loops until the user picks 'yes' or 'no'
      print("Is", location.upper(), "Right?")
      correct = input("If yes then type YES or if not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping1 = False
        looping3 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        looping3 = False
        time.sleep(2)
        clear()
      else:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you are typing either YES or NO")
        input("Press ENTER to try again ")
        clear()
      print("The location where you will eat is " + location)
  return food

def food_theme_park_zoo(): #Asks the user to pick an eating location if they chose the theme park or the zoo as thier location
  clear()
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid location that they agree is correct
    looping2 = True
    while looping2 == True: #Loops until the user picks a valid location
      print("Pick one of the following locations that you'd like to eat in:")
      blank()
      print("1) Chicken shop")
      print("2) Burger shop")
      print("3) Picnic")
      food = input("Type the number that links with the location you want: ")
      clear()
      if food == "1":
        food_options = ["chicken breast.", "chicken drumsticks.", "popcorn chicken."]
        food = "you go to the chicken shop and and have " + random.choice(food_options)
        location = "chicken shop"
        looping2 = False
      elif food == "2":
        food_options = ["chicken", "beef", "fish"]
        food = "you go to the burger shop and have " + random.choice(food_options) + " burger and chips."
        location = "burger shop"
        looping2 = False
      elif food == "3":
        food_options =["cheese", "ham", "egg"]
        food = "you go for a picnic and you have a " + random.choice(food_options) + " sandwich and crisps."
        location = "picnic"
        looping2 = False
      else: 
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you only enter the number of the location you'd like")
        input("Press ENTER to continue ")
        clear()
    looping3 = True
    while looping3 == True: #Loops until the user picks 'yes' or 'no'
      print("Is", location.upper(), "Right?")
      correct = input("If yes then type YES or if not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping1 = False
        looping3 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        looping3 = False
        time.sleep(2)
        clear()
      else:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you are typing either YES or NO")
        input("Press ENTER to try again ")
        clear()
      print("The location where you will eat is " + location)
  return food

def food_other(): #Asks the user to pick an eating location if they chose the playground, moutain or lake as their location
  clear()
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid location that they agree is correct
    looping2 = True
    while looping2 == True: #Loops until the user picks a valid location
      print("Pick one of the following locations that you'd like to eat in:")
      blank()
      print("1) Barbecue")
      print("2) Cafe")
      print("3) Picnic")
      food = input("Type the number that links with the location you want: ")
      clear()
      if food == "1":
        food_options = ["a burger.", "a hot dog.", "corn on the cob."]
        food = "you go to a restaurant and have " + random.choice(food_options)
        location = "barbecue"
        looping2 = False
      elif food == "2":
        food_options = ["chips", "a hot dog", "a burger"]
        food = "you go to a cafe and have " + random.choice(food_options) + "."
        location = "cafe"
        looping2 = False
      elif food == "3":
        food_options =["cheese", "ham", "egg"]
        food = "you go for a picnic and you have a " + random.choice(food_options) + " sandwich and crisps."
        location = "picnic"
        looping2 = False
      else: 
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you only enter the number of the location you'd like")
        input("Press ENTER to continue ")
        clear()
    looping3 = True
    while looping3 == True: #Loops until the user picks 'yes' or 'no'
      print("Is", location.upper(), "Right?")
      correct = input("If yes then type YES or if not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping1 = False
        looping3 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        looping3 = False
        time.sleep(2)
        clear()
      else:
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you are typing either YES or NO")
        input("Press ENTER to try again ")
        clear()
      print("The location where you will eat is " + location)
  return food

def find_food(location):# Main hub funcation for having hte user pick their food location
  if location == "beach":
    food = food_beach()
  elif location == "theme park" or location == "zoo":
    food = food_theme_park_zoo()
  elif location == "playground" or location == "mountain" or location == "lake":
    food = food_other() 
  input("Press ENTER to continue to the next question ")
  return food

def find_house(): #Asks the user to pick a house
  clear()
  print("Question Number 5")
  time.sleep(1)
  blank()
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid location that they agree is correct
    looping2 = True
    while looping2 == True: #Loops until the user picks a valid location
      print("Pick one of the following houses that you and " + friend + " go back to:")
      blank()
      print("1) Terraced house")
      print("2) Mansion")
      print("3) Castle")
      print("4) Underground cave")
      print("5) Campervan")
      blank()
      house = input("Type the number that links with the house you want: ")
      clear()
      if house == "1":
        house = "terraced house"
        looping2 = False
      elif house == "2":
        house = "mansion"
        looping2 = False
      elif house == "3":
        house = "castle"
        looping2 = False
      elif house == "4":
        house = "underground cave"
        looping2 = False
      elif house == "5":
        house = "campervan"
        looping2 = False
      else: 
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you only enter the number of the house you'd like")
        input("Press ENTER to continue ")
        clear()
    looping3 = True
    while looping3 == True: #Loops until the user picks 'yes' or 'no'
      print("Is", house.upper(), "Right?")
      correct = input("If yes then type YES or if not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping1 = False
        looping3 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        looping3 = False
        time.sleep(2)
        clear()
  print("The location where you'll live is", house + ".")
  input("Press ENTER to continue to the next question ")
  return house

def find_activity2(friend):#Asks the user to pcik an actvity to do once they get back to their house
  clear()
  print("Question Number 6")
  time.sleep(1)
  blank()
  looping1 = True
  while looping1 == True: #Loops until the user picks a valid location that they agree is correct
    looping2 = True
    while looping2 == True: #Loops until the user picks a valid location
      print("Pick one of the following activites to do when you get back home: ")
      blank()
      print("1) Watch some television")
      print("2) Play a video game")
      print("3) Play a board game")
      blank()
      activity2 = input("Type the number that links with the activity you want to do: ")
      clear()
      if activity2 == "1":
        activity_options = ["your favourite episode of your favourite show is on.", "you decide to watch some cartoons.", "you watch a film about animals."]
        activity_description = random.choice(activity_options)
        activity2 = "You and " + friend + " decide to watch some television and " + activity_description
        activity = "watch some television"
        looping2 = False
      elif activity2 == "2":
        activity_options = ["you win.", "you loose.", "you draw."]
        activity_description = random.choice(activity_options)
        activity2 = "You and " + friend + " decide to play some video games. After playing 1 game you " + activity_description
        activity = "play a video game"
        looping2 = False
      elif activity2 == "3":
        activity_options = ["monopoly.", "cluedo.", "the game of life."]
        activity_description = random.choice(activity_options)
        activity2 = "You and " + friend + " decide to play a board game. You play " + activity_description + " it was lots of fun."
        activity = "play a board game"
        looping2 = False
      else: 
        print("Sorry what you inputted wasn't a valid option")
        print("Make sure you only enter the number of the house you'd like")
        input("Press ENTER to continue ")
        clear()
    looping3 = True
    while looping3 == True: #Loops until the user picks 'yes' or 'no'
      print("Is", activity.upper(), "Right?")
      correct = input("If yes then type YES or if not type NO: ")
      clear()
      correct = correct.lower()
      if correct == "yes":
        looping1 = False
        looping3 = False
        clear()
      elif correct == "no":
        print("Okay, lets try again")
        looping3 = False
        time.sleep(2)
        clear()
  print("The activity you decide to do is " + activity + ".")
  input("Press ENTER to continue ")
  clear()
  return activity2

def save_story(first_line, paragraph, last_line, user_name, location):
  current_date = str(datetime.datetime.today().strftime('%Y_%m_%d:%H_%M'))
  title = user_name + "'s story about going to " + location + ": " + current_date +".txt"
  file_path = "./stories"
  file_name = os.path.join(file_path, title)
  story_file = open(file_name, "a")
  story_file.write(first_line)
  story_file.write("\n")
  story_file.write(paragraph)
  story_file.write("\n")
  story_file.write(last_line)
  story_file.close()
  return


##### Run Order #####

welcome_screen()
user_name = str(find_name())
location = str(find_location())
friend = str(find_friend())
activity1 = str(find_activity1(location))
activity1_description = str(gen_activity1_description(location, activity1, friend))
food = str(find_food(location))
house = str(find_house())
activity2 = str(find_activity2(friend))

##### Story formation #####
weather_options = ["sunny", "rainy", "cloudy", "snowy"]
weather = random.choice(weather_options)
day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day = random.choice(day_options)
first_line = "The following is a short story about " + user_name + " and their friend " + friend + ": "
paragraph = "On a " + weather + " " + day + " morning you and " + friend + " leave your " + house + " to go to the " + location + ". When you get there you " + activity1 + ". " + activity1_description +" Once you have finished you " + food + " After your fun day out at the " + location + " you go back home to your " + house + ". Once you get there " + activity2 + " After this you go to sleep thinking about how much fun you had. "
last_line = "The End."

##### Story printing #####
clear()
print("It is now time to see your story")
input("Press ENTER to view: ")
clear()
print(first_line)
print(paragraph)
print(last_line)
blank()
looping = True
while looping == True:
  print("Would you like to save this story")
  save = input("Type YES if you do and if not type NO")
  clear()
  save = save.lower()
  if save == "yes":
    print("Okay, now saving")
    save_story(first_line, paragraph, last_line, user_name, location)
    looping = False
    #print("sorry this feature is not avalible yet")
  elif save == "no":
    print("Okay this story will not be saved")
    looping = False
  else:
    print("That input was invalid. Please make sure you neter either YES or NO")
    input("Press ENTER to try again")
print("Thank you " + user_name + " for using the story box. Hopefully you enjoyed.")
input("Press ENTER to return to the main menu")
clear()

##### Testing #####
#print(activity1_description)#For testing use
#print(gen_activity1_description("beach", "build a sandcastle" , "Jim")) #For testing use
"""
#For testing use
print(user_name)
print(location)
print(friend)
print(activity1)
print(activity1_description)
print(food)
print(house)
print(activity2)
"""
