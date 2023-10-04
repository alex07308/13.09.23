map = [
    [0, 0, 'x'],
    [0, 0, 0],
    [0, 't', 0],
]

def get_path(map:list) -> str:
    x = None
    t = None
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'x':
                x = (i,j)
            elif map[i][j] =='t':
                t = (i,j)
    shift_x = t[1] - x[1]
    shift_y = t[0] - x[0]
    hor_dir = 'E' if shift_x > 0 else 'W'
    vert_dir = 'S' if shift_y > 0 else 'N'

    return hor_dir * abs(shift_x) + vert_dir * abs(shift_y)

print(get_path(map))
