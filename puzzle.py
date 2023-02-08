def check_columns(board: list):
    """
    checks whether there are no two or more identical digits in one column and returns True or False
    >>> check_cols(["*1**4***5","**3***27*","4***2**6*","*76**91**", \
    "**83**3**","*4**8**3*","***7*1**8","2**5***4*","*6***2**9"])
    True
    """
    for col in range(len(board[0])):
        curr_col_set = set()
        for line in range(len(board)):
            if board[line][col] != "*":
                if board[line][col] in curr_col_set:
                    return False
                else:
                    curr_col_set.add(board[line][col])

    return True