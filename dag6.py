import requests

data = requests.get('https://julekalender-backend.knowit.no/challenges/6/attachments/godteri.txt').text.split(",")
data = [int(x) for x in data]
ELVES = 127

elf_list = [0]*ELVES
done = False
while not done:
    for box in data:
        for i in range(box):
            lowest_index = elf_list.index(min(elf_list))
            elf_list[lowest_index] +=1
    if all(x == elf_list[0] for x in elf_list):
        done = True
    else:
        data.pop()
        print(len(data))
        elf_list = [0]*ELVES

print(f"Antall biter: {elf_list}")
