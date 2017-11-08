#coding=utf-8
'''
Created on 2017年11月8日

@author:  Wentao Mao
'''
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_norm_pmf():  
    ''''' 
                正态分布是一种连续分布，其函数可以在实线上的任何地方取值。 
                正态分布由两个参数描述：分布的平均值μ和方差σ2 。 
    '''  
    mu = 0 #mean  
    sigma = 1 #standard deviation  
    x = np.arange(-5,5,0.1)  
    y = stats.norm.pdf(x,0,1)  
    print y  
    plt.plot(x, y)  
    plt.title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu,sigma))  
    plt.xlabel('x')  
    plt.ylabel('Probability density', fontsize=15)  
    plt.show()  

test_norm_pmf()