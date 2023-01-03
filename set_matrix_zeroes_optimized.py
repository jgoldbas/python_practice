# This is problem 73 on Leetcode
def setZeroes(matrix):
    # Time complexity is better here
    rows = len(matrix)
    cols = len(matrix[0])

    rows_set = set()
    cols_set = set()

    # iterate through input matrix
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j] == 0:  # if element 0 found at row i, col j
                rows_set.add(i)  # store index of row to be assigned to 0
                cols_set.add(j)  # store index of col to be assigned to 0
            j += 1
        i += 1

    # iterate again thru matrix and check values w/in the rows_set and cols_set
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if i in rows_set or j in cols_set:
                matrix[i][j] = 0
            j += 1
        i += 1
    # print formatted matrix:
    for x in range(rows):
        print(matrix[x])
# ------------ main -----------------------------
if __name__ == '__main__':
    print("Optimized Solution:")
    my_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(my_matrix)