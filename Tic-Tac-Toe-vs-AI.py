import random

board = ["[1]", "[2]", "[3]",
         "[4]", "[5]", "[6]",
         "[7]", "[8]", "[9]"]
freePositions = []
winningPositions = []

def printBoard(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("---+---+---")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("---+---+---")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def chooseMark():
    mark = input("Choose your mark [ X | O ]: ").upper()

    if mark != "X" and mark != "O":
        isError = True

        while isError:
            print("Error! Choose X or O only!")
            mark = input("Choose your mark [ X | O ]: ").upper()

            if mark == "X" or mark == "O":
                return mark
    else:
        return mark

def opponentsMark(player):
    if player == "X":
        return "O"
    else:
        return "X"

def checkFreePositions(board, freePositions):
    freePositions.clear()

    for count in range(0, 9):
        if board[count] != " X " and board[count] != " O ":
            freePositions.append(int(count))

def pickPosition(mark):
    global moveCount

    printBoard(board)

    position = 10

    while position not in freePositions:
        position = int(input(f"Pick your position [ {mark} ]: ")) - 1
        print("")

        if position not in freePositions:
            print("Position not available! Choose another position.")

    board[position] = " " + mark + " "

    checkFreePositions(board, freePositions)

    moveCount += 1

    if moveCount == 9:
        print("IT'S A DRAW!")
        printBoard(board)
        exit()

def randomize(board):
    position = random.choice(freePositions)

    return position

def compMove(board, player, opponent, isFirstMove):
    global moveCount
    position = 10

    if isFirstMove:
        if board[4] != " X ":
            position = 4
        else:
            edge = [0, 2, 6, 8]
            position = random.choice(edge)
    else:
        position = findBestMoveBot(board, player, opponent)

    print(f"Computer position: {position+1}")

    board[position] = " " + opponent + " "

    checkFreePositions(board, freePositions)

    moveCount += 1

    if moveCount == 9:
        print("IT'S A DRAW!")
        printBoard(board)
        exit()

def findBestMoveBot(board, player, opponent):
    tempBoard = []

    for temp in board:
        tempBoard.append(temp)

    for position in freePositions:
        temp = tempBoard[position]
        tempBoard[position] = " " + opponent + " "

        if hasWinner(tempBoard, opponent):
            return position
        else:
            tempBoard[position] = temp

        temp = tempBoard[position]
        tempBoard[position] = " " + player + " "

        if hasWinner(tempBoard, player):
            return position
        else:
            tempBoard[position] = temp

    return randomize(board)

def hasWinner(board, mark):
    global winningPositions

    if board[0] == " " + mark + " " and board[1] == " " + mark + " " and board[2] == " " + mark + " ":
        winningPositions = [0, 1, 2]
        return True
    elif board[3] == " " + mark + " " and board[4] == " " + mark + " " and board[5] == " " + mark + " ":
        winningPositions = [3, 4, 5]
        return True
    elif board[6] == " " + mark + " " and board[7] == " " + mark + " " and board[8] == " " + mark + " ":
        winningPositions = [6, 7, 8]
        return True
    elif board[0] == " " + mark + " " and board[3] == " " + mark + " " and board[6] == " " + mark + " ":
        winningPositions = [0, 3, 6]
        return True
    elif board[1] == " " + mark + " " and board[4] == " " + mark + " " and board[7] == " " + mark + " ":
        winningPositions = [1, 4, 7]
        return True
    elif board[2] == " " + mark + " " and board[5] == " " + mark + " " and board[8] == " " + mark + " ":
        winningPositions = [2, 5, 8]
        return True
    elif board[0] == " " + mark + " " and board[4] == " " + mark + " " and board[8] == " " + mark + " ":
        winningPositions = [0, 4, 8]
        return True
    elif board[2] == " " + mark + " " and board[4] == " " + mark + " " and board[6] == " " + mark + " ":
        winningPositions = [2, 4, 6]
        return True
    else:
        return False

def printBoardWinner(board, mark, winningPositions):
    for position in range(0, 9):
        if position in winningPositions:
            board[position] = " " + mark + " "
        else:
            board[position] = "   "

    printBoard(board)

def checkWhoWins(board, mark1, mark2):
    if hasWinner(board, mark1):
        print("\nYOU WIN!")
        printBoardWinner(board, mark1, winningPositions)
    elif hasWinner(board, opponent):
        print("YOU LOSE!")
        printBoardWinner(board, mark2, winningPositions)
    else:
        print("IT'S A DRAW!")
        printBoard(board)

player = chooseMark()
opponent = opponentsMark(player)
freePositionsCount = len(freePositions)
checkFreePositions(board, freePositions)
moveCount = 0
isFirstMove = True
thereIsAWinner = False

if player == "X":
    while thereIsAWinner is False:
        pickPosition(player)

        thereIsAWinner = hasWinner(board, player)

        if thereIsAWinner:
            break

        compMove(board, player, opponent, isFirstMove)

        thereIsAWinner = hasWinner(board, opponent)

        if thereIsAWinner:
            break

        isFirstMove = False
elif player == "O":
    while thereIsAWinner is False:
        compMove(board, player, opponent, isFirstMove)

        thereIsAWinner = hasWinner(board, opponent)

        if thereIsAWinner:
            break

        pickPosition(player)

        thereIsAWinner = hasWinner(board, player)

        if thereIsAWinner:
            break

        isFirstMove = False



checkWhoWins(board, player, opponent)