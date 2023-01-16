
def spiralOrder(matrix):
    result = []
    s_row = 0
    s_col = 0
    len_row = len(matrix)
    len_col = len(matrix[0])

    while s_row < len_row and s_col < len_col:
        # Go from Left --> Right
        for i in range(s_col, len_col):
            result.append(matrix[s_row][i])
            print("L->R  "+ str(matrix[s_row][i]))
        # increment start of row
        s_row += 1

        # Go from top --> bottom, iterating through rows of last col
        for j in range(s_row, len_row):
            result.append(matrix[j][len_col - 1])
            print("top -> bottom " + str(matrix[j][len_col - 1]))
        # decrement max column
        len_col -= 1

        # make sure rows do not overlap, because we go from R->L now
        if s_row < len_row:
            # move from R->Left
            for j in reversed(range(s_col, len_col)):
                result.append(matrix[len_row - 1][j])  # changing cols, keeping rows fixed
                print("R->L " + str(matrix[len_row -1][j]))
            # decrement the row, so that you don't visit the last row again
            len_row -= 1

        # move from bottom --> top
        if s_col < len_col:
            for i in reversed(range(s_row, len_row)):
                result.append(matrix[i][s_col])
                print("bottom -> top " + str(matrix[i][s_col]))
            # increment the column
            s_col += 1

    return result


if __name__ == '__main__':
    #define hardcoded matrix to pass into function:
    my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    my_matrix2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    #call function:

    result = spiralOrder(my_matrix)
    for i in result:
        print(i)
