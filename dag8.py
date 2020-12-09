import requests
data = requests.get('https://julekalender-backend.knowit.no/challenges/8/attachments/input.txt').text.split('\n')

# Fikser opp i denne senere :))
locations = {key_val.split(':')[0]:{'location':(int(key_val.split(':')[1].split(',')[0].replace('(','')), int(key_val.split(':')[1].split(',')[1].replace(')', ''))), 'time':0} for key_val in data if ':' in key_val}

data = [item.split(':')[0] if ':' in item else item for item in data]
data.pop() # Remove the empty last line

def travel_to_location(current_location, target):
    target_x = locations[target]['location'][0]
    target_y = locations[target]['location'][1]
    current_x = current_location[0]
    current_y = current_location[1]

    while not current_x == target_x:
        if current_x < target_x:
            current_x += 1
        else:
            current_x -= 1
        update_times((current_x, current_y))

    while not current_y == target_y:
        if current_y < target_y:
            current_y += 1
        else:
            current_y -= 1
        update_times((current_x, current_y))


def update_times(current_location):
    for target in locations:
        target_location = locations[target]['location']
        steps = abs(current_location[0] - target_location[0]) + abs(current_location[1] - target_location[1])
        if target_location == current_location:
            continue
        elif steps < 5:
            locations[target]['time'] += 0.25
        elif steps < 20:
            locations[target]['time'] += 0.5
        elif steps < 50:
            locations[target]['time'] += 0.75
        else:
            locations[target]['time'] += 1

current_location = (0,0)
for target in data[50::]:
    if target == '': continue
    travel_to_location(current_location, target)
    current_location = locations[target]['location']

difference = set()
for i in locations:
    for j in locations:
        difference.add(abs(locations[i]['time']-locations[j]['time']))

print(f"Største tidsforskjell: {max(difference)}")
