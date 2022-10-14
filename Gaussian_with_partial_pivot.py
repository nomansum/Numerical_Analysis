#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2019331076
#GAUSSIAN WITH PARTIAL PIVOTING



def print_matrix(matrix):
    
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("")
    

def gaussian_parial_pivoting(matrix , n):
    step = 1
    for i in range(0,n-1):
        
        max_row, val = i, 0
        for j in range(i, n):
            if(abs(matrix[j][i]) > val):
                val = abs(matrix[j][i])
                max_row = j  
        
        for k in range(0, n+1):
            matrix[i][k],matrix[max_row][k] = matrix[max_row][k],matrix[i][k]
        
        for j in range(i+1,n):
            
            try:
                val = matrix[j][i]/matrix[i][i]
                
            except:
                print("Division By Zerro Error. Couldn't find solution")
                return False
                
            for k in range(i,n+1):
                matrix[j][k]-= (val*matrix[i][k])
        
        print("After Step {} :".format(step))
        print_matrix(matrix)
        step = step + 1
        
        

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



number_of_eqn = int(input("Input the number of equations"))

matrix = [[0.0 for j in range(number_of_eqn+1)] for i in range(number_of_eqn)]

#for i in range(0,n):
    #for j in range(0,n+1):
        #matrix[i][j]=0.0

print("Enter coefficients of equations in ax^n+bx^(n-1)+...+c = d format seperated by space")

for i in range(0,number_of_eqn):
    eqn = input("Equation{} : ".format(i+1)).split()
    for j in range(0,number_of_eqn+1):
        matrix[i][j]=float(eqn[j])

print("")
solution = gaussian_parial_pivoting(matrix,number_of_eqn)
print("Solution for SLE : ",end="")
print(solution)

