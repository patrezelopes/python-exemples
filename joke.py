MAP = {
    "SCISSORS": ['ROCK', 'PAPPER'],
    "ROCK": ['PAPPER', 'SCISSORS'],
    "PAPPER": ['SCISSORS', 'ROCK'],
}

if __name__ == '__main__':
    call_1 = input('primeiro: ')
    call_2 = input('segundo: ')
    if call_2 == MAP[call_1][0]:
        print('PLAYER2')
    elif call_2 == MAP[call_1][1]:
        print('PLAYER1')
    elif call_2 == call_1:
        print('DRAW')
