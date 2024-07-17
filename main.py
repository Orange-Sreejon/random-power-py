import time
import random

print("Hello there")
name = input("what's your name\n")
time.sleep(1)
print("Hello " + name + " good to see you")
time.sleep(1)
room = input("To enter the room you We need the code\npass: ")

if room == "kira":
    print("your are welcome sir,")
    time.sleep(.5)
    print("Are you sure do you know go?")
else:
    print("I'm sorry, but you can't enter the room")
    exit()
time.sleep(1)
choice = input("y/n\n")

if choice == "y":
    print("Open the potal. Go throw sir")
    print("wait.....")
    time.sleep(1.5)
    print("still going...")
    time.sleep(1)
    print("almost there..")
    time.sleep(4)
    print("Congratulations, you entered the room!")
    time.sleep(2)
    print("Good to see you after a long time")
else:
    print("sorry you did't enter")
    exit()

print("hello sir, and now the moment has come. that we are all waiting for")
time.sleep(2)
print("and now hear is your supper power")
time.sleep(2)

items = ['Super Maggots', 'Super Learning', 'Explosive Farting', 'Strength', 'Poison Generation', 'Channel the Devil', 'Evil Projections', 'Persuasion', 'Communicate with Cities', 'Control over the Elements', 'Detachable Limbs', 'Understand All Languages', 'Insect Control', 'Pheromones', 'Super Speed', 'Organ Rearranging', 'Mimic Other Powers', 'Control Machines', 'Darkness Dimension', 'Converting Sound to Light', 'Advanced Ryuo', 'Ultra Instinct', 'Control Over Other People', 'Destroy And Restore Things', 'shadows!','Future Sight', 'Op-Op Fruit', 'Manipulate Matter', 'Limitless','The Mangekyo Sharingan', 'Alchemy Can Be Used To Do Just About Anything', 'Life Creation ', 'Izanami ', 'Spirit Gun ', 'Comedian ', 'One For All ', 'Time-Skip ', 'Kotodama ', 'All For One ', 'Sharingan ', 'shadow']

selected_item = random.choice(items)

choice = input("do you wanna it  y/n\n")

if choice == "y":
    time.sleep(.5)
    print("...")
    time.sleep(.3)
    print("......")
    time.sleep(.3)
    print("........")
    time.sleep(.3)

    print("You have been granted the power of " + selected_item + "!")

else:
    print("ok no problem")
    exit()
