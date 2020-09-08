# 3 tumblers and 1 ball shuffle game

from random import shuffle

def player_guess():
	guess = ''
	while guess not in ['0','1','2']:
		guess = input('Pick a number - 0, 1, 2: ')
	return int(guess)
	
def shuffle_list(my_list):
	shuffle(my_list)
	return my_list
	
def check_guess(mixed_list, guess):
	if mixed_list[guess] == 'O':
		print('Correct Guess! :)')
	else:
		print('Wrong Guess! :(')
		print(mixed_list)


def main():
	my_list = [' ', 'O', ' ']
	mixed_list = shuffle_list(my_list)
	guess = player_guess()
	check_guess(mixed_list, guess)
	
if __name__ == "__main__":
    main()