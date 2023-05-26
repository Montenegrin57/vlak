import random


def print_board(metrix: list):
    for p in metrix:
        print(p)


def generate_one_track(board: list, last_row: int, last_column: int, last_direction: int):
    directions_list = [1, 2, 3, 3, 3, 3, 4, 5]
    while True:
        next_direction = random.choice(directions_list)
        match last_direction:
            case 1:  #from up
                current_row = last_row + 1
                current_column = last_column
                match next_direction:
                    case 1:
                        if current_column + 1 < 30:
                            board[current_row][current_column] = "└"
                            current_direction = 7
                            break
                    case 2:
                        if current_column + 1 < 30 or current_row + 1 < 30:
                            board[current_row][current_column] = "\""
                            current_direction = 8
                            break
                    case 3:
                        if current_row + 1 < 30:
                            board[current_row][current_column] = "|"
                            current_direction = 1
                            break
                    case 4:
                        if current_column - 1 > -1 or current_row + 1 < 30:
                            board[current_row][current_column] = "/"
                            current_direction = 2
                            break
                    case 5:
                        if current_column - 1 > -1:
                            board[current_row][current_column] = "┘"
                            current_direction = 3
                            break
            case 2:  #from up right
                current_row = last_row + 1
                current_column = last_column - 1
                match next_direction:
                    case 1:
                        if current_column + 1 < 30 or current_row + 1 < 30:
                            board[current_row][current_column] = "("
                            current_direction = 8
                            break
                    case 2:
                        if current_row + 1 < 30:
                            board[current_row][current_column] = "|"
                            current_direction = 1
                            break
                    case 3:
                        if current_column - 1 > -1 or current_row + 1 < 30:
                            board[current_row][current_column] = "/"
                            current_direction = 2
                            break
                    case 4:
                        if current_column - 1 > -1:
                            board[current_row][current_column] = "─"
                            current_direction = 3
                            break
                    case 5:
                        if current_column - 1 > -1 or current_row - 1 > -1:
                            board[current_row][current_column] = "V"
                            current_direction = 4
                            break
            case 3:  # from right
                current_row = last_row
                current_column = last_column - 1
                match next_direction:
                    case 1:
                        if current_row + 1 < 30:
                            board[current_row][current_column] = "┌"
                            current_direction = 1
                            break
                    case 2:
                        if current_column - 1 > -1 or current_row + 1 < 30:
                            board[current_row][current_column] = "/"
                            current_direction = 2
                            break
                    case 3:
                        if current_column - 1 > -1:
                            board[current_row][current_column] = "─"
                            current_direction = 3
                            break
                    case 4:
                        if current_column - 1 > -1 or current_row - 1 > -1:
                            board[current_row][current_column] = "\""
                            current_direction = 4
                            break
                    case 5:
                        if current_row - 1 > -1:
                            board[current_row][current_column] = "└"
                            current_direction = 5
                            break
            case 4:    # from down right
                current_row = last_row + 1
                current_column = last_column - 1
                match next_direction:
                    case 1:
                        if current_column - 1 > -1 or current_row + 1 < 30:
                            board[current_row][current_column] = "^"
                            current_direction = 2
                            break
                    case 2:
                        if current_column - 1 > -1:
                            board[current_row][current_column] = "─"
                            current_direction = 3
                            break
                    case 3:
                        if current_column - 1 > -1 or current_row - 1 > -1:
                            board[current_row][current_column] = "\""
                            current_direction = 4
                            break
                    case 4:
                        if current_row - 1 > -1:
                            board[current_row][current_column] = "|"
                            current_direction = 5
                            break
                    case 5:
                        if current_column + 1 < 30 or current_row - 1 > -1:
                            board[current_row][current_column] = "("
                            current_direction = 6
                            break
            case 5:  # from down
                current_row = last_row + 1
                current_column = last_column
                match next_direction:
                    case 1:
                        if current_column - 1 > -1:
                            board[current_row][current_column] = "┐"
                            current_direction = 3
                            break
                    case 2:
                        if current_column - 1 > -1 or current_row - 1 > -1:
                            board[current_row][current_column] = "\""
                            current_direction = 4
                            break
                    case 3:
                        if current_row - 1 > -1:
                            board[current_row][current_column] = "|"
                            current_direction = 5
                            break
                    case 4:
                        if current_column + 1 < 30 or current_row - 1 > -1:
                            board[current_row][current_column] = "/"
                            current_direction = 6
                            break
                    case 5:
                        if current_column + 1 < 30:
                            board[current_row][current_column] = "┌"
                            current_direction = 7
                            break

            case 6:  # from down left
                current_row = last_row + 1
                current_column = last_column + 1
                match next_direction:
                    case 1:
                        if current_column - 1 > -1 or current_row - 1 > -1:
                            board[current_row][current_column] = ")"
                            current_direction = 4
                            break
                    case 2:
                        if current_row - 1 > -1:
                            board[current_row][current_column] = "|"
                            current_direction = 5
                            break
                    case 3:
                        if current_column + 1 < 30 or current_row - 1 > -1:
                            board[current_row][current_column] = "/"
                            current_direction = 6
                            break
                    case 4:
                        if current_column + 1 < 30:
                            board[current_row][current_column] = "─"
                            current_direction = 7
                            break
                    case 5:
                        if current_column + 1 < 30 or current_row + 1 < 30:
                            board[current_row][current_column] = "^"
                            current_direction = 8
                            break
            case 7:  # from left
                current_row = last_row
                current_column = last_column + 1
                match next_direction:
                    case 1:
                        if current_row - 1 > -1:
                            board[current_row][current_column] = "┘"
                            current_direction = 5
                            break
                    case 2:
                        if current_column + 1 < 30 or current_row - 1 > -1:
                            board[current_row][current_column] = "/"
                            current_direction = 6
                            break
                    case 3:
                        if current_column + 1 < 30:
                            board[current_row][current_column] = "─"
                            current_direction = 7
                            break
                    case 4:
                        if current_column + 1 < 30 or current_row + 1 < 30:
                            board[current_row][current_column] = "\""
                            current_direction = 8
                            break
                    case 5:
                        if current_row + 1 < 30:
                            board[current_row][current_column] = "┐"
                            current_direction = 1
                            break
            case 8:  # from up left
                current_row = last_row - 1
                current_column = last_column + 1
                match next_direction:
                    case 1:
                        if current_column + 1 < 30 or current_row - 1 > -1:
                            board[current_row][current_column] = "V"
                            current_direction = 6
                            break
                    case 2:
                        if current_column + 1 < 30:
                            board[current_row][current_column] = "─"
                            current_direction = 7
                            break
                    case 3:
                        if current_column + 1 < 30 or current_row + 1 < 30:
                            board[current_row][current_column] = "\""
                            current_direction = 8
                            break
                    case 4:
                        if current_row + 1 < 30:
                            board[current_row][current_column] = "|"
                            current_direction = 1
                            break
                    case 5:
                        if current_column - 1 > -1 or current_row + 1 < 30:
                            board[current_row][current_column] = ")"
                            current_direction = 2
                            break

    return_list = [board, current_row, current_column, current_direction]
    return return_list


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
next_list = generate_one_track(track_map, row_id, column_id, direction)
for i in range(8):
    next_list = generate_one_track(next_list[0], next_list[1], next_list[2], next_list[3])
print_board(track_map)
