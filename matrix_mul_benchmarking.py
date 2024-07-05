import random
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

def create_mat(m,n):
    main_list=[]
    for i in range(m):
        temp_list=[]
        for j in range(n):
            random_number = random.randint(0,9)
            temp_list.append(random_number)
        main_list.append(temp_list)
    #array = np.array(main_list)    
    return main_list

def matrix_mul(matrix_1, matrix_2):
    if len(matrix_1[0]) == len(matrix_2):        
        result_rows = len(matrix_1)
        result_cols = len(matrix_2[0])
        result_matrix = [[0 for _ in range(result_cols)] for _ in range(result_rows)]
        for i in range(result_rows):
            for j in range(result_cols):
                sum = 0
                for k in range(len(matrix_2)):
                    sum += matrix_1[i][k] * matrix_2[k][j]
                result_matrix[i][j] = sum        
        return result_matrix  

def row_major_mul (matrix_1, matrix_2):
    row_major_1 = []
    row_major_2 = []
    for i in range(len(matrix_1)):
        for k in range(len(matrix_1[0])):
            row_major_1.append(matrix_1[i][k])
    for i in range(len(matrix_2)):
        for k in range(len(matrix_2[0])):
            row_major_2.append(matrix_2[i][k])   
    print(row_major_1)
    print(row_major_2)
    matrix_1_row = len(matrix_1)
    #matrix_1_column = len(matrix_1[0])
    matrix_2_row = len(matrix_2)
    matrix_2_column = len(matrix_2[0])
    if len(matrix_1[0]) == len(matrix_2):        
        result_matrix = []
        for i in range(matrix_1_row):
            for j in range(matrix_2_column):
                sum = 0
                for k in range(matrix_2_row):
                    sum += row_major_1[(matrix_1_row*i)+k] * row_major_2[(matrix_2_row*k)+j]
                result_matrix.insert(((matrix_1_row*i)+j),sum)    
        return result_matrix 

def optim_mul (matrix_1, matrix_2, z):
    row_major_1 = []
    row_major_2 = []
    for i in range(len(matrix_1)):
        for k in range(len(matrix_1[0])):
            row_major_1.append(matrix_1[i][k])
    for i in range(len(matrix_2)):
        for k in range(len(matrix_2[0])):
            row_major_2.append(matrix_2[i][k])  
    print(matrix_1)
    print(matrix_2) 
    matrix_1_row = len(matrix_1)
    matrix_2_row = len(matrix_2)
    matrix_2_column = len(matrix_2[0])
    if len(matrix_1[0]) == len(matrix_2):        
        temp = matrix_1_row - z
        while (temp>0):        
            for i in range(0,z):     
                result_matrix = []           
                for j in range(0,matrix_2_column):                    
                    sum = 0
                    for k in range(matrix_2_row):
                        sum += row_major_1[(matrix_1_row*i)+k] * row_major_2[(matrix_2_row*k)+j]
                    result_matrix.append(sum)     
                print(result_matrix)           
            z+=-1     
            temp+=-1
             

def benchmark():
    xpoint = []
    ypoint = []
    tflops = []
    for i in range(1,501,51):  
        xpoint.append(i)    
        time_start = perf_counter()
        matrix_1 = create_mat(i,i)
        matrix_2 = create_mat(i,i)
        matrix_mul(matrix_1,matrix_2)
        time_end = perf_counter()
        time_duration = time_end - time_start
        ypoint.append(time_duration)
        print(f'{time_duration}s')
        flops = (i*i*(2*i)-1)
        flops_sec = flops/time_duration
        tflops.append(flops_sec)       
    x_array = np.array(xpoint)
    y_array = np.array(ypoint)
    flops_array = np.array(tflops)
    plt.plot(x_array,flops_array)
    plt.xlabel('Size of Matrix')
    plt.ylabel('flops/s')
    plt.show()

#benchmark()
n = 3
bm = 2
matrix_1 = create_mat(n,n)
matrix_2 = create_mat(n,n)
optim_mul(matrix_1,matrix_2,bm)
'''
mat1_n = np.array(matrix_1).reshape(n, n)
mat2_n = np.array(matrix_2).reshape(n, n)
mato = np.matmul(mat1_n, mat2_n).flatten()

print(np.allclose(mato, matrix_res))
'''