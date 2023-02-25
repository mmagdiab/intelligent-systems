"""Write a program to search for a value in 2D array."""


def search(array, value):
    rows, columns = len(array), len(array[0])
    for r in range(rows):
        for c in range(columns):
            if array[r][c] == value:
                print("found , location({},{})".format(r, c))
                return r, c


arr = [[3, 0, 9],
       [4, 5, 12],
       [5, 3, 3],
       [0, 1, 0]]
search(arr, 5)
