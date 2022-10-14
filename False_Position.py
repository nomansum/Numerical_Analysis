#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2019331076
#False Position
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



def false_position(func, l, r, iterations, error_tolerance):
    cnt = 1
    prev_val = ((r*f(l,func)*1.0) - (l*f(r,func)*1.0))/(f(l,func) - f(r,func))
    xm = -1
    error = 0    
    error_list = []
    Iteration_list=[]
    Xu = []
    Xl=[]
    Xm=[]
    func_list=[]
    ll = l
    rr = r

    while cnt <= iterations:
        cnt = cnt + 1
        xm = ((r*f(l,func)*1.0) - (l*f(r,func)*1.0))/(f(l,func) - f(r,func))
        new_val = f(xm, func)
        
        Xl.append(l)
        Xu.append(r)
        Xm.append(xm)
        Iteration_list.append((cnt-1))
        func_list.append(new_val)

        if (cnt == 2):

            
            
            error_list.append(np.nan)
            

        else:
            error = abs(xm - prev_val) / abs(xm * 1.00)
            error = error * 100.0
            error_list.append(error)
            
            
        prev_val = xm    
            
            

        if ((f(xm, func) * f(l, func)) < 0):
            r = xm
        else:
            l = xm
    data_table = pd.DataFrame({"Iteration":Iteration_list, "Xl":Xl, "Xu":Xu, "Xm":Xm, "Error(%)":error_list, "f(Xm)":func_list})
                              
    data_table.set_index("Iteration")
    print(data_table)
    print("The Root is "+ str(xm) + " with error "+str(error))
    if(error>error_tolerance):
        print("Can't get accurate result you wanted due to iteration limitations")
    
    
    x=[]
    y=[]
    if ll>rr:
        tmp = rr
        rr = ll
        ll=tmp
    while ll<=rr:
        x.append(ll)
        y.append(f(ll,func))
        ll = ll + 0.01
        
    
    x=np.array(x)
    y=np.array(y)
    plt.figure(figsize=(15,15))
    plt.subplot(2,1,1)
    plt.xlabel("X")
    plt.ylabel("F(X)")
    plt.axhline(y = 0.0, color = 'r', linestyle = '-')
    plt.axvline(x=0.0,color='r')
    plt.plot(x,y)
    x=np.array(Iteration_list)
    y=np.array(error_list)
    plt.subplot(2,1,2)
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.axhline(y = 0.0, color = 'r', linestyle = '-')
    plt.axvline(x=0.0,color='r')
    plt.plot(x,y)
    



print(" Please enter the function to find root using False position Method ")
func = input()

while True:
    print(" Please input the lower limit for finding the root ")
    a = input()
    a = float(a)
    print(" Please input the upper limit for finding the root ")
    b = input()
    b = float(b)
    print("Enter the number of iterations")
    iterations = int(input())
    print("Enter the max error tolerance")
    error_tolerance = float(input())

    if (f(a, func) * f(b, func) < 0):
        false_position(func, a, b, iterations, error_tolerance)
        break
    else:
        print("Not a valid range")

