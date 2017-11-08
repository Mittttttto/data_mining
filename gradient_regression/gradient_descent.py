import tools.matplot as mat

x_list=[1,2,3,4,5,6]
y_list=[1,2,3.1,3.9,5.1,5.9]

theta1_list=[]
theta2_list=[]

def gradient_descent():
    theta1=0
    theta2=0 
    alpha=0.01
    gradient_cost=[0,0]
    loop_time=0
    while True:
        for i in range(0,len(x_list)):
            diff=theta1*x_list[i]+theta2-y_list[i]
            theta1=theta1-alpha*diff*x_list[i]
            theta2=theta2-alpha*diff
        
        gradient_cost[0]=0;
        for i in range(0,len(x_list)):
            gradient_cost[0]=gradient_cost[0]+(y_list[i]-theta1*x_list[i]-theta2)**2/2
        print  "gradient_cost is"+str(gradient_cost[0]);
        if abs(gradient_cost[0]-gradient_cost[1])<0.00001:
            break
        theta1_list.append(theta1)
        theta2_list.append(theta2)
        gradient_cost[1]=gradient_cost[0]
        loop_time=loop_time+1
        if loop_time>1000:
            print "loop too many times"
            break
    return theta1_list,theta2_list
    print theta1_list
    print theta2_list


if __name__ == '__main__':
    
    theta1_list,theta2_list=gradient_descent()
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