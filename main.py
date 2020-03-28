import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

def shuffle_field(): 
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 16)) + [EMPTY_MARK]
    random.shuffle(field)
    return field

def print_field(field): 
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    k = 0
    for i in range(16):
        if k % 4 == 0:
            print()

        if str(field[i]) == 'x':
            print(field[i], end='  ')
        elif field[i] < 10:
            print(field[i], end='  ')
        else:
            print(field[i], end=' ')
        k += 1

    print()
        
    

def is_game_finished(field):  
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    win_game = list(range(1, 16)) + [EMPTY_MARK]
    return (win_game == field)


def perform_move(field, key): # - 
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    delta = MOVES[key]
    x = field.index('x')
    
    if x % 4 == 0 and delta == -1 or x % 4 == 3 and delta == 1:
        raise IndexError('Ошибка!')

    if x < 4 and delta == -4 or x > 11 and delta == 4:
        raise IndexError('Ошибка!')

    field[x], field[x + delta] = field[x + delta], field[x]
    
    return field
    
def handle_user_input():  
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    keys = MOVES.keys()
    message = 'Введите направление хода (' + ','.join(keys) + '): '
    move = input(message)

    while move not in keys:
        move = input(message)
    
    return  move

def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()

    while True:
        print_field(field)
        while True:
            try:
                field = perform_move(field, handle_user_input())
                break
            except IndexError as ex:
                print (ex)
        if is_game_finished(field):
            print('Игра закончена!')

if __name__ == '__main__':

    main()


    