#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2019331076
#Newton Raphson Method
#remove comment if not installed the required modules in your pc
#!pip install matplotlib
#!pip install pandas
#!pip install numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy

def f(x, func):
    val = eval(func)
    return val


def newton_raphson(func,first_derivative,x0,iterations,error_tolerance):
    
    iteration_list = []
    prev_x = []
    xi_list = []
    error_list = []
    func_list = []
    cnt = 1
    xi = 1
    initial_guess = x0
    error = -1
    
    while cnt<=iterations:
        
        iteration_list.append(cnt)
        
        prev_x.append(x0)
        
        func_val = f(x0,func)
        first_derivative_val = f(x0,first_derivative)
        xi = x0 - (func_val/(first_derivative_val*1.00))
        
        xi_list.append(xi)
        
        if(cnt == 1):
            error_list.append(np.nan)
            
        else:
            error=( abs(x0-xi)/abs(xi*1.00) )*100.0
            error_list.append(error)
            
        func_list.append(f(xi,func))
        
        cnt = cnt + 1
        
        x0 = xi
        
    data_table = pd.DataFrame({"Iterations":iteration_list,"X(i-1)":prev_x,"Xi":xi_list,"Error(%)":error_list,"F(Xi)":func_list})
    
    print(data_table)
    
    print("The Root is "+ str(xi) + " with error "+str(error))
    if(error>error_tolerance):
        print("Can't get accurate result you wanted due to iteration limitations")
    
    
    x=[]
    y=[]
    l = initial_guess - 12
    r = initial_guess + 12
    
    while l<=r:
        x.append(l)
        y.append(f(l,func))
        l+=0.01
    
    
    x=np.array(x)
    y=np.array(y)
    plt.figure(figsize=(15,15))
    plt.subplot(2,1,1)
    plt.xlabel("X")
    plt.ylabel("F(X)")
    plt.axhline(y = 0.0, color = 'r', linestyle = '-')
    plt.axvline(x=0.0,color='r')
    plt.plot(x,y)
    x=np.array(list(data_table['Iterations']))
    y=np.array(list(data_table['Error(%)']))
    plt.subplot(2,1,2)
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.axhline(y = 0.0, color = 'r', linestyle = '-')
    plt.axvline(x=0.0,color='r')
    plt.plot(x,y)
        
    

        



print(" Please enter the function to find root using Newton-Raphson Method ")
func = input()

while True:
    print(" Please input the initial guess for finding the root ")
    x0 = input()
    x0 = float(x0)
    print("Enter the number of iterations")
    iterations = int(input())
    print("Enter the max error tolerance")
    error_tolerance = float(input())
    
    first_derivative = str(sympy.Derivative(func).doit())
    
    if(f(x0,first_derivative)==0):
        print("Division by zero error please provide another guess")
        
    else:
        newton_raphson(func,first_derivative,x0,iterations,error_tolerance)
        break
    

    

        
        
        

    
    
    
    
    

