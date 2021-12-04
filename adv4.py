with open("input_day_4.txt") as f:
    lines = f.read().splitlines()

import numpy as np

# get the numbers
nums = [int(i) for i in lines[0].split(",")]

# get lists as 5x5 arrays
boards = np.array([[list(map(int, filter(lambda x: x != '', row.split(' ')))) for row in lines[i:i + 5]] for i in range(2, len(lines), 6)])


# play bingo

def calculate_win_number_score(board, marks, num_list, i=0):
    num = num_list[i]
    marks[board == num] = True

    # calculate win condition (any row or any column has 5 marked spots)
    if any(np.sum(marks, axis=0) == 5) or any(np.sum(marks, axis=1) == 5):
        return [i, int(np.sum(board[marks==False]) * num)]
    return calculate_win_number_score(board, marks, num_list, i+1)

# calculate win number for each board
win_number_scores = np.array([calculate_win_number_score(board, np.zeros((5,5)), nums) for board in boards])

# get minimum index of win number with score
print(win_number_scores[np.argmin(win_number_scores[:, 0]),1])

# part 2
# get maximum index of win number with score
print(win_number_scores[np.argmax(win_number_scores[:, 0]), 1])
