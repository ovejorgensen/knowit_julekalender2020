with open('numbers.txt', 'r') as file:
    file = [int(x) for x in file.read().split(",")]
    file = [print(x) for x in range(file[0], file[-1]+1) if x not in sorted(file)]