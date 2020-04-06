"""
Aaron Jorgensen
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random

# Generates title of the app with dashes equal to length of word.
# Place outside the start_game function so that it is not shown more than once.
game_title = 'Welcome to the Number Guessing Game!'
title_len = len(game_title)
print('-' * title_len, '\n', game_title + '\n', '-' * title_len)
user_name = input("Hello! what can I call you?: ")
print(f"Ok Great, nice to meet you {user_name} Let's get started")

high_score = []

def start_game():
	number = random.randint(1, 10)


	# Start the attempts count at 0
	user_attempts = 0

	print("Please enter a number")

	# Changed while statement based on advise from @Megan, Slack moderator.
	# Thanks @Megan!!!!
	game_running = True

	while game_running:
		try:
			# Adds increment to number of attempts each time.
			user_attempts += 1
			# Creates a random number
			# asks the user for a number
			number_guessed = int(input())

			# If statment checks if user guessed within the acceptable range (i.e 1-10)
			if number_guessed not in range(1, 11):
				print(f"Ummm remember the numbers are between 1 and 10 cowboy!\nthat's your {user_attempts} attempt")
			elif number_guessed > number:
				print(f"Nope, too high. You guessed {number_guessed}\nthat was your {user_attempts} attempt")

			# If the user guesses lower than random generated number it tells you and lets you you number of attempts.
			elif number_guessed < number:
				print(f"Nope, too Low. You guessed {number_guessed}\nthat was your {user_attempts} attempt")

			# Success! You guessed the right number. You are magical!!
			elif number_guessed == number:
				print(f"You must be Psychic. You had a total of {user_attempts} guesses")
				play_again = input("Would you like to play again? Y/N: ")
				# practicing expressive names. Made a explicit list of acceptable responses to the 'Y'
				play_again_acceptable_answers = {'yes', 'y', 'Y', 'Yes', 'YES'}
				if play_again in play_again_acceptable_answers:

					# take score and add it to a list. than sort it and return the lowest number
					high_score.append(user_attempts)
					high_score.sort()
					print("Best score is:", *high_score[:1])
					number = []

					start_game()
				else:
					print("Ok, Bye")
					game_running = False
					raise SystemExit

		except ValueError:
			print("Oops! That's not a number")
			continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
	start_game()
