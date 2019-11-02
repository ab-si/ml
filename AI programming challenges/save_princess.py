#!/usr/bin/python

def dir_print(dire, times):
    for _ in range(abs(times)):
        print(dire)


def display_path_to_princess(n,grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
    diff_rows = princess[0] - mario[0]
    diff_cols = princess[1] - mario[1]
    if diff_rows > 0:
        dir_print('DOWN', diff_rows)
        if diff_cols < 0:
            dir_print('LEFT', diff_cols)
        else:
            dir_print('RIGHT', diff_cols)
    else:
        dir_print('UP', diff_rows) 
        if diff_cols < 0:
            dir_print('LEFT', diff_cols)
        else:
            dir_print('RIGHT', diff_cols)


if __name__ == "__main__":
    '''
    INPUT:
    The first line contains an odd integer N (< 100) denoting the size of the grid.
    This is followed by an NxN grid. Each cell is denoted by ‘-‘ (ascii value: 45).
    The bot position is denoted by ‘m’ and the princess position is denoted by ‘p’.
    The top left of the grid is indexed at (0,0) and the bottom right is indexed at (N-1,N-1)
    OUTPUT:
    Print out all the moves you take to rescue the princess in one go.
    Moves must be separated by ‘\n’ a newline.
    The valid outputs are LEFT or RIGHT or UP or DOWN.

    Example:
    Input:
    3
    ---
    -m-
    p--
    Output:
    DOWN
    LEFT
    '''
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())
    display_path_to_princess(m, grid)