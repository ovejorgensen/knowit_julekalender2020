cakes = melk = mel = sukker = egg = 0
with open("files/leveringsliste.txt", "r") as f:
    rows = f.read().splitlines()

for row in rows:
    row = row.split(",")
    for el in row:
        val = int(el.split(":")[1])
        if 'melk:' in el:
            melk += val
        elif 'mel:' in el:
            mel += val
        elif 'sukker:' in el:
            sukker += val
        else:
            egg += val
    
while(not ((melk - 3 < 0) or (mel - 3 < 0) or (sukker - 2 < 0) or (egg - 1 < 0))):
    melk -= 3
    mel -= 3
    sukker -=2
    egg -=1
    cakes += 1

print(f"Number of cakes: {cakes}")