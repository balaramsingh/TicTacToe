import turtle               # the start part of the python program
import time
import math
from copy import deepcopy
from queue import PriorityQueue

# function returns an empty board , whenever it is called
# no input parameters
# output parameters
# var : ti -> A 3x3 zero Matrix ( 2-D Array ) 
def create_board():
    li = [0,0,0]
    ti = []
    ti.append(deepcopy(li))
    ti.append(deepcopy(li))
    ti.append(deepcopy(li))
    return ti
    
# initializing the game window 
wn = turtle.Screen()
wn.title("tictactoe game")  # naming our game window
wn.colormode(255)
wn.bgcolor((255,255,255))    # background of board is set to white 
wn.setup(width=650, height=700)  # dimensions of  window
global ValidMove
ValidMove = True
board = create_board()
State = True
move = 0
moves = 

# function to draw the grid on game window
# has no input or output parameters 
def drawBoard():
    drawer.pensize(5)
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100-200*i)
        drawer.pendown()
        drawer.forward(600)
    drawer.right(90)
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200*i,300)
        drawer.pendown()
        drawer.forward(600)
    num=1
    for i in range(3):
        for j in range(3):
            strin = ""
            drawer.penup()
            drawer.goto(-290 + j * 200,280 - i *200)
            drawer.pendown()
            drawer.write(num, font=("Arial",12))
            num += 1
    screen.update()
    
# function to draw X at given co-ordinates
# input parameters
# var : x and var : y , are the co-ordinates of required position respectively
def drawX(x,y):
    drawer.color("red")
    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()
    drawer.setheading(60)
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
        screen.update()

# function to draw O at given co-ordinates
# input parameters
# var : x and var : y , are the co-ordinates of required position respectively       
def drawO(x,y):
    drawer.color("blue")
    drawer.penup()
    drawer.goto(x,y+75)
    drawer.pendown()
    drawer.setheading(0)
    for i in range(180):
        drawer.forward((150*math.pi)/180)
        drawer.right(2)
    screen.update()

# function to draw O at given matrix position
# this function calls the drawO function to draw
# input parameters
# var : x and var : y , are the co-ordinates of required position respectively
def addO(row,column):
    global ValidMove
    if ValidMove == True :
        announcer.clear()
        if board[row][column] == 1 or board[row][column] == 2 :
            announcer.write("That spot is taken !!",font=("Arial",40))
        else :
            rowvalue = 0
            colvalue = 0
            if row == 0 :
                colvalue = 200
            elif row == 1 :
                colvalue = 0
            elif row == 2 :
                colvalue = -200
            if  column == 0 :
                rowvalue = -200 
            elif column == 1 :
                rowvalue = 0
            elif column == 2 :
                rowvalue = 200
            board[row][column] = 2
            drawO(rowvalue,colvalue)  
            ValidMove = False
    else :
        announcer.clear()
        announcer.write("Please wait for your Turn",font=("Arial",40))

# function to draw O at given matrix position
# this function calls the drawO function to draw
# input parameters
# var : x and var : y , are the co-ordinates of required position respectively
def addX(row,column):
    rowvalue = 0
    colvalue = 0
    if row == 0 :
        colvalue = 200
    elif row == 1 :
        colvalue = 0
    elif row == 2 :
        colvalue = -200
    if  column == 0 :
        rowvalue = -200 
    elif column == 1 :
        rowvalue = 0
    elif column == 2 :
        rowvalue = 200
    drawX(rowvalue,colvalue) 

# the intermediate functions to take the user input as numbers
def squareOne():
    addO(0,0)
def squareTwo():
    addO(0,1)
def squareThree():
    addO(0,2)
def squareFour():
    addO(1,0)
def squareFive():
    addO(1,1)
def squareSix():
    addO(1,2)
def squareSeven():
    addO(2,0)
def squareEight():
    addO(2,1)
def squareNine():
    addO(2,2)

# the functions below are used to reflect the user's choice in game
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i],str(i+1))
def deactivate():
    for i in range(9):
        screen.onkey(None,str(i+1))

functions = [ squareOne,squareTwo,squareThree,squareFour,squareFive,
                squareSix,squareSeven,squareEight,squareNine]
# part of main program which initializes various turtles
# part of MAIN , which has all the pens' initialization 
drawer = turtle.Turtle()
announcer = turtle.Turtle()
drawer.pensize(10)
drawer.ht()
drawer.color("black")
announcer.penup()
announcer.ht()
announcer.goto(-100,300)
announcer.color("black")

screen = turtle.Screen()
screen.tracer(0)

drawBoard()
activate(functions)
screen.listen()

from copy import copy,deepcopy
from random import randint

# the utility function hellps to say whether any tile is empty or not
# input parameters
# var : board -> the current state of game
# output parameters
# var : a boolean variable 
def anymoves(board):
    inp = deepcopy(board)
    for i in range(len(inp)):
        for j in range(len(inp)):
            if inp[i][j] == 0 :
                return True
    return False

# this set of functions calculate the heuristic of a given state
# h_utility returns heuristic based on seperate string patterns ; they have been customized after analyzing many cases
def h_utility(stri):
    if stri == '111' :
        return 100000
    elif stri == '112' or stri == '211' :
        return 3000
    elif stri == '121' :
        return 200
    elif stri == '212' :
        return 0
    elif stri == '221' or stri == '122' :
        return 7000
    elif stri == '222' :
        return -20000
    elif stri == '210' or stri == '012' :
        return 500
    elif stri == '201' or stri == '102' :
        return 100
    elif stri == '021' or stri == '120' :
        return -300
    elif stri == '220' or stri == '022' :
        return -1000
    elif stri == '202' :
        return -3000
    elif stri == '110' or stri == '011':
        return 1000
    elif stri == '101' :
        return 3000
    elif stri == '020' :
        return -20
    elif stri == '002' or stri == '200' :
        return -50
    elif stri == '001' or stri == '100' :
        return 750
    elif stri == '010' :
        return 500
    elif stri == '000' :
        return 0
    else :
        print(stri)
        return 0

def get_heuristic(board):
    inp = deepcopy(board)
    heu = 0
    # row checking
    for i in range(len(inp)):
        stri = ''
        stri = str(inp[i][0]) + str(inp[i][1]) + str(inp[i][2])
        heu = heu + h_utility(stri)
        
    # column checking
    for i in range(len(inp)):
        stri = ''
        stri = str(inp[0][i]) + str(inp[1][i]) + str(inp[2][i])
        heu = heu + h_utility(stri)
    # diagonal 1 checking
    stri = ''
    stri = str(inp[0][2]) + str(inp[1][1]) + str(inp[2][0])
    heu = heu + h_utility(stri)
    stri = ''
    stri = str(inp[0][0]) + str(inp[1][1]) + str(inp[2][2])
    heu = heu + h_utility(stri)
    return heu
def heuristic_(board):
    poss = possiblemoves(board,1)
    ans_pos = poss[0]
    max_heu = -1000
    for states in poss :
        heu = get_heuristic(states)
        if heu >= max_heu :
            max_heu = heu
            ans_pos = states
    return ans_pos
def analyse_game_state(inp):
    curr_state = deepcopy(inp)
    if len(curr_state) == 2 :
        curr_state = curr_state[1]
    # row wise checking
    if curr_state[0][0] == curr_state[0][1] and curr_state[0][0] == curr_state[0][2] :
        if curr_state[0][0] == 1 :
            return 4 #Computer wins
        elif curr_state[0][0] == 2 :
            return 5 #User Wins
        else :
            return 2 #Continue
    elif curr_state[1][0] == curr_state [1][1] and curr_state[1][0] == curr_state [1][2] :
        if curr_state[1][0] == 1 :
            return 4 #Computer wins
        elif curr_state[1][0] == 2 :
            return 5 #User Wins 
        else :
            return 2 #Continue       
    elif curr_state[2][0] == curr_state [2][1] and curr_state[2][0] == curr_state [2][2] :
        if curr_state[2][0] == 1 :
            return 4 #Computer wins
        elif curr_state[2][0] == 2 :
            return 5 #User Wins
        else :
            return 2 #Continue
    # column wise checking
    elif curr_state[0][0] == curr_state [1][0] and curr_state[0][0] == curr_state [2][0] :
        if curr_state[0][0] == 1 :
            return 4 #Computer wins
        elif curr_state[0][0] == 2 :
            return 5 #User Wins
        else :
            return 2 #Continue
    elif curr_state[0][1] == curr_state [1][1] and curr_state[0][1] == curr_state [2][1] :
        if curr_state[0][1] == 1 :
            return 4 #Computer wins
        elif curr_state[0][1] == 2 :
            return 5 #User Wins   
        else :
            return 2 #Continue     
    elif curr_state[0][2] == curr_state [1][2] and curr_state[0][2] == curr_state [2][2] :
        if curr_state[0][2] == 1 :
            return 4 #Computer wins
        elif curr_state[0][2] == 2 :
            return 5 #User Wins
        else :
            return 2 #Continue
    # diagonal checking
    elif curr_state[0][0] == curr_state[1][1] and curr_state[0][0] == curr_state[2][2]:
        if curr_state[0][0] == 1 :
            return 4 #Computer wins
        elif curr_state[0][0] == 2 :
            return 5 #User Wins
        else :
            return 2 #Continue
    elif curr_state[2][0] == curr_state[1][1] and curr_state[1][1] == curr_state[0][2]:
        if curr_state[2][0] == 1 :
            return 4 #Computer wins
        elif curr_state[2][0] == 2 :
            return 5 #User Wins
        else :
            return 2 #Continue
    elif moves >= 9:
        return 3 #Game Draw
    else :
        return 2 #Continue
def print_curr():
    global board
    if len(board) == 2 :
        board = board[1]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 :
                addX(i,j)
            elif board[i][j] == 2:
                addO(i,j)
    screen.update()
def print_message(val):
    announcer.clear()
    if val == 1 :
        announcer.write("User's Move",font=("Arial",20))
    elif val == 2 :
        announcer.write("Computer's Move",font=("Arial",20))
    elif val == 3 :
        announcer.write("YOU LOSE",font=("Arial",20))
        time.sleep(5)
        exit()
    elif val == 4 :
        announcer.write("YOU WIN",font=("Arial",20))
        time.sleep(5)
        exit()
    elif val == 5 :
        announcer.write("DRAW MATCH !!!",font=("Arial",20))
        time.sleep(5)
        exit()
def possiblemoves(board,val):
    
    inp = deepcopy(board)
    arr = []
    tlist = []
    q = PriorityQueue()

    for i in range(len(inp)):
        for j in range(len(inp)):
            if inp[i][j] == 0 :
                tlist = deepcopy(inp)
                tlist[i][j] = val
                q.put((get_heuristic(tlist),tlist))
    
    while not q.empty() :
        k = q.get()
        arr.append(k[1])
    return arr
activate(functions)
screen.listen()
while State:
    analyse = analyse_game_state(board)
    print_curr()
    if analyse == 2 :
        if move == 0 :
            if ValidMove == True :
                while(ValidMove) :
                    print_message(1)
            if ValidMove == False :
                moves = moves + 1
                move = 1
            analyse = analyse_game_state(board)
            if analyse == 4 :
                print_curr()
                print_message(3)
                break
            elif analyse == 5 :
                print_curr()
                print_message(4)
                break
            elif moves == 9 :
                print_curr()
                print_message(5)
                break
        if move == 1 :
            
            print_message(2)
            board = heuristic_(board)

            move = 0
            moves = moves + 1
            ValidMove = True
    elif analyse == 4 :
        print_curr()
        print_message(3)
        State = False
    elif analyse == 5 :
        print_curr()
        print_message(4)
        State = False
turtle.done()