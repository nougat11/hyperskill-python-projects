# write your code here
from string import digits
def output():
    field = [[], [], []]
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if (state[index]=='_'):
                state[index]=' '
            field[i].append(state[index])
    print('-' * 9)
    for i in range(3):
        print('|',*field[i],'|')
    print('-' * 9)
    
state = [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ']
POSITION = (3, 2, 1)
output()
move = 0
game = True

while game:
    
    x, y = input("Enter the coordinates: > ").split()
    if x not in digits or y not in digits:
        print("You should enter numbers!")
        continue
    elif int(x) not in POSITION or int(y) not in POSITION:
        print("Coordinates should be from 1 to 3!")
        continue
    x, y = POSITION[int(y) - 1] - 1, int(x) - 1
    if state[x * 3 + y] != ' ':
        print("This cell is occupied! Choose another one!")
    else:
        move = (move + 1) % 2
        state[x * 3 + y] = 'X' if move else 'O'
        output()
    flags = [False, False, False, False, True]
    conditions = ('Impossible', 'O wins', 'X wins', 'Draw', 'Game not finished')
    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for combo in combinations:
        if (state[combo[0]] == state[combo[1]] == state[combo[2]] == 'X'):
            flags[2] = True
        if (state[combo[0]] == state[combo[1]] == state[combo[2]] == 'O'):
            flags[1] = True
    if (flags[1] == flags[2] == True) or (flags[1] == flags[2] == False and abs(state.count('X') - state.count('O')) > 1):
        flags[0] = True
    if flags[1] == flags[2] == False and state.count(' ') == 0:
        flags[3] = True
    for index in range(4):
        if flags[index]:
            print(conditions[index])
            game = False
