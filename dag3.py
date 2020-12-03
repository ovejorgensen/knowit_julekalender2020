import numpy as np

RESULT_SET = set()

with open("files/wordlist.txt", "r", encoding="utf-8") as f2:
    WORDS = np.array([word for word in f2.read().splitlines()])

with open("files/matrix.txt", "r", encoding="utf-8") as f1:
    M = np.array([list(line) for line in f1.read().splitlines()])

def horizontals(matrise):
    for row in matrise:
        row_joined = "".join(row)
        [RESULT_SET.add(word) for word in WORDS if word in row_joined]

def diagonals(ndarr):
    diag_arr = ndarr.copy()
    dimension_y = dimension_x = 1000
    before = dimension_x - 1
    after = 0

    result = np.chararray((dimension_y, dimension_x*2-1), unicode="utf-8")

    for i, row in enumerate(diag_arr):
        result[i] = np.concatenate((np.chararray(before, unicode="utf-8"), row, np.chararray(after, unicode="utf-8")))
        before -= 1
        after += 1

    horizontals(result.transpose())
    horizontals(np.fliplr(result.transpose()))


[horizontals(item) for item in (M, np.fliplr(M), M.transpose(), np.fliplr(M.transpose()))]
[diagonals(item) for item in (M, np.fliplr(M), M.transpose(), np.fliplr(M.transpose()))]

[print(word) for word in WORDS if word not in RESULT_SET]
