import requests
data = requests.get('https://julekalender-backend.knowit.no/challenges/9/attachments/elves.txt').text.split("\n")

data = [list(row) for row in data]

check = [(0,1), (0,-1), (1,0), (-1,0)]

def check_S(i, j):
    num_S = 0
    for row, col in check:
        try:
            if data[i+row][j+col] == 'S': 
                num_S += 1
        except IndexError:
            pass
    return num_S

days = 0
spreading = True
while spreading:
    next_day = [row[:] for row in data]
     
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == 'F' and check_S(i, j) >= 2:            
                next_day[i][j] = 'S'

    days += 1

    if next_day == data:
        spreading = False
    else:
        data = next_day

print(f"Days until smitten stanser opp: {days}")

