#coding=utf-8
'''
Created on 2017年11月6日

@author:  Wentao Mao
'''
import matplotlib.pyplot as plt
import random


def drawlines(xs,ys,labels=[],xlabel_name="",ylable_name=""):
    if len(labels) != 0:
        for i in range(0,len(xs)):
            color="#"+str(hex(random.randint(1048576,16777215)))[2:]
            
            plt.plot(xs[i],ys[i],color=color,label=labels[i])
    else :
        for i in range(0,len(xs)):
            color="#"+str(hex(random.randint(1048576,16777215)))[2:]
            plt.plot(xs[i],ys[i],color=color)
    
    plt.legend(loc='upper right')
    if xlabel_name:
        plt.xlabel(xlabel_name)  
    if ylable_name:
        plt.ylabel(ylable_name)  
    
    #辅助线
    plt.grid(True)
    
    # 展示
    plt.show()

if __name__ == '__main__':
    xs=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    ys=[[1,1,1,1],[1,2,3,4],[3,3,2,3]]
    labels=["s1","s2","s3","s4"]
    drawlines(xs,ys,labels,xlabel_name="x",ylable_name="y")