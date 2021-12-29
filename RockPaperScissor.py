import random
import time

print('Welcome to Rock Paper Scissors!')
print('You will be playing against a random AI')
i = 0  # Counter for number of games won by user
j = 0  # Counter for number of games won by computer
# print('Type \"rock\" \"paper\" or \"scissor\":')
while i < 3 and j < 3:
    choice = input('Type \"rock\" \"paper\" or \"scissor\":')
    while choice.lower() not in ['rock', 'paper', 'scissor']:
        choice = input('Please type \"rock\" \"paper\" or \"scissor\":')
    rand = random.randint(0,3)
    if rand == 0:  # Rock
        print('AI picked ROCK')
        if choice.lower() == 'scissor':
            print('AI won this round!')
            j += 1
        if choice.lower() == 'paper':
            print('You won this round!')
            i += 1
        else:
            print('Tie!')
    elif rand == 1:  # Paper
        print('AI picked PAPER')
        if choice.lower() == 'rock':
            print('AI won this round!')
            j += 1
        if choice.lower() == 'scissor':
            print('You won this round!')
            i += 1
        else:
            print('Tie!')
    else:  # Scissor
        print('AI picked SCISSOR')
        if choice.lower() == 'paper':
            print('AI won this round!')
            j += 1
        if choice.lower() == 'rock':
            print('You won this round!')
            i += 1
        else:
            print('Tie!')
    time.sleep(1)
    print('You\'ve won ' + str(i) + ' games')
    print('The AI\'s won ' + str(j) + ' games')

print('Good Game!')
if j > 2:
    print('AI won this game! Better luck next time!')
    print('You won a total of ' + str(i) + ' games!')
else:
    print('You won! Great job!')
    print('The AI won a total of ' + str(j) + ' games!')
