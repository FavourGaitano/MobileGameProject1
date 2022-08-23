print("Welcome to my phone quiz!")
playing=input("Do you want to play? ").lower()
if playing != "yes":
    quit()
print("Okay! Let's Begin")
score = 0
answer = input("What does RPF stand for? ").lower()
if answer == "rwanda patriot forum":
    print("You got it! CORRECT")
    score += 1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("You got it! CORRECT")
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("You got it! CORRECT")
    score += 1
else:
    print("Incorrect!")
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("You got it! CORRECT")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")