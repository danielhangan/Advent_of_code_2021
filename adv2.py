with open("input.txt") as f:
    lines = f.readlines()

def day_2_part_1():
    '''
    forward X = horizontal
    down X = + In depth
    up X = - In depth
    '''
    horizontal = 0
    vertical = 0

    for i in lines:
        movement = i.strip().split(" ")

        if movement[0] == "down":
            vertical += int(movement[1])
        elif movement[0] == "up":
            vertical -= int(movement[1])
        else:
            horizontal += int(movement[1])

    return horizontal * vertical

result_1 = day_2_part_1()

def day_2_part_2():
    '''
    forward X = + horizontal & aim = aim * forward
    down X = + In aim
    up X = - In aim
    '''
    horizontal = 0
    depth = 0
    aim = 0

    for i in lines:
        movement = i.strip().split(" ")
        move = movement[0]
        steps = int(movement[1])

        if move == "down":
            aim += steps
        elif move == "up":
            aim -= steps
        else:
            horizontal += steps
            depth = depth + (aim * steps)

    return horizontal * depth

result_2 = day_2_part_2()

