#Tic Tac Toe Game
#Author: Ashlee Butterfield




square = [
    1,2,3,4,5,6,7,8,9
]



def main():
    player_turn = new_turn("")
    print("Welcome to the Tic Tac Toe Game!")
    print("Player 1 will use X")
    print("Player 2 will use O")
    print("Let's Begin!")
    while not (winner(square) or no_winner(square)):
        draw_board()
        turn(player_turn)
        if winner(square) == True:
            print()
            print(f"{player_turn} wins!")
        else:
            player_turn = new_turn(player_turn)
    print("Thank you for playing!")


def new_turn(player):
    if player == "" or player == "O":
        return "X"
    elif player == "X":
        return "O"

def turn(player_turn):
    print()
    print(f"It's {player_turn}'s turn!")
    square_choice = int(input("Please type in a square number: "))
    while square_choice < 1 or square_choice > 9:
        square_choice = int(input("Invalid Answer. Please type in a square number: "))
    square[square_choice-1] = player_turn


def draw_board():
    print()
    print(f"{square[0]}!{square[1]}!{square[2]}")
    print("-+-+-")
    print(f"{square[3]}!{square[4]}!{square[5]}")
    print("-+-+-")
    print(f"{square[6]}!{square[7]}!{square[8]}")
    print()

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[6] == board[4] == board[2])

def no_winner(board):
    for space in range(9):
        if board[space] != "X" and board[space] != "O":
            return False
    print()
    print("It's a tie!")
    return True


if __name__ == "__main__":
    main()