import requests
import matplotlib.pyplot as plt

response = requests.get('https://julekalender-backend.knowit.no/challenges/5/attachments/rute.txt')
data = response.text

arr = [(0, 0)]
for el in data:
    if el == 'H':
        arr.append((arr[-1][0]+1, arr[-1][1]))
    elif el == 'V':
        arr.append((arr[-1][0]-1, arr[-1][1]))
    elif el == 'O':
        arr.append((arr[-1][0], arr[-1][1]+1))
    else:
        arr.append((arr[-1][0], arr[-1][1]-1))

def find_area(array):
    a = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        ox,oy = x,y
    return a/2

print(f"Area: {abs(find_area(arr))}")

x = [x[0] for x in arr]
y = [y[1] for y in arr]
plt.plot(x, y)
plt.fill(x, y)
plt.show()


