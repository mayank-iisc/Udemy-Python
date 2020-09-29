#Function to Display a board
def display_board(board):
    print('\n'*100)
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
	
#Function to take input 
def player_input():
    '''
    Output Format: (Player1 marker, Player2 marker)
    '''
    
    choice = ''     
    while choice not in ['X','O']:
        choice = input("Player A: Make your choice (X / O):")
    
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
		
def place_marker(board, position, mark):
    board[position-1] = mark
    return board
	
def win_check(board, mark):
    #row check
    if (board[0] == board[1] == board[2] == mark):
        return True
    elif (board[3] == board[4] == board[5] == mark):
        return True
    elif (board[6] == board[7] == board[8] == mark):
        return True
    #column check
    elif (board[0] == board[3] == board[6] == mark):
        return True
    elif (board[1] == board[4] == board[7] == mark):
        return True
    elif (board[2] == board[5] == board[8] == mark):
        return True
    #diagonal check
    elif (board[0] == board[4] == board[8] == mark):
        return True
    elif (board[2] == board[4] == board[6] == mark):
        return True
    else:
        return False
		
import random

def choose_first():
    starter = random.randint(1,2)
    if starter == 1:
        return 'Player A'
    else:
        return 'Player B'
		
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False
		
		
def full_board_check(board):
    
    #Board is Full if we return True
    
    for i in range(0,9):
        if space_check(board, i):
            return False
    
    return True
	
def player_choice(board):
    place = int(input('Choose a place where you want to insert(1-9):'))
    
    while place not in range(1,10) or space_check(board, place-1) == False:
        print('Wrong Choice!')
        place = int(input('Choose a place where you want to insert(1-9):'))

    return place
	
def replay():
    play_again = input('Do you want to play again (Y/N)? ')
    while play_again not in ['Y','N']:
        print('Wrong Choice!')
        play_again = input('Do you want to play again (Y/N)? ')
    
    if play_again == 'Y':
        return True
    else:
        return False
		
print('Welcome to Tic Tac Toe!')


def main():

	while True:

		#Setup (Board, Who is first,choose markers X, O)
    
		board = [' ']*9
		choose_first()
		p1_marker, p2_marker = player_input()
    
		turn = choose_first()
		print(turn + ' will go first')
    
		play_game = input('Ready to play (Y/N)?')
    
		if play_game == 'Y':
			game_on = True
		else:
			game_on = False

		while game_on:
        
			if turn == 'Player A':
        
				# Show Board
				display_board(board)
        
				# Choose Position
				position = player_choice(board)
        
				# Place the marker in the position
				place_marker(board, position, p1_marker)
        
				# Check if they Won?
				if win_check(board, p1_marker):
					display_board(board)
					print('Player A won the game!')
					game_on = False
				else:
					# or check if tie?
					if full_board_check(board):
						display_board(board)
						print('Tie Game!')
						game_on = False
					else:
						turn = 'Player B'
        
			# No tie or win? Next player's turn
			else:
				# Show Board
				display_board(board)
        
				# Choose Position
				position = player_choice(board)
        
				# Place the marker in the position
				place_marker(board, position, p2_marker)
			
				# Check if they Won?
				if win_check(board, p2_marker):
					display_board(board)
					print('Player B won the game!')
					game_on = False
				else:
					# or check if tie?
					if full_board_check(board):
						display_board(board)
						print('Tie Game!')
						game_on = False
					else:
						turn = 'Player A'

		if replay() == False:
			break
	
if __name__ == "__main__":
    main()	
		
