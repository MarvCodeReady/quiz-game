print("Hello, welcome to quiz game!")
#create a variable called playing
#created input() function with prompt
playing = input("Would you like to play? ")

#use if statement to quit game if player condition is not equal to yes
#use .lower() to convert user answer to lowercase
if playing.lower() != "yes":
    quit()

#Add string if user continues game
print("Alright then lets begin")

#Create a variable to track score
score = 0
#create variable to ask user question and recieve input
answer = input("What state is San Francisco located in? ")
#Added if else statement to confirm if users answer is correct or incorrect
if answer.lower() == "california":
    print("You are Correct!")
    score += 1 #Every time user gets something correct add 1 to the score
else: 
    print("That is incorrect!")
    
#Second question
answer = input("What continent is Brazil located in? ")
if answer.lower() == "south america":
    print("You are Correct!")
    score += 1 #By doing '+= 1' the score is being increased by one 
else: 
    print("That is incorrect!")
    
#Third question
answer = input("Beijing is the capitol of what country? ")
if answer.lower() == "china":
    print("You are Correct!")
    score += 1
else: 
    print("That is incorrect!") 

#Fourth question
answer = input("Paris is located in what country? ")
if answer.lower() == "france":
    print("You are Correct!")
    score += 1
else: 
    print("That is incorrect!") 

#Fifth question
answer = input("Who was the first president of the United States? ")
if answer.lower() == "george washington":
    print("You are Correct!")
    score += 1
else: 
    print("That is incorrect!")

#Sixth question
answer = input("Who was the second president of the United States? ")
if answer.lower() == "john adams":
    print("You are Correct!")
    score += 1
else: 
    print("That is incorrect!")
    
#use str() to turn score variable into a string, it is originally an integer
print("you recieved a score of " + str(score))
