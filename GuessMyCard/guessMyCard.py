''' GUESS MY CARD GAME
    NAME: Sam Treadwell
    DATE: 10/19/2022
    Description of Project 3: Here the task is to write a program that chooses
    a card at random from the deck. This first function needs to choose the suit, 
    then the face value of the card. The user guesses a color, red or black, 
    and the card is revealed for the user to see. The system then prints if they
    guessed correctly or not
'''
import random

def getSuit():
    '''The objective of the getSuit function is to assign a random suit for the selected card'''
    suit = ['Diamonds', 'Spades', 'Hearts', 'Clubs'] # These are the possible suits
    choose = random.choice(suit) # Here we use 'random' to choose a suit
    return choose # Then the built-in function 'return' to store the random choice

def getValue():
    '''The objective of the getValue funciton is to assign a random value for the selected card'''
    value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # These are the possible values
    choose = random.choice(value) # Here we use 'random' to choose a value
    return choose # Then the built-in function 'return' to store the random choice

def printCard():
    '''The objective of getValue is to choose a random card from the deck of 52 possible cards'''
    value = getValue() # Here we call the getValue function
    suit = getSuit() # Here we call the getValue function
    return value, suit # We want to return both so the user can see what card they have

def main():
    '''Here, in the main function, we execute the entire program by pulling the other functions.
    The user is prompted to choose a color and the program then prints their card and tells the user 
    if their guess was the right color based on the suit'''
    color = str(input("Choose a color, either black or red: ")) # Prompts the user to choose a color
    value, suit = printCard() # The printCard function is called
    print(value, suit) # The printCard function prints for the user to see their card (value, suit)
    if suit == 'Clubs' or suit == 'Spades': # These parameters set the suit to the suitcolor 'black'
        suitcolor = 'black' # Clubs and Spades are black
    elif suit == 'Hearts' or suit == 'Diamonds': # These parameters set the suit to the suitcolor 'red'
        suitcolor = 'red' # Hearts and Diamonds are red
    if suitcolor == color: # If the suitcolor and the color the user input ARE the same...
        print("Your card is the same color") # Prints: "Your card is the same color" CORRECT!
    else:
        print("Your card is not the same color") # If the suitcolor and the color the user input ARE NOT the same...
                                                 # Prints: "Your card is not the same color" INCORRECT!
main()
