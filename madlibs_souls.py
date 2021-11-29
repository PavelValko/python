# Init Variables
theAgeofAncient = ""
adjective = ""
creatures = ""
theDragons = ""
nouns = [""] * 10
gods = [""] * 5
epic = [""] * 2
power = ""
newEra = ""
theUndead = ""
name = ""


# Get Input From User
print("Hello, my friend and welcome to your story. What's your name?")
name = input("Enter your name, please: ")

print(f"Nice to meet you, {name}")

print("What time of the age do you like?")
theAgeofAncient = input("Enter the age of ... : ")

adjective = input("I need to one adjective, enter please: ")

print("What's creatures do you know?")
creatures = input()

print("Name who you don't like.")
theDragons = input("Enter its name: ")

print("Now we need to enter ten nouns.")
for i in range(len(nouns)):
	nouns[i] = input(f"Enter {i+1} noun: ")

print("What gods do you like? Choose five gods.")
for i in range(len(gods)):
	gods[i] = input(f"God number {i+1} is: ")

print("We need two epic words!")
for i in range(len(epic)):
	epic[i] = input(f"Word {i+1}: ")

print("Then we need power of your gods!")
power = input("Enter them power. It will be called: ")

print("What would you call a new era?")
newEra = input("Enter it: ")

print("How would you like to name your hero?")
theUndead = input("Enter his name: ")

print("Nice. We have done this. We made history! Now let's see what we've got!")


# Init Story
main_story = f"In {theAgeofAncient}, the world was {adjective}, shrouded by {nouns[8]}. A land of gray crags, {creatures} and {theDragons}. But then there was {nouns[0]}, and with {nouns[0]} came disparity. {nouns[1]} and {nouns[2]}, {nouns[3]} and {nouns[4]}, and of course, {nouns[5]} and {nouns[6]}. Then from the {nouns[6]}, they came, and found {power} within the {nouns[7]}. {gods[0]}, the first of the dead. {gods[1]}, and her Daughters of {epic[0]}. {gods[2]}, the Lord of {epic[1]} and his faithful knights, and the furtive {gods[3]}, so easily forgotten. With {power}, they challenched {theDragons}. {gods[2]}'s mighty bolts peeled apart their stone scales. {gods[1]} weaved great firestorms. {gods[0]} unlished a miasma of {nouns[4]} and {nouns[9]}. And {gods[4]} betrayed his own, and {theDragons} were no more. Thus began {newEra}. But soon, the flames will fade, and only {nouns[6]} will remain. Even now, there are only embers, and man sees not {nouns[5]}, but only endless nights. And amongst the living are seen, carriers of the accursed Darksign. Yes, indeed. The Darksign brands {theUndead}. And in this land, {theUndead} are corralled and led to the north, where they are locked away, to await the end of the world. ...This is your fate, {name}."

# Print Story


print(main_story)


# "In {theAgeofAncient}, the world was {unformed}, shrouded by {fog}. A land of gray crags, {creatures} and {theDragons}. But then there was {fire}, and with {fire} came {disparity}. {Heat} and {cold}, {life} and {death}, and of course, {light} and {dark}. Then from the {dark}, they came, and found {theSoulsOfLords} within the {flame}. {Nito}, the first of the {dead}. {theWitchofIzalith}, and her Daughters of {Chaos}. {Gwyn}, the Lord of {Sunlight} and his faithful knights, and the furtive {pygmy}, so easily forgotten. With {theStrengthOfLords}, they challenched {theDragons}. {Gwyn}'s mighty bolts peeled apart their stone scales. {TheWitches} weaved great firestorms. {Nito} unlished a miasma of {death} and {disease}. And {SeathTheScaleless} betrayed his own, and {theDragons} were no more. Thus began {theAgeOfFire}. But soon, the {flames} will fade, and only {Dark} will remain. Even now, there are only embers, and man sees not {light}, but only endless nights. And amongst the living are seen, carriers of the accursed Darksign. Yes, indeed. The Darksign brands {theUndead}. And in this land, {theUndead} are corralled and led to the north, where they are locked away, to await the end of the world. ...This is your fate, {name}