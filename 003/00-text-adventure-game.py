import time
import os

print('''
**********************************************************
       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^  \n      /|\/|\/|\ /|\    /\-_--\    /|\/|\0/|\/|\/|\ /|\/|\ \n      /|\/|\/|\ /|\   /  \_-__\   /|\/|\H/|\/|\/|\ /|\/|\ \n      /|\/|\/|\ /|\   |[]| [] |   /|\/|\⨅/|\/|\/|\ /|\/|\ \n    
**********************************************************
''')
print("Welcome to Escape the Dark Forest.")
print("Your mission is to escape from the forest... and from **it**.") 

# Start

time.sleep(2)
print('''
You find yourself inside a small cave.
You hid here because it was raining a lot earlier while you were taking a stroll, but now it has stopped.
The thing is... you took a too long nap, and now it's night time!
You should get out of the forest as fast as you can. You've heard some weird stories about it...

    You get out of the cave, and switch on your small flashlight.
    You can see three paths, but can't remember where you came from.
''')

time.sleep(1)
choice = input("Do you wanna go left, right or center?: ")

time.sleep(1)
os.system('clear')
# Still Alive
if choice == "left":
  print(''' 
    Okay, now you can see a... lake? The moon is reflected, it's actually really beautiful!
    You can also see a bridge. The lake looks too big and deep to swim now, but the bridge looks pretty old...
  ''')
  time.sleep(1)
  choice = input("Do you wanna try crossing the bridge, or going right? C or R: ").upper()
  
  time.sleep(1)
  os.system('clear')
  # Still Alive
  if choice == "R":
    choice = "center"

  # Game Over
  else:
    print('''
      ****************************************
                    GAME OVER
      ****************************************
      The bridge couldn't hold your weight and broke down.
      The last thing you can feel is something grabbing you by your feet... deep into the cold lake.
    ''')

# Still Alive
if choice == "center":
  print('''
    You get into a clearing in the forest.
    Now that you think of it, you could try and check if there's any signal.
    Maybe you could open that famous navigation app and search for a way out.
    Or maybe you should hurry and keep walking instead...
  ''')
  time.sleep(1)
  choice = input("Do you wanna try the GPS, or keep walking? G or W: ").upper()

  time.sleep(1)
  os.system('clear')
  # Game Over
  if choice == "G":
    print('''
    ****************************************
                  GAME OVER
    ****************************************
    It kinda looks like there's some signal, so you try opening the app...
    And it's loading... and still loading...
    After a couple of minutes, you feel a cold limb grab you from behind.
    It found you.
    ''')

  # Still Alive
  else:
    print(''' 
    You decide it might be a better idea to keep walking.
    You kinda remember going through here before, so you continue that path.
    After 10 minutes of walking, you can see the edge of the forest!

    But... you can also hear some loud footsteps behind you. FAST footsteps.
    ''')

    time.sleep(1)
    choice = input("Do you wanna try and run for the edge, or hide for a moment? R or H: ").upper()

    time.sleep(1)
    os.system('clear')
    
    # Game Over
    if choice == "R":
      print('''
      ****************************************
                    GAME OVER
      ****************************************
      You take a deep breath and begin running.
      You were super fast in P.E., so it's almost impossible it can get you!! Right?
      Or maybe not.
      Suddenly, the only thing you can see is the ground while something cold is pulling you by your feet, back into the darkness.
    ''')

    # WIN
    else:
      print(''' 
      ****************************************
                      WINNER!
      ****************************************
      You hide fast behind some bushes, while peeking through them.
      After what felt like a second, you can see a blurred dark figure appear.
      It almost feels like it's not there, but... You can feel yourself sweating and holding your breath just from looking at it.

      A minute passes and it suddenly disappears. 
      You get to the edge of the forest really cautiously.

      When you arrive home, you take a hot bath and make yourself a hot cup of chocolate. 
      Maybe you should check the weather before going for a stroll from now on...
      ''')
    
# Game Over
elif choice == "right": 
  print('''
  ****************************************
                GAME OVER
  ****************************************
  It found you... It was **right** there! :(
  ''')


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload