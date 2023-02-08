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