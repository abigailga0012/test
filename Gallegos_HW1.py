#Matrix A and B
A = [[1, 3, 7],
    [5, 1, 2],
    [0, 1, 2]]

B = [[2,0,1],
    [4,1,3],
    [3,5,2]]

# Part 2.1 (Python Programming):
def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Number of columns in A must be equal to the number of columns in B")

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

print(matrix_multiplication(A,B))
#Part 2.2.a:
import numpy as np
#Matrix A and B NUMPY
arr1 = np.array(A)
arr2 = np.array(B)
Numpy_matrixresult = np.dot(arr1,arr2)
print(Numpy_matrixresult)
#Part 2.2.b:
import time
start_time = time.perf_counter()
matrix_multiplication(A,B)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)

start_time_np = time.perf_counter()
Numpy_matrixresult
end_time_np = time.perf_counter()
elapsed_time_np = end_time_np - start_time_np
print(elapsed_time_np)

#2.2. The fastest method is the numpy package. Python packages are faster since these have been optimized to perform at faster rates