P1 = 1 # item 1 for player 1
P2 = 2 # item 2 for player 2
BLANK = 0 # Item 0 for empty case

SIZE = 9 # size of Table

WINNER_P1 = (P1, P1, P1) # condition for winner is P1
WINNER_P2 = (P2, P2, P2) # condition for winner is P2

def init_table():
    """create cases of morpion, default: 9 cases"""
    return [[BLANK for i in range(SIZE//3)] for j in range(SIZE//3)]

def put_item(table, item, line, column):
    """put item in the line and the column of table
    return True if success else False"""
    if table[line][column] == 0:
        table[line][column] = item
        return True
    return False

def is_winner_line(table, line):
    """test winner for one line of table"""
    line = tuple(table[line])
    if line == WINNER_P1 or line == WINNER_P2:
        return True
    return False

def is_winner_column(table, column):
    """test winner for one column of table"""
    column = tuple((line[column] for line in table))
    if column == WINNER_P1 or column == WINNER_P2:
        return True
    return False
    
def is_winner_diag(table, start):
    """test winner for one diagonale of table"""
    diag = []
    
    count = 1 if not start else -1
    
    for line in table:
        diag.append(line[start])
        start += count
    
    diag = tuple(diag)
    if diag == WINNER_P1 or diag == WINNER_P2:
        return True
    return False
    
def is_winner(table):
    """return if there is a winner"""
    winner_diag = is_winner_diag(table, 0) or is_winner_diag(table, 2)
    winner_line = is_winner_line(table, 0) or is_winner_line(table, 1) or\
                    is_winner_line(table, 2)
    winner_column = is_winner_column(table, 0) or is_winner_column(table, 1) or\
                    is_winner_column(table, 2)
    
    if winner_diag or winner_line or winner_column:
        return True
    
    return False

def display(table):
    """display table"""
    for line in table:
        print(' '.join(map(str, line)))
    
table = init_table()
current_player = P1

while True:
    
    player = input("Entrer la ligne et la colonne où placer l'item {}:"
            .format(current_player))
    
    line, column = list(map(int, player.split()))
    
    if not put_item(table, current_player, line, column):
        continue
    
    if is_winner(table):
        print("le gagnant est l'item {}".format(current_player))
        display(table)
        break
    
    display(table)
    
    current_player = P1 if current_player == P2 else P2
