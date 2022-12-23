#Name: Michelle T
#Teacher: Ms. Brace
#Course: ICS 3U0
#Date: July 27th, 2020

#Program: This program creates an app that teaches you about biometrics. There are two parts to this app.
#There are two parts: "learn" and "quiz". In "learn", the user will learn more about biometrics
#Through a variety of information pages. In "quiz", the user can take a multiple choice quiz that
#tests their learning on biometrics.

#Import modules pygame and random
import pygame
import random

#Initializes pygame and pygame fonts
pygame.init()
pygame.font.init()

#Sets up the surface called screen in pygame, identifying width of the surface, height of the surface
#and gives the pygame window a caption 
screenwidth = 800
screenheight = 550
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Biometrics App")

#Constants that contain the tuple values of several different colours used in the program
#Colours match the constant names
WHITE = (255,255,255)
RED = (225,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (50,150,255)

#Identifies several variables; appscreen is used to decide what state of the screen to display
#such as home screen, learn screen, quiz screen, score screen
#Page is used to decide which page to show in the learn screeen
#Score represents the score that the user obtains on the quiz
appscreen = 0
page = 0
score = 0

#Represents the index of the answer that the user selected for a question on the quiz
#Set to -1, meaning at first nothing is selected
selectedIndex = -1

#Identifies a list of positions for the multiple choice boxes and answers
positions = [(60, 270), (270, 270), (60, 380), (270, 380)]

#Identifies the width and height of the multiple choice boxes
width = 200
height = 100

#Declares a function that identifies and returns the index of the answer the user clicked
def getSelectedIndex(mouseClickPosition):

    #For i in range lenth of the list positions
    #Variable position is equal to the index i of list positions
    #mouseClickPosition indicates the position of the mouse when clicked
    #Variable selected is True when it is within the parameters of a multiple choice box
    for i in range(len(positions)):
        position = positions[i]
        selected = position[0] < mouseClickPosition[0] < position[0]+width and position[1] < mouseClickPosition[1] < position[1]+height

        #Tests if selected is true and returns the index that is selected
        if selected:
            return i
    
    #If nothing is selected, return -1 
    return -1

#Create a class Question that bundles data related to the questions and answers of the multiple choice quiz
class Question:

    #Initializes attributes of the class Question, including a question that will be displayed,
    #the answers that will be displayed, and the index of the correct answer
    def __init__(self, question, answers, correctAnswerIndex):
        self.question = question
        self.answers = answers
        self.correctAnswerIndex = correctAnswerIndex

#Identifies variable that represents the index of the current questions, which is 0 right now (the first question)
currentQuestionIndex = 0

#Creates a list of questions, answers, and the correct answer index using the class Question
questions = [\
    Question("Human characteristics that can be used to digitally identify people", ["ergonomics", "scanners", "biometrics", "scientometrics"], 2),\
    Question("Unique human characteristics and features recorded in a biometric system", ["scanners", "identifiers", "signatures", "behaviours"], 1),\
    Question("Immutable and device independent identifiers", ["morphological","biological","physical","behavioural"],2),\
    Question("How we interact with technology in different ways",["engagement patterns","navigation patterns","typing patterns","signatures"],0),\
    Question("Second most common type of identification, usually used with a camera",["facial contortion","iris recognition","voice recognition","facial recognition"],3),\
    Question("This biological identifier is commonly used in law enforcement",["signatures","fingerprints","DNA","facial recognition"],2),\
    Question("Identifiers that are structures of the body",["morphological","biological","facial recognition","palm vein reading"],0),\
    Question("Identifiers based on patterns unique to the individual",["physical","morphological","biological","behavioural"],3),\
    Question("Styles of this identifier include speed, length, impact",["typing patterns","DNA","signatures","navigation patterns"],0),\
    Question("Most common type of biometric identification, usually used with touch",["signatures","fingerprints","facial recognition","navigation patterns"],1),\
    Question("Includes mouse and finger movements",["fingerprints","typing patterns","navigation patterns","physical movements"],2),\
    Question("Often used to authenticate fincancial transactions",["DNA","fingerprints","facial recognition","signatures"],3),\
    Question("The way someone walks or sits",["physical movements","navigation patterns","behavioural","stretches"],0)\
    ]

#Declares a function that consumes a bundle of data in the questions list and draws a page of 
#the multiple choice quiz when called using several other functions
def drawQuestion(question) :

    #Calls the function that draws the current question onto the screen
    #Calls the function that draws the current answers onto the screen
    #Calls the function that draws wrong or correct onto the screen according to the 
    #selected index and the correct index
    drawQuestionText(question.question, currentQuestionIndex)
    drawAnswers(question.answers)
    drawResult(selectedIndex, question.correctAnswerIndex)

#Declares a function that consumes a selected index and the correct index and draws
#correect or wrong onto the screen according to the selected index
def drawResult(selected, correctIndex):

    #Identifies variable answerfont that sets the font of the following strings
    #Correct renders "Correct!" in the answerfont in green
    #Wrong renders "Wrong!" in the answerfont in red
    answerfont = pygame.font.SysFont("stencil", 50)
    correct = answerfont.render("Correct!",1,(GREEN))
    wrong = answerfont.render("Wrong!",1,(RED))

    #Tests if selected is equal to -1, which means nothing is selected, and returns nothing
    #Tests if selected is equal to the correct index and draws correct if True
    #Otherwise, draws wrong onto the screen
    if selected == -1:
        return
    if selected == correctIndex:
        screen.blit(correct, (520,330))
    else:
        screen.blit(wrong, (520,330))

#Declares a function that consumes a question text and a question number
#and draws the question text and number onto the screen
def drawQuestionText(qtext,num):

    #Identifies a variable that sets the font of the questions
    #Renders the question and the question number in questionfont in white
    #Draws the question onto the screen
    questionfont = pygame.font.SysFont("centaur",19,True)
    question = questionfont.render("Question " + str(num+1) + ": " + qtext, 1, (WHITE))
    screen.blit(question, (60, 200))

#Declares a function that consumes a list of answers and draws individual answers
def drawAnswers(answers) :

    #For i in range of the length of the answers list, call the function drawAnswer using the index i of the variables identified
    for i in range(len(answers)):
        drawAnswer(answers[i], positions[i], selectedIndex == i)

#Declares a function that consumes an answer, a position, and a selected index and draws
#a rectangle and an answer of the multiple choice quiz
def drawAnswer(answer, position, selected) :

    #Identifies local variable borderColour that represents the colour of rectangles and the text
    borderColour = WHITE

    #Identifies local variable that represents the current mouse position
    mouse = pygame.mouse.get_pos()

    #Identifies a variable that is True if the mouse position is within a multiple choice box
    hovered = position[0] < mouse[0] < position[0]+width and position[1] < mouse[1] < position[1]+height 
    
    #If hovered is true, the colour will be set to red, if it is selected, the colour will be blue,
    #and anything else is white
    if hovered:
        borderColour = RED
    else:
        if selected:
            borderColour = BLUE
        else:
            borderColour = WHITE

    #Identifies a variable that sets the font for the following answers that will be drawn
    #Identifies a variable that represents the answer rendered in buttonfont in borderColour
    #Draws the answer onto the screen at the specified position in the parameters
    #Draws a rectangle in the colour represented by borderColour onto the screen at the specified position
    buttonfont = pygame.font.SysFont("centaur", 25)
    displayanswer = buttonfont.render(answer, 1, borderColour)
    screen.blit(displayanswer, (position[0] + 10,position[1] + int(height/3)))
    pygame.draw.rect(screen,borderColour,(position[0],position[1], width,height),3)

#Declares a function that displays the home screen    
def display1():

    #Fills the screen with black 
    screen.fill(BLACK)

    #Identifies variable that represents the background picture loaded and draws it onto the screen
    bg = pygame.image.load("bg.jpg").convert()
    screen.blit(bg,(80,50))

    #Calls functions title, subtitle, buttons, and instructiontext that makes up the main page
    title()
    subtitle()
    button(int(screenwidth/4+50), 350, 100, 5, "Learn", 30, 0,1)
    button(int(screenwidth/4*3-50), 350, 100, 5, "Quiz", 30, 1,1)
    instructiontext("Click \"LEARN\" to learn more about biometrics. \
Click \"QUIZ\" to test your knowledge on biometrics in a quiz game.")

    #Identifies global variables score, page, selectedIndex, and currentQuestionIndex to set them back to their original values
    #Must use global when changing a global variable inside a function
    global score 
    score = 0
    global page
    page = 0
    global selectedIndex
    selectedIndex = -1
    global currentQuestionIndex
    currentQuestionIndex = 0

#Declares a function title that draws a title    
def title():

    #Identifies the font, renders the text, draws the text
    titlefont = pygame.font.SysFont("stencil",100)
    title = titlefont.render("BIOMETRICS", 1, (WHITE))
    screen.blit(title, (int(screenwidth/2) - int(title.get_width()/2),85))

#Declares a function subtitle that draws a subtitle
def subtitle():

    #Identifies the font, renders the text, draws the text
    subtitlefont = pygame.font.SysFont("centaur",27,True)
    subtitle = subtitlefont.render("Digital Identification Through Human Characteristics", 1, (240,240,240))
    screen.blit(subtitle, (int(screenwidth/2) - int(subtitle.get_width()/2),190))

#Declares a function instructiontext that consumes a string and draws instructions as text
def instructiontext(string):

    #Identifies the font, renders the text, draws the text
    instructionfont = pygame.font.SysFont("centaur",17)
    instruction = instructionfont.render(string, 1, (WHITE))
    screen.blit(instruction, (int(screenwidth/2) - int(instruction.get_width()/2),525))

#Declares a function button that consumes several parameters and draws a button with images and text
def button(x,y,radius,width,text,size,num,scalenum):
    
    #Draws a white circle using parameters identified
    pygame.draw.circle(screen, (WHITE), (x,y), radius, width)

    #Identifies a list of image names and a list of tuples that represent scales of images
    #Identifies a list of tuples that represent the positions of the images
    load_image_list = ["Learn Icon.png","Quiz Icon.png","home2.png","Forward arrow.png","Backward arrow.png"]
    scale_list = [(125,125),(25,25)]
    image_positions = [(x-63,y-62),(x-64,y-62),(x-13,y-15),(x-11,y-13),(x-13,y-13)]
    
    #Loads the image in index num in the list, converts it to alpha to preserve transparency
    #Scales the image according to index scalenum-1 in the list of positions 
    #Draws the image onto the screen at the position of the index num in positions
    image = pygame.image.load(load_image_list[num]).convert_alpha()
    image = pygame.transform.scale(image,scale_list[scalenum-1])
    screen.blit(image,image_positions[num])
    
    #Identifies the font, renders the text, draws the text
    buttonfont = pygame.font.SysFont("stencil", size)
    buttontext = buttonfont.render(text, 1, (WHITE))
    screen.blit(buttontext, (int(x - buttontext.get_width()/2),int(y+radius+radius/5)))

    #Identifies variable that represents the values of the current position of the mouse
    mouse = pygame.mouse.get_pos()
    
    #Checks if the mouse position is within the paramters of a button and its corresponding text
    if x-radius < mouse[0] < x+radius and y-radius < mouse[1] < y+radius+radius/5+buttontext.get_height():
        
        #Overlays a red circle and red text
        pygame.draw.circle(screen, (RED), (x,y), radius, width)
        buttontext = buttonfont.render(text, 1, (RED))
        screen.blit(buttontext, (int(x - buttontext.get_width()/2),int(y+radius+radius/5)))

        #Loads a list of red congruent images and overlays the white images
        load_image_list_red = ["Learn Red.png","Quiz Red.png","home_red.png","Forward red.png","Backward red.png"]
        image_red = pygame.image.load(load_image_list_red[num]).convert_alpha()
        image_red = pygame.transform.scale(image_red,scale_list[scalenum-1])
        screen.blit(image_red,image_positions[num])

#Declares a function that displays the learning screen           
def display2():

    #Fills screen black
    screen.fill(BLACK)

    #Calls function shapes and calls functions in learning page according to index page
    shapes()
    learningpages[page]()

    #If page is not equal to 0 (first page), display a back button by calling function button
    #If page is not equal to 6 (last page), display a next button
    #Display a home button
    #Display some instruction text by calling function instructiontext
    if page != 0:
        button(40,500,20,2,"BACK",20,4,2)
    if page != 6:
        button(760,500,20,2,"NEXT",20,3,2)
    button(760,30,20,2,"HOME",20,2,2)
    instructiontext("Navigate through the learning pages \
with the \"NEXT\" or \"BACK\" buttons.")

#The following 7 functions displays different pages of information and images using the functions images, topics, and texts
def page1():
    images(0)
    topics("BIOMETRICS")
    texts("Human characteristics that can be used", 200)
    texts("to digitally identify people",230)
    texts("Systems and devices measure and analyze people's attributes", 280)
    texts("Used to identify, authenticate, authorize, and verify identity", 330)
    texts("Can replace or augment password systems", 380)

def page2():
    images(1)
    topics("IDENTIFIERS")
    texts("Related to human characteristics and features",200)
    texts("used and recorded in a biometric system",230)
    texts("Usually unique to the individual",280)
    texts("Two types: PHYSICAL and BEHAVIOURAL", 330)

def page3():
    images(2)
    topics("PHYSICAL")
    texts("Immutable and device-independent identifiers",200)
    texts("Biological: traits at a genetic/molecular level",250)
    texts("such as DNA, blood, fluid samples",280)
    texts("Morphological: structures of the human body, such as",330)
    texts("fingerprints and eyes",360)

def page4():
    images(3)
    topics("PHYSICAL")
    texts("DNA: used primarily in law enforcement",200)
    texts("to identify suspects",230)
    texts("Fingerprints: most common type of biometric identification",280)
    texts("usually used with any device that can be touched",310)
    texts("Facial recognition: second most common type",360)
    texts("usually used with devices equipped with a camera",390)

def page5():
    images(4)
    topics("PHYSICAL")
    texts("Voice: commonly used by voice-based",200)
    texts("digital assistants and telephone-based",230)
    texts("service portals using voice recognition",260)
    texts("Other: hand geometry recognition, ear recognition, ",310)
    texts("palm prints, finger and palm vein patterns, structures of the",340)
    texts("eye (iris or retina), body odours, facial contortion",370)

def page6():
    images(5)
    topics("BEHAVIOURAL")
    texts("Based on patterns unique to the individual",200)
    texts("Signatures: often used to authorize",250)
    texts("financial transactions",280)
    texts("Typing patterns: speed, length to go from a letter to another,",330)
    texts("degree of impact on the keyboard",360)
    texts("Physical movements: the way someone walks, sits, etc.",410)
    
def page7():
    images(6)
    topics("BEHAVIOURAL")
    texts("Navigation patterns: mouse movements",200)
    texts("and finger movements on trackpads",230)
    texts("or touch-sensitive screens",260)
    texts("Engagement patterns: how we engage with technology",310)
    texts("such as how we open and use apps, how low our battery gets,",340)
    texts("locations and times of day we use our devices, how we",370)
    texts("navigate websites, how much we tilt our phone screens,",400)
    texts("how often we check social media, etc.",430)

#Identifies a list of functions that are all pages in the learning screen
learningpages = [page1,page2,page3,page4,page5,page6,page7]

#Declares a function that consumes a string and draws it onto the screen
def topics(string):

    #Identifies the font, renders the text, draws the text
    topicfont = pygame.font.SysFont("stencil",50)
    topic = topicfont.render(string, 1, (WHITE))
    screen.blit(topic, (60,100))

#Declares a function that consumes a string and a y position and draws it onto the screen
def texts(string, y):

    #Identifies the font, renders the text, draws the text
    textfont = pygame.font.SysFont("centaur",30)
    text = textfont.render(string, 1, (WHITE))
    screen.blit(text, (80, y))

#Declares a function that draws shapes
def shapes():

    #Draws a white rectangle and a white circle
    pygame.draw.rect(screen,(WHITE),(int(screenwidth/2) - 340, 170, 680,300),3)
    pygame.draw.circle(screen,(WHITE),(660,165),100)

##Declares a function that consumes a string and draws it onto the screen
def images(num):

    #Loads several images and assigns them to variables
    biometrics = pygame.image.load("biometrics.png").convert_alpha()
    fingerprint = pygame.image.load("page 2.png").convert_alpha()
    eye = pygame.image.load("page 3.png").convert_alpha()
    dna = pygame.image.load("page 4.png").convert_alpha()
    voice = pygame.image.load("page 5.png").convert_alpha()
    signature = pygame.image.load("page 6.png").convert_alpha()
    mouse = pygame.image.load("page 7.png").convert_alpha()

    #Put the images in a list of images
    images = [biometrics,fingerprint,eye,dna,voice,signature,mouse]

    #Scales and draws the image and index num in the list of images
    image = pygame.transform.scale(images[num], (160,160))
    screen.blit(image,(578,87))

#Declares a function that draws the multiple choice quiz screen
def display3():

    #Fills the screen black
    #Calls the function topics and draws "MULTIPLE CHOICE QUIZ"
    screen.fill(BLACK)
    topics("MULTIPLE CHOICE QUIZ")

    #Draws a next button and a home button using function button
    button(760,500,20,2,"NEXT",20,3,2)
    button(760,30,20,2,"HOME",20,2,2)

    #Draws the current bundle of question and answer data by calling the function drawQuestion
    drawQuestion(questions[currentQuestionIndex])

    #Draws some instruction text onto the screen
    instructiontext("Click a box to choose an answer. Click \"NEXT\" to proceed to the next question.")

#Declares a function that returns True if the mouse clicks within the next button
def nextQuestionButtonClicked(mousePos):

    #Identifies a variable click that is True if the mouse position is within the parameters of the next button
    click = 710 < mousePos[0] < 780 and 480 < mousePos[1] < 540

    #If click is True, return true, otherwise return False
    if click:
        return True
    return False

#Declares a function that goes to the draws the next bundle of question and answer data onto the multiple chocie screen
def goToNextQuestion():

    #Global variables score, questions, currentQuestionIndex, selectedIndex, appscreen
    global score
    global questions 
    global currentQuestionIndex
    global selectedIndex
    global appscreen

    #If the correct answer index is equal to the selected index, then add one to the score
    #If the index of the current question and answer data has not yet reached the end, reset values of 
    #the selected index and adds one to the current question index, which moves on to the next bundle of question and answer data
    #If the current question index is the last one in the list of questions data, set appscreen to 3
    if questions[currentQuestionIndex].correctAnswerIndex == selectedIndex:
        score = score + 1
    if currentQuestionIndex != len(questions) - 1:
        currentQuestionIndex = currentQuestionIndex + 1
        selectedIndex = -1
    elif currentQuestionIndex == len(questions) - 1:
        appscreen = 3

#Declares a function that draws the score screen
def display4():

    #Fills the screen black
    screen.fill(BLACK)

    #Draws a home button
    button(760,30,20,2,"HOME",20,2,2)

    #Global variable score
    global score

    #Identifies the font, renders the score in a score/total questions format, draws the text onto the screen
    scorefont = pygame.font.SysFont("stencil", 50)
    scoredisplay = scorefont.render("Your score: " + str(score) + "/" + str(len(questions)),1,(WHITE))
    return screen.blit(scoredisplay,(int(screenwidth/2)-100,int(screenheight/2)))

#Identifies a list of functions that display the four different screens
displayscreens = [display1, display2, display3, display4]

#Identifies run as True, and while run is true the main program runs
run = True
while run:

    #For each event that happens in a list of events in pygame
    for event in pygame.event.get():

        #If the event is quit, which is pressing the red X on the top right corner, run is set to false which quits the loop
        if event.type == pygame.QUIT:
            run = False

        #If the event is that the left mouse button has been pressed 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #If the value of appscreen is equal to 2
            if appscreen == 2:
                #If the selected index is equal to -1, set selected index to the result of the function getSelectedIndex
                #If the function nextQuestionButtonClicked is True, call the function goToNextQuestion
                if selectedIndex == -1:
                    selectedIndex = getSelectedIndex(pygame.mouse.get_pos())
                if nextQuestionButtonClicked(pygame.mouse.get_pos()):
                    goToNextQuestion()

            #Identifies variable mouse that represents the current position of the mouse
            mouse = pygame.mouse.get_pos()
            #If appscreen is equal to 0
            if appscreen == 0:
                #If the y position of the mouse is within the y parameters of the learn and quiz buttons
                if 250 < mouse[1] < 500:
                    #If the x position of the mouse is within the x parameters of the learn button, set appscreen to 1
                    if 150 < mouse[0] < 450:
                        appscreen = 1
                    #Otherwise if the x position of the mouse is within the x parameters of the quiz button, set appscreen to 2
                    elif 450 < mouse[0] < 650:
                        appscreen = 2
            #Otherwise if appscreen is equal to 1
            elif appscreen == 1:
                #If the position of the mouse is within the parameters of the home button, set appscreen to 0
                if 710 < mouse[0] < 780 and 10 < mouse[1] < 70:
                    appscreen = 0
                #If the position of the mouse is within the parameters of the back button
                elif 20 < mouse[0] < 60 and 480 < mouse[1] < 540:
                    #If page is not 0, set value of page to page - 1
                    if page != 0:
                        page = page - 1
                #If the position of the mouse is within the parameters of the next button
                elif 710 < mouse[0] < 780 and 480 < mouse[1] < 540:
                    #If page is not 6, set value of page to page + 1
                    if page != 6:
                        page = page + 1
            #Otherwise if appscreen is equal to 2 or 3
            elif appscreen == 2 or appscreen == 3:
                #If the position of the mouse is within the parameters of the home button, set appscreen to 0
                if 710 < mouse[0] < 780 and 10 < mouse[1] < 70:
                    appscreen = 0

    #Display the screen according to the index of appscreen
    displayscreens[appscreen]()

    #Update the pygame display window    
    pygame.display.update()

#Quits pygame once the main loop stops executing
pygame.quit()


