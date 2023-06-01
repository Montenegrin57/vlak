import random

def print_board(metrix: list):
    for p in metrix:
        print(p)


def generate_one_track(board: list, last_row: int, last_column: int, last_direction: int, counter):
    directions_list = [1, 2, 3, 3, 3, 3, 4, 5]
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
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 8
                                break
                        case 3:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 1
                                break
                        case 4:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 2
                                break
                        case 5:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "┘"
                                current_direction = 3
                                break
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
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " ":
                                board[current_row][current_column] = "("
                                current_direction = 8
                                break
                        case 2:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 1
                                break
                        case 3:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 2
                                break
                        case 4:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 3
                                break
                        case 5:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " ":
                                board[current_row][current_column] = "V"
                                current_direction = 4
                                break
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
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 2
                                break
                        case 3:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 3
                                break
                        case 4:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 4
                                break
                        case 5:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "└"
                                current_direction = 5
                                break
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
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " ":
                                board[current_row][current_column] = "^"
                                current_direction = 2
                                break
                        case 2:
                            if current_column - 1 > -1 and board[current_row][current_column-1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 3
                                break
                        case 3:
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 4
                                break
                        case 4:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 5
                                break
                        case 5:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " ":
                                board[current_row][current_column] = "("
                                current_direction = 6
                                break
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
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 4
                                break
                        case 3:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 5
                                break
                        case 4:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 6
                                break
                        case 5:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "┌"
                                current_direction = 7
                                break
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
                            if current_column - 1 > -1 and current_row - 1 > -1 and board[current_row-1][current_column-1] ==  " ":
                                board[current_row][current_column] = ")"
                                current_direction = 4
                                break
                        case 2:
                            if current_row - 1 > -1 and board[current_row-1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 5
                                break
                        case 3:
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 6
                                break
                        case 4:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 7
                                break
                        case 5:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " ":
                                board[current_row][current_column] = "^"
                                current_direction = 8
                                break
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
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " ":
                                board[current_row][current_column] = "/"
                                current_direction = 6
                                break
                        case 3:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 7
                                break
                        case 4:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 8
                                break
                        case 5:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "┐"
                                current_direction = 1
                                break
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
                            if current_column + 1 < 30 and current_row - 1 > -1 and board[current_row-1][current_column+1] ==  " ":
                                board[current_row][current_column] = "V"
                                current_direction = 6
                                break
                        case 2:
                            if current_column + 1 < 30 and board[current_row][current_column+1] ==  " ":
                                board[current_row][current_column] = "─"
                                current_direction = 7
                                break
                        case 3:
                            if current_column + 1 < 30 and current_row + 1 < 30 and board[current_row+1][current_column+1] ==  " ":
                                board[current_row][current_column] = "╲"
                                current_direction = 8
                                break
                        case 4:
                            if current_row + 1 < 30 and board[current_row+1][current_column] ==  " ":
                                board[current_row][current_column] = "|"
                                current_direction = 1
                                break
                        case 5:
                            if current_column - 1 > -1 and current_row + 1 < 30 and board[current_row+1][current_column-1] ==  " ":
                                board[current_row][current_column] = ")"
                                current_direction = 2
                                break
                    if tried == [1, 2, 3, 4, 5]:
                        board[current_row][current_column] = " "
                        return False
                    next_direction += 1
                    if next_direction == 6:
                        next_direction = 1

        if counter > 50:
            return True
        if generate_one_track(board, current_row, current_column, current_direction, counter+1):
            return board
        else:
            if tried == [1, 2, 3, 4, 5]:
                board[current_row][current_column] = " "
                return False



#generate metrix
track_map = []
for row in range(30):
    row_list = []
    for column in range(30):
        row_list.append(" ")
    track_map.append(row_list)

#generate track
row_id = random.randint(0, 29)
column_id = random.randint(0, 29)
track_map[row_id][column_id] = "X"
direction = random.randint(1, 8)
track_map = generate_one_track(track_map, row_id, column_id, direction, 0)

print_board(track_map)
