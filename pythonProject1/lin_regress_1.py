import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading and visualizing data 

CSV_Data = pd.read_csv("D:/Semester 6/Machine Learning/Assignment 1/canada_per_capita_income.csv", header=None)
CSV_Data = CSV_Data.replace(np.NaN,0)

X = CSV_Data.iloc[:,0]
Y = CSV_Data.iloc[:,1]

#Convert in 2 Rank

X = np.array(X)
Y = np.array(Y)
X = X[:,np.newaxis]
Y = Y[:,np.newaxis]

#Scaling_Of_X

min_x = X.min()
max_x = X.max()
scale_x_numerator = X-min_x
scale_x_denominator = max_x-min_x #2017-min_x 
scale_x = scale_x_numerator/scale_x_denominator

#Scaling_Of_Y

min_y = Y.min()
max_y = Y.max()
scale_y_numerator = Y-min_y
scale_y_denominator = max_y-min_y
scale_y = scale_y_numerator/scale_y_denominator

#print(scale_x)
#print(scale_y)

# Having Extra Column With Values 1 for theta 0

m,col = scale_x.shape
ones = np.ones((m,1))
scale_x = np.hstack((ones,scale_x))

theta = np.zeros((2,1))
iterations = 10000
alpha = 0.01

# Defining Cost function

def Get_cost_J(X,Y,Theta):
    Pridictions = np.dot(X,Theta)
    Error = Pridictions-Y
    SqrError = np.power(Error,2)
    SumSqrError = np.sum(SqrError)
    J  = (1/2*m)*SumSqrError # Where m is total number of rows
    return J

#Defining Gradient Decent Algorithm

def Gradient_Decent_Algo(X,Y,Theta,alpha,itrations,m):
    histroy = np.zeros((itrations,1))
    for i in range(itrations):
        temp =(np.dot(X,Theta))-Y
        temp = (np.dot(X.T,temp))*alpha/m
        Theta = Theta - temp
        histroy[i] = Get_cost_J(X, Y, Theta)
       
    return (histroy,Theta)

h,t = Gradient_Decent_Algo(scale_x, scale_y, theta, alpha, iterations, m)

final_prediction = np.dot(scale_x,t)

plt.scatter(scale_x[:,1],scale_y)
plt.plot(scale_x[:,1],final_prediction,color="red")
plt.show()

#now scaling year 2020

xnew_numerator = 2020-min_x
xnew_denomenator = max_x-min_x
x_new = xnew_numerator/xnew_denomenator

#Now Predict the salary of year 2020

t0 = t[0,0]
t1 = t[1,0]

predict_new_value = t0+(t1*x_new)

salary_predicted_final = predict_new_value*(max_y-min_y)+min_y

print(salary_predicted_final)














