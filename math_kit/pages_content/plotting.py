from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt



class Plotter():
    def __init__(self ):
        pass

    def line_plot(self, x_list, y_list, plt_name= None, x_lable= None ,y_lable= None, line_lable=None):
        """
        will plot x set vs y set
        takes x list of integars, y list of integers , plat name as string , x axis lable as string , y axis lable as string, line_lable as string
        return plot
        """
        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        plt.plot(x_list,y_list, label=line_lable)
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def function_plotter(self,a=0,b=0,c=0,d=0,e=0,f=0,plt_name= None, x_lable= None ,y_lable= None, line_lable=None, x_start=-100,x_end=100,step=.1 ):
        """
        will plot a polynomial function in the form of ax^5+bx^4+cx^3+dx^2+ex+f
        the function can auto generate the x list, in the form of x_start and x_end is the begging of and end of the list , with step between numbers
        takes a,b,c,d,e,f as integers , plat name as string , x axis lable as string , y axis lable as string,line_lable as string
        """
        x_list= np.arange(x_start,x_end+step,step)
        def _funx(x):
            return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
        y_list=_funx(x_list)
        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        plt.plot(x_list,y_list, label=line_lable)
        plt.legend()
        plt.grid(True)

        plt.show()
        
        pass
        


"""   
def function(x,a,b,c):
  return a*x**2+b*x+c


start_x=-10
end_x=10
x_spacing=100
a=3
b=1
c=4


#xlist= np.linspace(-10,10,num=1000)
xlist=[1,2,7,13]
#print(xlist)
#ylist= function(xlist,a,b,c)
ylist=[100,22,317,75]


plt.figure(num=0,dpi=120)
plt.legend()


plt.title("example")
plt.xlabel("x lable")
plt.ylabel("y lable")
plt.plot(xlist,ylist, label="testing")
plt.show()
"""

if __name__== "__main__":
    p1=Plotter()
    x=[1,4,7,10]
    y=[13,25,100,33]
    p1.line_plot(x,y,"test", "testing x", "testing y","testline")
    
    """
    p2=Plotter()
    p2.function_plotter(0,0,3,1,5,0,"func test", "funx","funy","funlable",-100,100,1)
    """