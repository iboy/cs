#Importing the necessary libraries into python. 
import pygame
import random
import time

locationx = [121, 180, 242, 302]
locationy = [557, 558, 560, 560]

def DisplayColouredPeg(num, locationx, locationy):
    if num == 1:
        pygame.draw.circle(gameDisplay, blue, (locationx, locationy), 19, 0)
        pygame.display.update()
    elif num == 2:
        pygame.draw.circle(gameDisplay, orange, (locationx, locationy), 19, 0)
        pygame.display.update()
    elif num == 3:
        pygame.draw.circle(gameDisplay, pink, (locationx, locationy), 19, 0)
        pygame.display.update()
    elif num ==4:
        pygame.draw.circle(gameDisplay, yellow , (locationx, locationy), 19, 0)
        pygame.display.update()
    elif num ==5:
        pygame.draw.circle(gameDisplay, black , (locationx, locationy), 19, 0)
        pygame.display.update()
    else:
        pygame.draw.circle(gameDisplay, purple, (locationx, locationy), 19, 0)
        pygame.display.update()

#Initialising the game screen and captioning it as Master Mind
pygame.init()
gameDisplay = pygame.display.set_mode((600, 637))
pygame.display.set_caption('Mastermind.')

#Setting the screen to a colour to display a welcome message and updating the screen.
colour = (145, 184, 255)
gameDisplay.fill(colour)
pygame.display.flip()
number = 0
#Creating A function to display a welcome message.
def WelcomeMessage():
#Setting the font, size and text as well as the positioning of the text. 
    Welcome_font = pygame.font.Font('freesansbold.ttf',36)
    Welcome_text = Welcome_font.render("Welcome to MasterMind, ",True,(0,0,0))
    Welcome_text1 = Welcome_font.render("I hope you enjoy the game!",True,(0,0,0))
    gameDisplay.blit(Welcome_text,((70), (317)))
    gameDisplay.blit(Welcome_text1,((50), (357)))
    pygame.display.update()
#Using the time module setting how long the message displays for and then resetting the screen.
    time.sleep(4)
    gameDisplay.fill(colour)
    pygame.display.flip()

#Creating A function to display a congratulations message.
def CongratsMessage():
#Setting the font, size and text as well as the positioning of the text.
    colour = (145, 184, 255)
    gameDisplay.fill(colour)
    pygame.display.flip()
    Welcome_font = pygame.font.Font('freesansbold.ttf',36)
    Welcome_text = Welcome_font.render("Congratulations!",True,(0,0,0))
    gameDisplay.blit(Welcome_text,((140), (317)))
    pygame.display.update()
#Using the time module setting how long the message displays for and then resetting the screen.
    time.sleep(4)
    gameDisplay.fill(colour)
    pygame.display.flip()


def GoodAttemptMessage():
#Setting the font, size and text as well as the positioning of the text.
    colour = (145, 184, 255)
    gameDisplay.fill(colour)
    pygame.display.flip()
    Welcome_font = pygame.font.Font('freesansbold.ttf',36)
    Welcome_text = Welcome_font.render("Good Attempt!",True,(0,0,0))
    gameDisplay.blit(Welcome_text,((140), (317)))
    pygame.display.update()
#Using the time module setting how long the message displays for and then resetting the screen.
    time.sleep(4)
    gameDisplay.fill(colour)
    pygame.display.flip()

WelcomeMessage()

#Importing the edited graphic of the Mastermind board and updating the screen.
image = pygame.image.load('MasterMindBoard.jpg')
gameDisplay.blit(image, (0, 0))
pygame.display.update()

#Generating the 4 ball sequence.
#Setting Colours for the future
blue = (112, 206, 226)
orange = (242, 101, 36)
pink = (242, 110, 113)
purple = (114, 61, 151)
red =(205,92,92)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

#Setting up an array to store the answer
Answer = []

#Setting up num of white and red pegs to 0.
num_white_pegs = 0
num_red_pegs = 0

#Creating four values for the four pegs
for j in range(4):
    num = random.randint(1, 6)
    if num == 1:
        num = blue
    elif num ==2:
        num = orange
    elif num ==3:
        num = pink
    elif num ==4:
        num = yellow
    elif num ==5:
        num = black
    else:
        num = purple
    Answer.append(num)
    

#Drawing circles onto the game board.
#X and Y co-ordinates of the peg holes
Xco_ords1 = [188,228,268,308,186,226,266,306,186,226,266,306,179,219,259,299,170,214,258,302,170,214,258,302,165,211,257,303,155,205,255,305,147,200,253,306,140,194,248,302,137,192,247,302,130,187,244,301]
Yco_ords1 = [44,69,94,119,148,177,215,251,291,337,385,436]

#Setting the counter to 0
counter = 0
correct = False
#Function needed to print the circles to the screen in the right position. Yellow as the default colour. 
def printRow(counter):
    circles = counter * 4
    circle_rect1 = pygame.draw.circle(gameDisplay, yellow, (Xco_ords1[circles], Yco_ords1[counter]),10, 0)
    x1 = Xco_ords1[circles]
    circles += 1
    circle_rect2 = pygame.draw.circle(gameDisplay, yellow, (Xco_ords1[circles], Yco_ords1[counter]),10, 0)
    x2 = Xco_ords1[circles]
    circles += 1
    circle_rect3 = pygame.draw.circle(gameDisplay, yellow, (Xco_ords1[circles], Yco_ords1[counter]),10, 0)
    x3 = Xco_ords1[circles]
    circles += 1
    circle_rect4 = pygame.draw.circle(gameDisplay, yellow, (Xco_ords1[circles], Yco_ords1[counter]),10, 0)
    x4 = Xco_ords1[circles]
    circles += 1
    y1 = Yco_ords1[counter]
    pygame.display.update()
    return circle_rect1,x1,circle_rect2,x2,circle_rect3,x3,circle_rect4,x4,y1
    
#Creating a loop of colours for the button
def getcolour(click):
    colour = [yellow, blue, orange, pink, purple,black]
    length = len(colour)
    if click>(length-1):
        click = 0
    col = colour[click]
    return click, col

#Function to establish if the answer is correct.
def checkAnswer(Answer, Guess, counter):
    used =[False,False,False,False]
#Setting the necessary variables to 0.
    num_white_pegs = 0
    num_red_pegs = 0
    ArrayCounter = 0
#Checking if they are identical.
    if Answer[0] == Guess[0] and Answer[1]==Guess[1] and Answer[2]==Guess[2] and Answer[3] == Guess[3]:
        correct = True
        return correct
#Beginning to calculate the pegs if they are not identical.
    else:
        for w in range(4):
            if Answer[w] == Guess[w]:
                num_red_pegs += 1
                used[w] = True
        return num_red_pegs,used
                

#Drawing the submit button onto the screen.    
circle_rect5 = pygame.draw.circle(gameDisplay, black, (450,500),20, 0)
pygame.display.update()

#Making it so that when a circle is clicked it changes colour.
circle_rect1,x1, circle_rect2,x2, circle_rect3,x3, circle_rect4,x4,y1 = printRow(counter)
'''Guess = []
click1 = 0
click2 = 0
click3 = 0
click4 = 0
colour1 = yellow
colour2 = yellow
colour3 = yellow
colour4 = yellow
'''
#Displaying Red Pegs:
def display_red_pegs(checkanswer,x4, y1):
    x4 = x4+2
    num_red_pegs = checkanswer
    if num_red_pegs ==1:
        pygame.draw.circle(gameDisplay, red, ((x4+27), (y1-3)),6,0)
        pygame.display.update()
    elif num_red_pegs ==2:
        pygame.draw.circle(gameDisplay, red, ((x4+27), (y1-3)),6,0)
        x4 += 10
        pygame.draw.circle(gameDisplay, red, ((x4+(27+9)), (y1-3)),6,0)
        pygame.display.update()            
    elif num_red_pegs==3:
        pygame.draw.circle(gameDisplay, red, ((x4+27), (y1-3)),6,0)
        x4 += 10
        pygame.draw.circle(gameDisplay, red, ((x4+(27+9)), (y1-3)),6,0)
        x4 = x4 -10
        pygame.draw.circle(gameDisplay, red, ((x4+27), (y1+10)),6,0)
        pygame.display.update()

#Calculating the number of white pegs needed.
def displaying_white_pegs(used, Answer, Guess):
    num_white_pegs = 0
    for z in range(4):
        for e in range(4):
            if not used[e] and Guess[e] == Answer[z]:
                num_white_pegs += 1
                used[e] = True
    return num_white_pegs
print(Answer)
def display_white_pegs(num_white_pegs,x4, y1):
    x4 = x4 + 2
    num_red_pegs = checkanswer
    print(num_red_pegs)
    if num_white_pegs ==1:
        x4+=10
        pygame.draw.circle(gameDisplay, white, ((x4+27+9), (y1+10)),6,0)
        pygame.display.update()
    elif num_white_pegs ==2:
        pygame.draw.circle(gameDisplay, white, ((x4+27), (y1+10)),6,0)
        x4 += 10
        pygame.draw.circle(gameDisplay, white, ((x4+(27+9)), (y1+10)),6,0)
        pygame.display.update()            
    elif num_white_pegs ==3:
        pygame.draw.circle(gameDisplay, white, ((x4+(9+37)), (y1-3)),6,0)
        pygame.draw.circle(gameDisplay, white, ((x4+(27)), (y1+10)),6,0)
        x4 = x4 +10
        pygame.draw.circle(gameDisplay, white, ((x4+(27+9)), (y1+10)),6,0)
        pygame.display.update()
    elif num_white_pegs ==4:
        pygame.draw.circle(gameDisplay, white, ((x4+27), (y1-3)),6,0)
        x4 += 10
        pygame.draw.circle(gameDisplay, white, ((x4+(27+9)), (y1-3)),6,0)
        x4 = x4 -10
        pygame.draw.circle(gameDisplay, white, ((x4+27), (y1+10)),6,0)
        x4 = x4 +10
        pygame.draw.circle(gameDisplay, white, ((x4+(27+9)), (y1+10)),6,0)
        pygame.display.update()
    



def read_scores(filename, splitter=','):
    """reads scores and names from a file, and returns a list of each"""
    scores = []
    names = []

    with open(filename) as f:
        for score in f:
            score, name = score.strip().split(splitter)
            scores.append(int(score))
            names.append(name)
    return scores, names

def sort_scores(scores, names, reverse_bool=True):
    """sorts the scores from greatest to least and returns in a list of tuples format"""
    return sorted(zip(scores,names))

def print_scores(score_list, splitter=' ', top_amount=5):
    """prints the number of leaderboard scores stated"""
    for score_tuple in score_list[:top_amount]:
        print(splitter.join(map(str, score_tuple)))
    
                
    

#Creating the code for the counter = 0 instance to make it so the user can enter at least 1 guess.

for c in range(0,12):
    Guess = []
    click1 = 0
    click2 = 0
    click3 = 0
    click4 = 0
    colour1 = yellow
    colour2 = yellow
    colour3 = yellow
    colour4 = yellow

    circle_rect1,x1, circle_rect2,x2, circle_rect3,x3, circle_rect4,x4,y1 = printRow(counter)
    while counter ==c:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if circle_rect1.collidepoint(x, y):
                    click1+=1
                    click1, colour1 = getcolour(click1)
                    pygame.draw.circle(gameDisplay, colour1, (x1, y1),10, 0)
                    pygame.display.update()
                
                elif circle_rect2.collidepoint(x, y):
                    click2+=1
                    click2, colour2 = getcolour(click2)
                    pygame.draw.circle(gameDisplay, colour2, (x2, y1),10, 0)
                    pygame.display.update()
                elif circle_rect3.collidepoint(x, y):
                    click3+=1
                    click3, colour3 = getcolour(click3)
                    pygame.draw.circle(gameDisplay, colour3, (x3, y1),10, 0)
                    pygame.display.update()
                elif circle_rect4.collidepoint(x, y):
                    click4+=1
                    click4, colour4 = getcolour(click4)
                    pygame.draw.circle(gameDisplay, colour4, (x4, y1),10, 0)
                    pygame.display.update()
                elif circle_rect5.collidepoint(x,y):
                    Guess = [colour1, colour2, colour3, colour4]
                    print(Guess)
                    counter +=1
                    next 

              
    try:
        checkanswer,used = checkAnswer(Answer, Guess, counter)
    except:
        for h in range(4):
            num =Answer[(h-1)]
            if num == yellow:
                num  = 4
            elif num == orange:
                num =2
            elif num == pink:
                num =3
            elif num ==purple:
                num =6
            elif num == black:
                num =5
            elif num == blue:
                num = 1
            DisplayColouredPeg(num, locationx[(h - 1)], locationy[(h - 1)])
            CongratsMessage()
            number = number + 12
            name = str(input("Please enter your name for the leaderboard"))
            score = counter
            with open ("Leaderboard.txt","a") as f:
                writeto = str(score) + "," + name +"\n"
                f.write(writeto)
                f.close()
            scores,names = read_scores("Leaderboard.txt")
            zips = sort_scores(scores,names)
            print_scores(zips)
            pygame.quit()
            
    display_red_pegs(checkanswer,x4,y1)
    num_white_pegs = displaying_white_pegs(used, Answer, Guess)
    display_white_pegs(num_white_pegs,x4,y1)
    pygame.display.update()
    



for h in range(4):
    num =Answer[(h-1)]
    if num == yellow:
        num  = 4
    elif num == orange:
        num =2
    elif num == pink:
        num =3
    elif num ==purple:
        num =6
    elif num == black:
        num =5
    elif num == blue:
        num = 1
    DisplayColouredPeg(num, locationx[(h - 1)], locationy[(h - 1)])
    
time.sleep(5)
GoodAttemptMessage()
pygame.quit()













