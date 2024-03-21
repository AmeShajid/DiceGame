#Dice Game basically a dice game you can play with 4 people

import random #import random so when you use the module it generates a random number

#getting a dice simulator
def roll():
    min_value = 1 # this is lowest number we want
    max_value = 6 # this is the max number we want
    roll = random.randint(min_value, max_value) # our roll will = to a random integer between 1 and 6

    return roll # we want roll back


#getting a valid input

while True: #we have this because we want to make sure it is actually a number and within range
    players = input("Enter the numbers of players(2-4): ")#ask for player input
    if players.isdigit(): #this is how we can check if it is an acutal whole number
        players = int(players) #when we actual input an integer it is a string so we will then make it an integer
        if 2 <= players <= 4: #this is what we want it inbetween
            break #this means if 2<= players <= 4 is valid we stop and move on
        else:
            print("Must be between 2-4 players.")#if top isn't valid it will say this.
    else:
        print("Invalid, Try again")#right here we will ask them to put it again


# getting the scores

max_score = 50 # set the max score
player_scores = [0 for _ in range(players)]#leave it as empty so we can append to it
# explaining what the inside for the list is so basically list comprehension it basically puts a 0 inside the list for the amount of "players" we have.

#now we are doing the player turns
while max(player_scores) < max_score: # this means the maximum of our players scores has to be below the max score which is 50 it will basically keep going and will stop once it reaches or exceeds 50
    for player_whoever in range(players):#player_whoever represents all the player, and this entire forloop simulates one entire person turns
        print("\nPlayer", player_whoever + 1, "turn has just started!")#this so they know the turn has officialy started
        print("Your total score is:", player_scores[player_whoever], "\n")#tells them their score
        current_score = 0 #initiate their score at 0 
  
        while True:#This happens for each player    
            should_roll = input("Would you like to roll(yes): ") #ask the people if they want to roll obviously yes
            if should_roll.lower() != "yes": #reason why we did lower was incase they add a capital it should always be yes. If it doesn't equal yes then leavr
                break #if it doesn't equal yes then bruh leave
    
            value = roll() #start their roll by going into roll function
            if value == 1:#if the person runs a one then it will print undereath
                print("You rolled a 1! Turn done!")
                current_score = 0 # bring this here so they know the current score is still 0
                break #add a break becasue once they spin then their turn is done
            else:
                current_score += value#this will add to their current score
                print("You rolled a:", value)
    
            print("Your score is:", current_score)

        player_scores[player_whoever] += current_score #so basically the current score will be added to the index
        print("Your total score is:", player_scores[player_whoever])

#finding the maxiumum score to find out who won
max_score = max(player_scores) #take the max score of all the player scores
winning_person = player_scores.index(max_score)#find which index has the highest score
print("Player number", winning_person + 1, "is the winner with a score of:", max_score) # we are adding 1 because an index starts at 0 so we have to add one to make it 1-4 and not 0-3


#game is offiically done this is the dice game


