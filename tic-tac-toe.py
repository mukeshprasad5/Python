# A Simple Tic-Tac-Toe Game

def curr_stage(arr):
    print("---------")
    for row in arr:
        print('|', end = ' ')
        print(*row, end = ' ')
        print('|')
    print("---------")
    
    
def x_or_y_wins(arr, x):
    pattern = ''
    for row in arr:
        pattern += ''.join(map(str, row))
    
    if pattern[2:7:2] == x or pattern[:9:4] == x: return True
    # Rows
    for i in range(0, 7, 3):
        if pattern[i:i+3] == x:
            return True
    # cols
    for i in range(3):
        if pattern[i::3] == x:
            return True
    return False


def start_game():
    arr = [[' '] * 3 for _ in range(3)]
    curr_stage(arr)
    turn = 'X'
    n = 0
    while True:
        inp = input("Enter coordinates: ").split()
        
        if len(inp) == 1 or not(inp[0].isdigit()) or not(inp[1].isdigit()):
            print("You should enter numbers!")
            continue
        
        a, b = int(inp[0]), int(inp[1])
        if not(1 <= a <= 3) or not(1 <= b <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        
        if arr[a-1][b-1] != ' ':
            print("This cell is occupied! Choose another one!")
            continue
        
        arr[a-1][b-1] = turn
        turn = "O" if turn == 'X' else "X"
        curr_stage(arr) # print current pattern 
        n += 1
        if n >= 3:
            if x_or_y_wins(arr, 'XXX'):
                print("X wins")
                break
            
            elif x_or_y_wins(arr, 'OOO'):
                print("O wins")
                break
            
            elif n == 9:
                print("Draw")
                break

while True:
    start_game()
    choice = input("Wanna play again(Y/N)?")
    if choice.lower() == 'n':
        print("Hope you enjoyed!")
        print("See you later!")
        break
    
