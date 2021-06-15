print("Welcome to my quiz!")

playing = input("Do you want to play?")

if playing != "yes":
    quit()

print("okay lets play :)")
score=0


#1
answer = input("Who is the owner of SpaceX? and Tesla ")
if answer == "elon musk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#2
answer = input("What is the name of smallest unit of data? ")
if answer == "bit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#3
answer = input("What was the orignal name of google? ")
if answer == "backrub":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#4
answer = input("What does iss stand for? ")
if answer == "international space station":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100) + "%.")