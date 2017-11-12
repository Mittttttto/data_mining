#coding=utf-8
'''
Created on 2017年11月10日

@author: wenmao
'''
import math
import tools
import numpy as np
alpha=0.5
x_list=[1,2,0,6,4,5]
y_list=[0,0,0,1,1,1]

theta1_list=[]
theta2_list=[]
sim_list=[0,0]

def sigmoid(x=0):
    return 1/(1+math.e**(-x))
    


def logistic():
    theta1=0
    theta2=0
    loop_time=0
    while True:
        sim=1
        for i in range(0,len(x_list)):
            f=theta1*x_list[i]+theta2
            y_tmp=sigmoid(f)
            theta1=theta1+alpha*x_list[i]*(y_list[i]-y_tmp)
            theta2=theta2+alpha*(y_list[i]-y_tmp)
            sim=sim*(y_tmp**y_list[i])*((1-y_tmp)**(1-y_list[i]))
        sim_list[0]=sim
        print "sim is "+str(sim)
        theta1_list.append(theta1)
        theta2_list.append(theta2)    
        if sim > 0.9999:
            break
        sim_list[1]=sim_list[0]
        loop_time=loop_time+1
        if loop_time >1000000:
            print "fail"
            break


if __name__ == '__main__':
    logistic()
    
    def get_tmp_y(theta1,theta2,x):
        return theta1*x+theta2
    x = np.arange(1,6,0.0001)
    xs =[]
    ys= []
    label_text=[]
#     for i in range(0,len(theta1_list)):
#         print "regression time "+ str(i)+" theta1 is "+str(theta1_list[i])+" theta2 is " +str(theta2_list[i])
#         xs.append(x)
#         #ys.append(get_tmp_y(theta1_list[i],theta2_list[i],x))
#         ys.append(sigmoid(get_tmp_y(theta1_list[i],theta2_list[i],x)))
#         label_text.append("line "+ str(i))
#     tools.matplot.drawlines(xs, ys,label_text)
    
    
    xs =[]
    ys= []
    xs.append(x)
        #ys.append(get_tmp_y(theta1_list[i],theta2_list[i],x))
    ys.append(sigmoid(get_tmp_y(theta1_list[-1],theta2_list[-1],x)))
    tools.matplot.drawlines(xs, ys)
    #draw sigmoid line
    '''
    x = np.arange(-5,5,0.5)
    xs =[]
    ys= []
    xs.append(x)
    ys.append(sigmoid(x))
    tools.matplot.drawlines(xs, ys)
    '''