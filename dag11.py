import requests
import numpy

data = requests.get('https://julekalender-backend.knowit.no/challenges/11/attachments/hint.txt').text.split('\n')

for word in data:
    thisword = word
    word_matrix = [list(word)]
    count = 0
    while len(word) > 1:
        word = word[1:] # remove first char

        word = [ord(x) for x in list(word)] # Find ASCII number of each char

        word = [((x - 97) + 1) % 26 for x in word] # push each char up

        word = [(el + ord(word_matrix[count][i])-97) % 26 for i, el in enumerate(word)] # Add pos of above char

        word = [chr(x + 97) for x in word] # ASCII -> String
        
        word_matrix.append(word)
        count += 1

    columns = []

    for length in range(len(word_matrix[0])):
        [columns.append(word_matrix[i][length]) for i in range(len(word_matrix))]
        word_matrix.pop()

    password = ''.join(columns)
    if 'eamqia' in password:
        print(f'The password is: {thisword}')