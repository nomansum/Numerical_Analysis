#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 2019331076
#Secant Method
#remove comment if not installed the required modules in your pc
#!pip install matplotlib
#!pip install pandas
#!pip install numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *

def f(x, func):
    val = eval(func)
    return val


def secant_method(func,x0,x1,iterations,error_tolerance):
    
    iteration_list = []
    
    Xi_prev = []
    
    Xi = []
    
    Xi_1 = []
    
    error_list = []
    
    func_list = []
    
    cnt = 1
    xi = 1
    
    while cnt<=iterations:
        
        iteration_list.append(cnt)
        
        
        Xi_prev.append(x0)
        
        Xi.append(x1)
        
        try:
            xi = x1 - ( ( f(x1,func) * (x1 - x0) )/ ( f(x1,func) - f(x0,func) )*1.00   )
            
        except:
            print("Division By Zero Error Before completing provided iterations")
            Xi_1.append(Xi_1[-1])
            error_list.append(error_list[-1])
            func_list.append(func_list[-1])
            break
            
            
        Xi_1.append(xi)
        
        x0=x1
        x1=xi
        
        if(cnt == 1):
            error_list.append(np.nan)
            
        else:
            error=( abs(xi-x0)/abs(xi*1.00) )*100.0
            error_list.append(error)
            
        func_list.append(f(xi,func))
        
        cnt = cnt + 1
        
        
        
    data_table = pd.DataFrame({"Iterations":iteration_list,"X(i-1)":Xi_prev,"X(i)":Xi,"X(i+1)":Xi_1,"Error(%)":error_list,"F(Xi)":func_list})
    
    print(data_table)
    
    print("The Root is "+ str(xi) + " with error "+str(error))
    if(error>error_tolerance):
        print("Can't get accurate result you wanted due to iteration limitations")
    
    
    
    
    x=np.array(Xi_1)
    y=np.array(func_list)
    plt.figure(figsize=(15,15))
    plt.subplot(2,1,1)
    plt.xlabel("X")
    plt.ylabel("F(X)")
    plt.axhline(y = 0.0, color = 'r', linestyle = '-')
    plt.axvline(x=0.0,color='r')
    plt.plot(x,y)
    x=np.array(iteration_list )
    y=np.array(error_list)
    plt.subplot(2,1,2)
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.axhline(y = 0.0, color = 'r', linestyle = '-')
    plt.axvline(x=0.0,color='r')
    plt.plot(x,y)
        
    

        



print(" Please enter the function to find root using Secant Method ")
func = input()

while True:
    print(" Please input the X(-1) guess for finding the root ")
    x0 = float(input())
    print("Please input the X(0) guess for finding the root")
    x1 = float(input())
    print("Enter the number of iterations")
    iterations = int(input())
    print("Enter the max error tolerance")
    error_tolerance = float(input())
    
    if(f(x1,func)-f(x0,func)==0):
        print("Division by zero error please provide another guess")
        
    else:
        secant_method(func,x0,x1,iterations,error_tolerance)
        break
    

    

        
        
        

    
    
    
    
    

