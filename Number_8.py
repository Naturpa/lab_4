def tic_tac_toe(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != '-':
            return f"{field[i][0]} win"
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != '-':
            return f"{field[0][i]} win"

    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '-':
        return f"{field[0][0]} win"
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '-':
        return f"{field[0][2]} win"

    if all(cell != '-' for row in field for cell in row):
        return "draw"

    return "draw"


print(tic_tac_toe([["x", "0", "x"], ["0", "x", "0"], ["x", "-", "0"]]))
