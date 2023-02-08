def check_colors(board):
    '''
    Checks colors.
    >>> check_colors(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 2 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    True
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
    >>> >>> validate_board(["****7****",\
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