def flip_vertical_axis(matrix):

    rows = len(matrix) - 1
    columns = len(matrix[0]) - 1

    i = 0
    j = 0

    while i <= rows:
       while j <= (c//2):
            temp = 0
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][c-j]
            matrix[i][c-j] = temp

            j += 1
        i += 1
