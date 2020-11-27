import random
import time

print('Welcome to Rock, Paper, Scissors!\n')

def main():
    rounds = int(input('Best of how many rounds are we playing?:  '))
    userWins = 0
    computerWins = 0
    
    for i in range(rounds):
        if userWins > (rounds / 2) or computerWins > (rounds / 2):
            break
        _round = i +1
        wins = PlayRound(userWins, computerWins, _round)
        userWins = wins[0]
        computerWins = wins[1] 

    time.sleep(1)
    if userWins > computerWins:
        print('You win best of ', rounds, '!', sep='')
    else:
        print('Computer wins best of ', rounds, '.', sep='')

    time.sleep(2)
    repeat = input('\n\nPlay again? y/n:  ')
    if repeat.lower() == 'y':
        print()
        main()

def PlayRound(userWins, computerWins, _round):
    if _round > 1:
        time.sleep(1)
    print('\n(Round ', _round, ')', sep='')
    print('==============================================')
    usersPlay = input('Choose rock, paper, or scissors:  ')
    usersPlay = usersPlay.lower()
    valid = CheckIfValid(usersPlay)
    if valid == False:
        print('Invalid input. Restarting round.')
        time.sleep(1)
        return PlayRound(userWins, computerWins, _round)
    computersPlay = GenerateComputerAnswer()
    winner = CompareAnswer(usersPlay, computersPlay)
    print('Computer plays: ', computersPlay)
    time.sleep(1)
    PrintPlay(usersPlay, computersPlay)
    time.sleep(4)
    if winner == 'user':
        userWins += 1
    if winner == 'computer':
        computerWins += 1
    if winner == 'tie':
        return PlayRound(userWins, computerWins, _round)
    print('Player\'s total wins: ', userWins)
    print('Computer\'s total wins: ', computerWins)
    wins = [userWins, computerWins]
    return wins
        
def GenerateComputerAnswer():
    ansLibrary = ['rock', 'paper', 'scissors']
    compAnsRaw = random.randint(0,2)
    return ansLibrary[compAnsRaw]

def CompareAnswer(userAns, compAns):
    if userAns == compAns:
        return 'tie'
    if userAns == 'rock' and compAns == 'paper':
        return 'computer'
    if userAns == 'rock' and compAns == 'scissors':
        return 'user'
    if userAns == 'paper' and compAns == 'rock':
        return 'user'
    if userAns == 'paper' and compAns == 'scissors':
        return 'computer'
    if userAns == 'scissors' and compAns == 'rock':
        return 'computer'
    if userAns == 'scissors' and compAns == 'paper':
        return 'user'

def PrintPlay(userAns, compAns):
    print()
    if userAns == compAns:
        print('The plays are the same. The round is a tie and must be repeated.')
    if userAns == 'rock' and compAns == 'paper':
        print('Paper covers rock. Computer wins this round.')
    if userAns == 'rock' and compAns == 'scissors':
        print('Rock smashes scissors. Player wins this round.')
    if userAns == 'paper' and compAns == 'rock':
        print('Paper covers rock. Play wins this round.')
    if userAns == 'paper' and compAns == 'scissors':
        print('Scissors cut paper. Computer wins this round.')
    if userAns == 'scissors' and compAns == 'rock':
        print('Rock smashes scissors. Computer wins this round.')
    if userAns == 'scissors' and compAns == 'paper':
        print('Scissors cuts paper. Player wins this round.')
    print()

def CheckIfValid(play):
    ansLibrary = ['rock', 'paper', 'scissors']
    if play in ansLibrary:
        return True
    else:
        return False

main()
