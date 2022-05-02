from array import array
from sys import stdin

"""
Function will take a 2D array and check if cells with value of 1. If 0, then set new array index to 0 automatically. 
If so, it will then check if there are at least 3 neighbors with a value of also 1. (8 max neighbors)  
If so, then set new array index to 1, otherwise 0.
"""

"""
TEST CASE:
ARRAY:  [[1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]]
ANSWER: [[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]]
"""

Rows = int(input("Enter the number of Rows: "))
Columns = int(input("Enter the number of Rows: "))

# Will take user input to fill the array and also create an empty array of same size
arr = []
arr_final = []
for i in range(Rows):
    a = []
    b = []
    for j in range(Columns):
        a.append(int(input()))
        b.append(0)
    arr.append(a)
    arr_final.append(b)

# Will check all possible nieghbors that do not cause Index OOB Error
for i in range(Rows):
    for j in range(Columns):
        count = int(0)

        if arr[i][j] == 1:
            # Top Left
            if i != 0 and j != 0:
                if arr[i - 1][j - 1] == 1:
                    count += 1

            # Top
            if i != 0:
                if arr[i - 1][j] == 1:
                    count += 1

            # Top Right
            if i != 0 and j != (Columns - 1):
                if arr[i - 1][j + 1] == 1:
                    count += 1

            # left
            if j != 0:
                if arr[i][j - 1] == 1:
                    count += 1

            # right
            if j != (Columns - 1):
                if arr[i][j + 1] == 1:
                    count += 1

            # Botom Left
            if i != (Rows - 1) and j != 0:
                if arr[i + 1][j - 1] == 1:
                    count += 1

            # Bottom
            if i != (Rows - 1):
                if arr[i + 1][j] == 1:
                    count += 1

            # Bottom Right
            if i != (Rows - 1) and j != (Columns - 1):
                if arr[i + 1][j + 1] == 1:
                    count += 1

        # Checks the count and sets value of new array
        if count >= 3:
            arr_final[i][j] = 1
        else:
            arr_final[i][j] = 0

print(arr_final)
