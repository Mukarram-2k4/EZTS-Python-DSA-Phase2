board=[['','','',],['','','',],['','','']]
def print_board(board):
    print(*board[0],sep="|")
    print("-------")
    print(*board[1],sep="|")
    print("-------")
    print(*board[2],sep="|")
    print("-------")
def get_marks():
    marker1=input("Player1 choice(x or O): ").upper()
    marker2=""
    if marker1=="X":
        marker2=="o"
        return ['X','O']
    elif marker1=='o':
        marker2='X'
        return['O','x']
    else:
        print("Invalid Input")
        return get_markers()
def get_coordinates():
    x,y=list(map(int,input("Enter The coordinates").split()))
    if x in [0,1,2]and y in [0,1,2]:
        return[X,Y]
    else:
        print("Invalid Input")
        return get_coordinates()
def check_for_win(board):
    for row in board:
        if row[0] == row[1] and row[2] and row[1]!="":
            return True
        for i in range(len(board)):
            if board[0][i]==board[1][i]and board[i][i]==board[2][i] and board[2][i]!="":
                return True
            if board[0][0]==board[1][1] and board[1][1]==board[2][2]and board[2][2]!="":
                return True
            if board[0][2]==board[1][1] and board[1][1]==board[2][0]and board[2][0]!="":
                return True
            return False
def update_board(board,chance,marker,X,Y):
    if chance==True:
        board[X][Y]=marker
        if check_for_(winboard):
            print("Player1 Wins")
            return "game over"
        return False
    else:
        board[X][Y]=marker
        if check_for_win(board):
            print("Player2 Wins")
            return "game over"
        return True
def play_game():
    player1=0
    player2=0
    m1,m2=get_marker()
    print(f"player1:{m1},player2:{m2}")
    chance=True
    while(True):
        print_board(board)
        X,Y=get_coordinates()
        if chance:
            chance=update_board(board,chance,m1,X,Y)
            if chance =="game over":
                break
            else:
                chance=update_board(board,chance,m2,X,Y)
                if chance=="game over":
                    break
play_game