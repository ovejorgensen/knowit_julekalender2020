import requests

ordbok = requests.get('https://julekalender-backend.knowit.no/challenges/15/attachments/wordlist.txt').text.split('\n')
ordpar = requests.get('https://julekalender-backend.knowit.no/challenges/15/attachments/riddles.txt').text.split('\n')
ordpar.pop() #remove trailing whitespace

ordbok = {x for x in ordbok}
limord = set()

for word in ordbok:
    for par in ordpar:
        first, second = par.replace(' ', '').split(',')
        if first+word in ordbok and word+second in ordbok:
            limord.add(word)
    
bokstaver = sum([len(x) for x in limord])

print(f'Antall bokstaver til sammen : {bokstaver}')