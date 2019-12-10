import numpy as np

def rowop(matrix, a, b, k):
    for i in range(len(matrix[0])):
        matrix[a][i] -= k*matrix[b][i]

def gauss(matrix):
    for j in range(len(matrix)):
        rowop(matrix, j, j, 1-1/matrix[j][j])
        for l in range(len(matrix)):
            if(j!=l):
                rowop(matrix,l, j, matrix[l][j])
    return [[matrix[0][3]],[matrix[1][3]], [matrix[2][3]]] 

def gauss_jacobi(matrix, x0, y0, z0, v0, n):
    x = x0
    y = y0
    z = z0
    v = v0
    for i in range(n):
        
        x = (matrix[0][3] - matrix[0][1]*y0 - matrix[0][2]*z0 - matrix[0][3]*v0) / matrix[0][0]
        y = (matrix[1][3] - matrix[1][0]*x0 - matrix[1][2]*z0 - matrix[1][3]*v0) / matrix[1][1]
        z = (matrix[2][3] - matrix[2][0]*x0 - matrix[2][1] * y0 - matrix[2][3]*v0) / matrix[2][2]
        v = (matrix[3][3] - matrix[3][0]*x0 - matrix[3][1] * y0 - matrix[3][2]*z0) / matrix[3][3]
        #print([x, y, z, v])
        
        x0 = x
        y0 = y
        z0 = z
        
    return [x, y, z]
  
m = [[4.5, -1.0, -1.0, 1.0, 1.0],[-1.0, 4.5, 1.0, -1.0, -1.0],[-1.0, 2.0, 4.5, -1.0, -1.0], [2.0, -1.0, -1.0, 4.5, 0.0]]      
print("JACOBI: ", gauss_jacobi(m, 0.25, 0.25, 0.25, 0.25, 2))    


a = [[18,-1, 1],[3, -5, 4],[6, 8, 29]]
b = [[10],[2],[-1]]

#print(np.linalg.solve(a, b))

#b-a.x0~
x0 = gauss(m)

res = np.subtract(b, np.matmul(a, x0))
print("\nRESIDUO: \n\n", res)

int_stab = np.matmul(np.linalg.inv(a), res)
print("\nINTERNAL STABILITY: \n\n", int_stab)

#external statibility with deltaA and deltaB IGUAL TO 0.1

deltaA = [[0.1,0.1,0.1], [0.1,0.1,0.1], [0.1,0.1,0.1]]
deltaB = [[0.1], [0.1,], [0.1]]

x0 =[[0.552949],[-0.15347],[-0.10655]]

ext_stab = np.matmul(np.linalg.inv(a), np.subtract(deltaB, np.matmul(deltaA, x0)))
print("\nEXTERNAL STABILITY: \n\n", ext_stab)
