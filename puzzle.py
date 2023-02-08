def check_lines(board):
    """Check lines 
    >>> check_lines([\
    "**** ****",\
    "***1 ****",\
    "  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  ",\
    "  8  2***",\
    "  2  ****"\
    ])
    True
    """
    for i in range(len(board)):
        check_list = []
        for k in range(len(board[i])):
            if board[i][k] not in check_list and board[i][k] != ' ' and board[i][k] != '*':
                check_list.append(board[i][k])
            elif board[i][k] in check_list:
                return False
    return True

def check_columns(board: list):
    """
    checks whether there are no two or more identical digits in one column and returns True or False
    >>> check_columns(["**** ****",\
"***1 **", "  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **",\
"  8  2***", "  2  ****"])
    False
    """
    for col in range(len(board[0])):
        curr_col_set = set()
        for line in range(len(board)):
            if board[line][col] != "*" and board[line][col] != ' ':
                if board[line][col] in curr_col_set:
                    return False
                else:
                    curr_col_set.add(board[line][col])

    return True 

def check_colors(board):
    '''
    Checks colors.
    '''
    s = 0
    lst_for_check = []
    for i in range(0,5):
        for k in range(4 + s , 4 + s + 5):
            value = board[k][i]
            if board[k][i] != ' ':
                if board[k][i] in lst_for_check:
                    return False
                else:
                    lst_for_check.append(board[k][i])
            if k == 5+s+4-1:
                for line in range(i,i +5):
                    if board[k][line] in lst_for_check:
                        return False
                    elif board[k][line] != ' ':
                        lst_for_check.append(board[k][line])
        lst_for_check = []
        s-=1
    return True

def validate_board(board):
    '''
    Checks main function.
    >>> validate_board(["****7****",\
"***17****",\
"**  3****",\
"* 4 1****",\
"     9 2 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    '''
    return check_lines(board) and check_columns(board) and check_colors(board)
