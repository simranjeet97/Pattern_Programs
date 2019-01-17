def pattern_s():
    return [
        ''.join([
            '*' if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5)
                or (column == 1 and (row == 1 or row == 2 or row == 6))
                or (column == 5 and (row == 0 or row == 4 or row == 5))) else ' '
            for column in range(7)]) for row in range(7)
    ]

def pattern_i():
    return [
        ''.join([
            '*' for column in range(1)]) for row in range(7)
    ]

def pattern_m():
    return [
        ''.join([
            '*' if column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3) else ' '
            for column in range(7)]) for row in range(7)
    ]

def pattern_r():
    return [
        ''.join([
            '*' if column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2) else ' '
            for column in range(7)]) for row in range(7)
    ]

def pattern_a():
    return [
        ''.join([
            '*' if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))) else ' '
            for column in range(7)]) for row in range(7)
    ]
def pattern_n():
    return [
        ''.join([
            '*' if (col==0 or col==1 or col==6 or col==7) or (row==col-1) else ' '
            for col in range(7)]) for row in range(7)
    ]





for s,i,m,r,a,n in zip(pattern_s(), pattern_i(),pattern_m(),pattern_r(),pattern_a(),pattern_n()):
    print(s,i,m,r,a,n)
