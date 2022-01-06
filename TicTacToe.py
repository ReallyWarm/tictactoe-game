import random

def selectGameMode():
    print("GAME MODE")
    print("1. One player")
    print("2. Two player")
    while True:
        mode = input("Select game mode (1/2) : ")
        if mode == '1' or ans.lower == 'one player':
            mode = 1
            return mode
        elif mode == '2' or ans.lower == 'two player':
            mode = 2
            return mode
        else:
            print("This isn\'t a game mode")

def printBoard():
    print(' ' + box[1] + ' | ' + box[2] + ' | ' + box[3])
    print('-----------')
    print(' ' + box[4] + ' | ' + box[5] + ' | ' + box[6])
    print('-----------')
    print(' ' + box[7] + ' | ' + box[8] + ' | ' + box[9])
    print('-----------------------------------')

def isOver(mark, side):
    return ((mark[1] == side and mark[2] == side and mark[3] == side) or 
    (mark[4] == side and mark[5] == side and mark[6] == side) or 
    (mark[7] == side and mark[8] == side and mark[9] == side) or 
    (mark[1] == side and mark[4] == side and mark[7] == side) or 
    (mark[2] == side and mark[5] == side and mark[8] == side) or 
    (mark[3] == side and mark[6] == side and mark[9] == side) or 
    (mark[1] == side and mark[5] == side and mark[9] == side) or 
    (mark[3] == side and mark[5] == side and mark[7] == side))

def getTurn():
    return turn

def nextTurn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'

def isFull(box):
    return True if box.count(' ') < 1 else False

def placeMark(mark, pos):
    box[pos] = mark

def freeSpace(pos):
    return box[pos] == ' '

def randomMove(arr):
    lenth = len(arr)
    r = random.randrange(0, lenth)
    return arr[r]

def playerMove(turn):
    progress = True
    while progress:
        move = input(f"It's {turn}\'s turn! Choose a position to place a mark (1-9) : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freeSpace(move):
                    if turn == 'X':
                        placeMark('X', move)
                        progress = False
                    else:
                        placeMark('O', move)
                        progress = False
                else:
                    print('This space is occupied!')
            else:
                print('This position is out of board!')
        except:
            print('This isn\'t a number!')

def botMove():
    possibleChoice = [i for i, mark in enumerate(box) if mark == ' ' and i != 0]
    move = 0

    # see if next O's or X's move will win the game
    for option in ['O', 'X']:
        for pos in possibleChoice:
            nextBox = box[:]
            nextBox[pos] = option
            if isOver(nextBox, option):
                move = pos
                return move
    
    if 5 in possibleChoice:
        move = 5
        return move

    openCorners = []
    openEdges = []
    for pos in possibleChoice:
        if pos in [1, 3, 7, 9]:
           openCorners.append(pos)
        if pos in [2, 4, 6, 8]:
           openEdges.append(pos) 

    if len(openCorners) > 0:
        move = randomMove(openCorners)
        return move

    if len(openEdges) > 0:
        move = randomMove(openEdges)

    return move

def main():
    print("Welcome to Tic Tac Toe :D")
    gamemode = selectGameMode()
    printBoard()

    while not isFull(box):
        turn = getTurn()
        if not isOver(box, 'O'):
            playerMove(turn)
            printBoard()
            turn = nextTurn(turn)
        else:
            print("O is the winner!")
            break

        if not isOver(box, 'X'):
            if gamemode == 1:
                move = botMove()
                if move == 0:
                    print('Too bad. It\'s stalemate!')
                    break
                else:
                    placeMark('O', move)
                    turn = nextTurn(turn)
                    print('Computer placed an \'O\' in position', move , ':')                    
            else:
                playerMove(turn)
            printBoard()
            turn = nextTurn(turn)           
        else:
            print("X is the winner!")
            break
    
    if isFull(box):
        print("Too bad. It\'s stalemate!")

while True:
    ans = input('Do you want to play? (Y/N) : ')
    if ans.lower() == 'y' or ans.lower() == 'yes':
        turn = 'X'
        box = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break