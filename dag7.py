with open('files/forest.txt', "r") as f:
    data = f.readlines()

total = 0

hash_indices = [i for i, hashtag in enumerate(data[34]) if hashtag == "#"]

def check_symmetry(i):
    for el in data[::-1]:
        symmetrical = False
        count = 0
        while not symmetrical:
            if el[i+count] == "#" and el[i-count] == "#":
                count += 1
            elif el[i+count] == " " and el[i-count] == " " and el[i+count+1] == " " and el[i-count-1] == " ":
                symmetrical = True
            else:
                return False
    return True

for i in hash_indices:
    if check_symmetry(i):
        total += 1

print(f"Number of symmetrical trees: {total}")
