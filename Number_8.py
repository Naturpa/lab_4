def tic_tac_toe(field):
    tr_field = list(zip(*field))
    for symb in ('x', '0'):
        for F in (field, tr_field):
            for i in range(3):
                if ''.join(F[i]) == symb * 3:
                    return print(f'{symb} win')
        if field[0][0] + field[1][1] + field[2][2] == symb * 3 \
                or field[0][2] + field[1][1] + field[2][0] == symb * 3:
            return print(f'{symb} win')
    print('draw')


data = """x x 0
          - x 0
          x 0 0"""
field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)
