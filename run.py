#coding=utf-8
'''
Created on 2017年10月16日

@author: wenmao
'''


import tools

if __name__ == '__main__':
    tools.module_2.log_a("text")
    xs=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    ys=[[1,1,1,1],[1,2,3,4],[3,3,2,3]]
    labels=["s1","s2","s3","s4"]
    tools.matplot.drawlines(xs, ys, labels)