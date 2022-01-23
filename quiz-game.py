print("Hello, welcome to quiz game!")
#create a variable called playing
#created input() function with prompt
playing = input("Would you like to play? ")

#use if statement to quit game if player condition is not equal to yes
if playing != "yes":
    quit()

#Add string if user continues game
print("Alright then lets begin")

#create variable to ask user question and recieve input
answer = input("What state is San Francisco located in? ")
#Added if else statement to confirm if users answer is correct or incorrect
if answer == "california":
    print("You are Correct!")
else: 
    print("That is incorrect!")

#Second question
answer = input("What continent is Brazil located in? ")
if answer == "south america":
    print("You are Correct!")
else: 
    print("That is incorrect!")

#Third question
answer = input("Beijing is the capitol of what country? ")
if answer == "china":
    print("You are Correct!")
else: 
    print("That is incorrect!")

#Fourth question
answer = input("Paris is located in what country? ")
if answer == "france":
    print("You are Correct!")
else: 
    print("That is incorrect!")

#Fifth question
answer = input("Who was the first president of the United States? ")
if answer == "george washington":
    print("You are Correct!")
else: 
    print("That is incorrect!")

#Sixth question
answer = input("Who was the second president of the United States? ")
if answer == "john adams":
    print("You are Correct!")
else: 
    print("That is incorrect!")