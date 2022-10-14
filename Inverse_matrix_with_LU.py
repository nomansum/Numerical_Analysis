#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2019331076
#Inverse of Matrix using LU DECOMPOSITION


def print_matrix(matrix):
    
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("")



def get_lower_upper(mat, n):
    upper = [[0.0 for j in range(n)] for i in range(n)]
    lower = [[0.0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            upper[i][j] = mat[i][j]

    for i in range(n):
        for j in range(n):
            if(i==j):
                lower[i][j] = 1


    for j in range(0, n-1):
        for i in range(j+1, n):
            if (upper[j][j] == 0):
                return False, False
            c = upper[i][j] / upper[j][j]
            lower[i][j] = c

            for k in range(j, n):
                v = c*upper[j][k]
                upper[i][k]-=v

    return upper, lower

def preprocess(matrix,val):
    n = len(matrix)
    new_matrix = [[0.0 for j in range(n+1)] for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            new_matrix[i][j] = matrix[i][j]
    

    for i in range(0,n):
        new_matrix[i][n]=val[i]

    return new_matrix


def sol_upper(matrix , n):
    
        
    solution = [0 for k in range(n)]

    for i in range(n-1,-1,-1):
        try:
            solution[i]=matrix[i][n]/matrix[i][i]
        except:
            
            print("Division By Zerro Error. Couldn't find solution")
            return False
            
        for j in range(i-1,-1,-1):
            matrix[j][n] -= (matrix[j][i]*solution[i])


    return solution

def sol_lower(matrix,n):
    solution = [0 for k in range(n)]
    for i in range(0,n):
        solution[i]=matrix[i][n]
        for j in range(i+1,n):
            matrix[j][n] -= (solution[i] * matrix[j][i])
            
    return solution    

def lu_decompose(base,eqn_val,L,U):
    A = preprocess(L,eqn_val)
    primary_solution = sol_lower(A,len(A))
    AU = preprocess(U,primary_solution)
    result = sol_upper(AU,len(AU))
    return result

def find_inverse(base,L,U):
    n = len(base)
    inverse = [[0.0 for j in range(n)] for i in range(n)]
    for i in range(0,n):
        inverse[i][i]=1
    
    for j in range(0,n):
        eqn_val=[0.0 for k in range(n)]
        for i in range(0,n):
            eqn_val[i]=inverse[i][j]
        val = lu_decompose(base,eqn_val,L,U)
        
        for i in range(0,n):
            inverse[i][j]=val[i]
    print("Lower Matrix:")
    print_matrix(L)
    print("Upper Matrix:")
    print_matrix(U)        
        
    return inverse
    

n = int(input(" Input the number of rows "))

matrix = [[0.0 for j in range(n)] for i in range(n)]

#for i in range(0,n):
    #for j in range(0,n+1):
        #matrix[i][j]=0.0

print("Enter matrix values seperated by space to find Inverse Matrix")

for i in range(0,n):
    eqn = input("Row{} : ".format(i+1)).split()
    for j in range(0,n):
        matrix[i][j]=float(eqn[j])

base = [[0.0 for j in range(n)] for i in range(n)]

for i in range(0,n):
    for j in range(0,n):
        base[i][j]=matrix[i][j]
        
        
        
U,L = get_lower_upper(base,n)

if L == False and U == False:
    print("No solution exists")
    
else:
    
    
    
    print("")
    solution = find_inverse(base,L,U)
    print("Inverse Matrix : ")
    print_matrix(solution)

    

    
        

