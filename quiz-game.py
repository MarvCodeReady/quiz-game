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
