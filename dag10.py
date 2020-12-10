import requests
data = requests.get('https://julekalender-backend.knowit.no/challenges/10/attachments/leker.txt').text.split('\n')

elves = {}
for row in data:
    row = row.split(',')
    for i, elf in enumerate(row):
        if elf not in elves:
            elves[elf] = len(row) - i-1
        else:
            elves[elf] += len(row) - i-1
            
winner = max(elves.items(), key=lambda x:x[1])

print(f'Winner: {winner[0]}-{winner[1]}')
