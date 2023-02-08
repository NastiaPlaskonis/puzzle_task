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