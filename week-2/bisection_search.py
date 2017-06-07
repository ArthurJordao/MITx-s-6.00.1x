print('Please think of a number between 0 and 100!')
min_value = 0
guess = 50
max_value = 100
valid_options = ['c', 'h', 'l']

while True:
    print('Is your secret number ' + str(guess) + '?')
    result = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                   "Enter 'c' to indicate I guessed correctly. ")
    if result not in valid_options:
        print('Sorry, I did not understand your input.')
    if result == 'c':
        break
    if result == 'h':
        max_value = guess
    if result == 'l':
        min_value = guess
    guess = min_value + (max_value - min_value) // 2

print('Game over. Your secret number was: ' + str(guess))
