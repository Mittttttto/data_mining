#coding=utf-8
'''
Created on 2017年11月14日

@author: wenmao
'''


# y = x**2 -3
# 计算机求开根


x_list=[]
y_list=[]

def newton_reg():
    x=3.0
    x_list.append(x)
    loop_time=0
    
    while True:
        x=x-(x**2-3)/(x*2)
        x_list.append(x)
        y_list.append(x**2-3)
        if abs(y_list[-1])<0.00000001:
            break
        loop_time=loop_time+1
        if loop_time>1000:
            break
    



if __name__ == '__main__':
    newton_reg()
    print x_list
    print y_list