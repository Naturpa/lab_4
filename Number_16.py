def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence += [next_element] #создается копия sequence, а метод append меняет текущее состояние.

sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)
