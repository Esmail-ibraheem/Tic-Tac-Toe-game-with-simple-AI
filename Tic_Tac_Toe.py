import random
board = [" " for x in range(10)]

def InsertLetter(pos,letter):
    board[pos] = letter
def SpaceFree(pos):
    return board[pos] == " "
def PrintBoard(board):
    print("-----------")
    print("   |   |")
    print("  " + board[1] + "| " + board[2] + " |" + board[3])
    print("-----------")
    print("   |   |")
    print("  " + board[4] + "| " + board[5] + " |" + board[6])
    print("-----------")
    print("   |   |")
    print("  " + board[7] + "| " + board[8] + " |" + board[9])
    print("-----------")
def IsWinner(bo , le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or 
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le)    )
def IsBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
def PlayerMove():
    run = True
    while run :
        move = input("Select a number from (1-9) to enter your position : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if SpaceFree(move):
                    run = False
                    InsertLetter(move,"X")
                else:
                    print("This Place is Ocuupied !")
            else:
                print("Select a number within a range !")
        except:
            print("Type a number , nothing esle")
def SelectRandom(li):
    length = len(li)
    R = random.randrange(0,length)
    return li[R]
def ComputerMove():
    PossibleMoves = [x for x,letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O" , "X"]:
        for i in PossibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if IsWinner(boardCopy,let):
                move = i
                return move

    CornerOpen = []
    for i in PossibleMoves:
        if i in [1,3,7,9]:
            CornerOpen.append(i)
    if len(CornerOpen) > 0:
        move = SelectRandom(CornerOpen)

    if 5 in PossibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in PossibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = SelectRandom(edgesOpen)

    return move

def main():
    print("Welcome to My Tic Tac Toe Game (: :")
    name = input("Enter your name : ").lower().strip()
    print(f"Ok , {name} your move will be [X] letter")
    PrintBoard(board)

    while not(IsBoardFull(board)):
        if not(IsWinner(board,"O")):
            PlayerMove()
        else:
            print("Sorry , O's win this time ): (that's me (: ))")
            PrintBoard(board)
            break
        if not(IsWinner(board,"X")):
            move = ComputerMove()
            if move == 0:
                print("Tie Game ! >> 1")
            else:
                InsertLetter(move,"O")
                print(f"Computer's moved is : " , move)
                PrintBoard(board)
        else:
            print("Great Job , X's win this Time (:")
            PrintBoard(board)
            break
    if IsBoardFull(board):
        print("Tie Game ! >> 2")
        PrintBoard(board)

if __name__ == "__main__":
    main()
