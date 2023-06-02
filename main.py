import random

def print_board(metrix: list):
    for p in metrix:
        print(p)


def generate_one_track(last_row: int, last_column: int, last_direction: int, counter):
    global board, column_count, row_count
    directions_list = [1, 2, 3, 3, 3, 4, 5]
    next_direction = random.choice(directions_list)
    tried = []
    while True:
        while True:
            match last_direction:
                case 1:  #from up
                    current_row = last_row + 1
                    current_column = last_column
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_column + 1 < 30 and board[current_row][current_column+1] == " ":
                                board[current_row][current_column] = "└"
                                current_direction = 7
                                break
                        case 2:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 8
                                break
                        case 3:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 1
                                break
                        case 4:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 2
                                break
                        case 5:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "┘"
                                current_direction = 3
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 2:  #from up right
                    current_row = last_row + 1
                    current_column = last_column - 1
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "("
                                current_direction = 8
                                break
                        case 2:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 1
                                break
                        case 3:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 2
                                break
                        case 4:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 3
                                break
                        case 5:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "V"
                                current_direction = 4
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 3:  # from right
                    current_row = last_row
                    current_column = last_column - 1
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "┌"
                                current_direction = 1
                                break
                        case 2:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 2
                                break
                        case 3:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 3
                                break
                        case 4:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 4
                                break
                        case 5:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "└"
                                current_direction = 5
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 4:    # from down right
                    current_row = last_row - 1
                    current_column = last_column - 1
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "^"
                                current_direction = 2
                                break
                        case 2:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 3
                                break
                        case 3:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 4
                                break
                        case 4:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 5
                                break
                        case 5:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "("
                                current_direction = 6
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 5:  # from down
                    current_row = last_row - 1
                    current_column = last_column
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "┐"
                                current_direction = 3
                                break
                        case 2:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 4
                                break
                        case 3:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 5
                                break
                        case 4:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 6
                                break
                        case 5:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "┌"
                                current_direction = 7
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 6:  # from down left
                    current_row = last_row - 1
                    current_column = last_column + 1
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = ")"
                                current_direction = 4
                                break
                        case 2:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 5
                                break
                        case 3:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 6
                                break
                        case 4:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 7
                                break
                        case 5:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "^"
                                current_direction = 8
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 7:  # from left
                    current_row = last_row
                    current_column = last_column + 1
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "┘"
                                current_direction = 5
                                break
                        case 2:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 6
                                break
                        case 3:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 7
                                break
                        case 4:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 8
                                break
                        case 5:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "┐"
                                current_direction = 1
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
                case 8:  # from up left
                    current_row = last_row + 1
                    current_column = last_column + 1
                    tried.append(next_direction)
                    match next_direction:
                        case 1:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "V"
                                current_direction = 6
                                break
                        case 2:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 7
                                break
                        case 3:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " "\
                               and board[current_row][current_column+1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 8
                                break
                        case 4:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 1
                                break
                        case 5:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " "\
                               and board[current_row][current_column-1] ==  " "and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = ")"
                                current_direction = 2
                                break
                    tried.sort()
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1
        for r in range(row_count):
            for c in range(row_count):
                if board[r][c] == " ":
                    if generate_one_track(current_row, current_column, current_direction, counter+1):
                        return True
                    else:
                        tried.sort()
                        if tried == [1, 2, 3, 4, 5]:
                            board[current_row][current_column] = "0"
                            return False
                        next_direction += 1
                        if next_direction == 6:
                            next_direction = 1
                else:
                    break
        else:
            return True



#generate metrix
row_count = 30
column_count = 30
board = []
for row in range(row_count):
    row_list = []
    for column in range(column_count):
        row_list.append(" ")
    board.append(row_list)

#generate track
row_id = random.randint(1, 28)
column_id = random.randint(1, 28)
board[row_id][column_id] = "X"
direction = random.randint(1, 8)
generate_one_track(row_id, column_id, direction, 0)
print_board(board)
