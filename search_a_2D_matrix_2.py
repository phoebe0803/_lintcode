
def searchMatrix(matrix, target):
    last=len(matrix)-1
    left_corner=matrix[last][0]

    while target !=left_corner :
        if target>left_corner:
            for i in matrix:
                del i[0]
        else:
            matrix.pop(last)
        //1.consider the last row pop out  then matrix is empty
        //2.consider every column del then matrix[[],[],[],[]]
        // above all ,consider two different  edge condition
        if matrix:
            last = len(matrix)-1
            if last>=0:
                if matrix[0]:
                    left_corner = matrix[last][0]
                else:
                     return False
        else:
            return False
    if target == left_corner:
        return True


if __name__=='__main__':
    matrix=[[5]]
    print(searchMatrix(matrix,2))


