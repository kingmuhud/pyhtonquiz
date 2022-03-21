print("Welcome to the quiz \n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Let's play :)")
score = 0

answer = input("1. What is green and red and starts with first letter of the alphabet? ")
if answer.lower() == "apple":
    print("correct!")
    score += 1
else:
    print("wrong")

answer = input("2. What is second letter of the alphabet? ")
if answer.lower() == "b":
    print("correct!")
    score += 1
else:
    print("wrong")

answer = input("3. What is teacher's name? ")
if answer.lower() == "teacher moha" or answer.lower() == "moha":
    print("correct!")
    score += 1
else:
    print("wrong")
# can copy and paste and write as many questions as you like?

print("Your total score is " + str(score) + ".")
print("Your total score is " + str((score / 3) * 100) + "%.")
