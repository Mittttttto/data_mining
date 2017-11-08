#coding=utf-8
#通过高斯分布来对样本的权重进行分配，从而达到局部拟合的效果
import tools.matplot as mat
import numpy as np
from scipy import stats
stats_mu=3   #高斯分布的中点
stats_sigma=1   #高斯分布的方差，值越小越细高 值越大越扁胖

x_list=[1,2,3,4,5,6]
y_list=[1,2,3.1,3.9,5.1,5.9]

theta1_list=[]
theta2_list=[]

def gradient_descent_gaussian():
    theta1=0
    theta2=0 
    alpha=0.1
    gradient_cost=[0,0]
    loop_time=0
    while True:
        for i in range(0,len(x_list)):
            diff=theta1*x_list[i]+theta2-y_list[i]
            theta1=theta1-alpha*diff*x_list[i]*stats.norm.pdf(x_list[i],stats_mu,stats_sigma)
            theta2=theta2-alpha*diff*stats.norm.pdf(x_list[i],stats_mu,stats_sigma)
        
        gradient_cost[0]=0;
        for i in range(0,len(x_list)):
            gradient_cost[0]=gradient_cost[0]+(y_list[i]-theta1*x_list[i]-theta2)**2/2*stats.norm.pdf(x_list[i],stats_mu,stats_sigma)
        print  "gradient_cost is"+str(gradient_cost[0]);
        if abs(gradient_cost[0]-gradient_cost[1])<0.0000001:
            break
        theta1_list.append(theta1)
        theta2_list.append(theta2)
        gradient_cost[1]=gradient_cost[0]
        loop_time=loop_time+1
        if loop_time>1000:
            print "loop too many times"
            break
    return theta1_list,theta2_list
   


if __name__ == '__main__':
    
    theta1_list,theta2_list=gradient_descent_gaussian()
    def get_y(theta1,theta2,x):
        return theta1*x+theta2
    xs=[]
    ys=[]
    labels=[]
    for i in range(0,len(theta1_list)):
        y=[]
        x=[]
        y.append(get_y(theta1_list[i], theta2_list[i], 0))
        y.append(get_y(theta1_list[i], theta2_list[i], 5))
        x.append(0)
        x.append(5)
        xs.append(x)
        ys.append(y)
        print "time "+str(i)+" theta1 is "+str(theta1_list[i])+"theta2 is "+str(theta2_list[i])
        labels.append("line"+str(i))

    #print "draw pic"
    mat.drawlines(xs, ys, labels, xlabel_name="x", ylable_name="y")