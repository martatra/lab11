def print_square(square):
    for row in square:
        for cell in row:
            print("{:6}".format(cell), end=" ")
        print()


def check_square(square):
    N = len(square)
    magic_k = N*(N*N + 1)/2
    
    # check row
    for i in range(N):
        sum_row = 0
        incomplete = False
        for j in range(N):
            if square[i][j] == 0:
                incomplete = True
            sum_row += square[i][j]
        if not incomplete and sum_row != magic_k or incomplete and sum_row >= magic_k:
            return False
        
    # check col
    for i in range(N):
        sum_col = 0
        incomplete = False
        for j in range(N):
            if square[j][i] == 0:
                incomplete = True
            sum_col += square[j][i]
        if not incomplete and sum_col != magic_k or incomplete and sum_col >= magic_k:
            return False
        
    # check diag1
    incomplete = False
    sum_diag = 0
    for i in range(N):
        if square[i][i] == 0:
            incomplete = True
        sum_diag += square[i][i]
    if not incomplete and sum_diag != magic_k or incomplete and sum_diag >= magic_k:
        return False
        
    # check diag 2
    incomplete = False
    sum_diag = 0
    for i in range(N):
        if square[i][N -i -1] == 0:
            incomplete = True
        sum_diag += square[i][N-i-1]
    if not incomplete and sum_diag != magic_k or incomplete and sum_diag >= magic_k:
        return False
    
    return True


def create_square(N):
    square = [[0]*N for i in range(N)]
    to_insert = {i+1 for i in range(0, N*N)}
    populate_square(square, 0, to_insert)
    return square


def populate_square(square, pos, to_insert):
    if not check_square(square):
        return False
    if not to_insert:
        return True
    row = pos // len(square)
    col = pos % len(square)
    for num in to_insert:
        square[row][col] = num
        if populate_square(square, pos+1, to_insert - {num}):
            return True
        square[row][col] = 0
    return False


def main():
    square = create_square(4)
    print_square(square)


if __name__ == "__main__":
    main()
