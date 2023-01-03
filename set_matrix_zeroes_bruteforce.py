# This is problem 73 on Leetcode
def setZeroes( matrix):
    """
    Brute Force Algorithm:
    1. Iterate through matrix, if element 0 found at row i column j, makr all elements in that row,column as -1.
    2. Iterate through the intermediate matrix to replace all -1s (Nones) to 0.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j] == 0:
                for R in range(rows):
                    if matrix[R][j] != 0: #if we find an addtl 0, don't change to -1
                        matrix[R][j] = None
                for C in range(cols):
                    if matrix[i][C] != 0: #if we find an addtl 0, don't change to -1
                        matrix[i][C] = None
            j += 1
        i += 1

    #iterate again thru matrix to switch all -1s to 0
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j] == None:
                matrix[i][j] = 0
            j += 1
        i += 1

    #print formatted matrix:
    for x in range(rows):
        print(matrix[x])
# ------------------------------------------------------
if __name__ == '__main__':
    #define hardcoded matrix to pass into function:
    my_matrix = [[1,1,1],[1,0,1],[1,1,1]]
    #call function:
    print("Brute Force Solution:")
    setZeroes(my_matrix)