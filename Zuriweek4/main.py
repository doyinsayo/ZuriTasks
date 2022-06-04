# RPS - ROCK PAPER SCISSORS GAME

# CodeSkulptor runs Python programs in your browser.
https://py3.codeskulptor.org/#user305_WNFjIeQWMd3Qi6b_1.py
#Welcome to the Classical Rock-Paper-Scissors game Where Rock beats Scissors and 
#Scissors beats Paper and Paper beats Rock

import random
import simplegui


AI_SCORE = 0
HUMAN_SCORE = 0
AI_CHOICE = ""
HUMAN_CHOICE = ""

def choice_to_number(choice):
    # converts choice to number where the 
    # choices of Rock,Paper,Scissors are 0,1,2 respectively
    RPS_DICT = {'Rock':0,'Paper':1,'Scissors':2}
    return RPS_DICT[choice]

def number_to_choice(choice):
    # converts the number back to choice
    RPS_DICT = {0:'Rock',1:'Paper',2:'Scissors'}
    return RPS_DICT[number]  

def random_AI_choice():
    #generates random choices for the computer
    return random.choice(['Rock','Paper','Scissors'])

def choice_result(HUMAN_CHOICE,AI_CHOICE):
    #RETURNS THE RESULT OF WHO WINS
    global AI_SCORE
    global HUMAN_SCORE
    #increment the winner's score by 1 
    # if tie do not increment        

    human_number = choice_to_number(HUMAN_CHOICE)
    AI_number = choice_to_number(AI_CHOICE)
    
    if (human_number - AI_number) % 3 == 1:
        AI_SCORE += 1
        print(' AI wins !')

    elif human_number == AI_number:
        print('Tie !')

    else:
        HUMAN_SCORE += 1
        print(' You win !')


#functions to test the code
def test_choice_to_number():
    assert choice_to_number('Rock') == 0
    assert choice_to_number('Paper') == 1
    assert choice_to_number('Scissors') == 2

def test_number_to_choice():
    assert number_to_choice(0) == 'Rock'
    assert number_to_choice(1) == 'Paper'
    assert number_to_choice(2) == 'Scissors'

def test_all():
    test_choice_to_number()
    test_number_to_choice()     

# handler for Rock
def Rock():
    global HUMAN_CHOICE, AI_CHOICE
    global HUMAN_SCORE, AI_SCORE
    
    HUMAN_CHOICE = 'Rock'
    AI_CHOICE = random_AI_choice()
    choice_result(AI_CHOICE , HUMAN_CHOICE)

# handler for paper
def Paper():
    global HUMAN_CHOICE , AI_CHOICE
    global HUMAN_SCORE , AI_SCORE
    
    HUMAN_CHOICE = 'Paper'
    AI_CHOICE = random_AI_choice()
    choice_result(AI_CHOICE , HUMAN_CHOICE)


# Handler for Scissors
def Scissors():
    global HUMAN_CHOICE , AI_CHOICE
    global HUMAN_SCORE , AI_SCORE
    
    HUMAN_CHOICE = 'Scissors'
    AI_CHOICE = random_AI_choice()
    choice_result(AI_CHOICE , HUMAN_CHOICE)
    
 # Handler to draw on canvas
def draw(canvas):
    try:
        # Draw choices
        canvas.draw_text("PLAYER: " + HUMAN_CHOICE , [10,40], 48, "Green")
        canvas.draw_text("CPU: " + AI_CHOICE , [10,80], 48, "Red")
        
        # Draw scores
        canvas.draw_text("Player Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("CPU Score: " + str(AI_SCORE), [10,190], 30, "Red")
        
    except TypeError:
        pass
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", Rock)
    frame.add_button("Paper", Paper)
    frame.add_button("Scissors", Scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 
play_rps()
    