import imp
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import Counter
from tkinter import Frame, Label


class Plotter():
   
    def __init__(self, master, tools):
        pass
        
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.plotter_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.plotter_frame)
        
        Label(self.plotter_frame, text="Plotter").pack()
        
        

    def line_plotter(self, x_list, y_list, plt_name= None, x_lable= None ,y_lable= None, line_lable=None, save=False):
        """
        will plot x set vs y set
        takes x list of integars, y list of integers , plat name as string , x axis lable as string , y axis lable as string, line_lable as string
        return plot
        """
        
        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        plt.plot(x_list,y_list, label=line_lable, color="c")
        plt.legend()
        plt.grid(True)
        if save:
            plt.savefig("./math_kit/assets/plots/plot.png")
        plt.show()
    
    def function_plotter(self,a=0,b=0,c=0,d=0,e=0,f=0,plt_name= None, x_lable= None ,y_lable= None, line_lable=None, x_start=-100,x_end=100,step=.1,save=False ):
        """
        will plot a polynomial function in the form of ax^5+bx^4+cx^3+dx^2+ex+f
        the function can auto generate the x list, in the form of x_start and x_end is the begging of and end of the list , with step between numbers
        takes a,b,c,d,e,f as integers , plot name as string , x axis lable as string , y axis lable as string,line_lable as string
        """
        x_list= np.arange(x_start,x_end+step,step)
        def _funx(x):
            return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
        y_list=_funx(x_list)
        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        plt.plot(x_list,y_list, label=line_lable, color="c")
        plt.legend()
        plt.grid(True)
        if save:
            plt.savefig("./math_kit/assets/plots/plot.png")

        plt.show()

    def bar_plotter(self, x_list, y_list, plt_name= None, x_lable= None ,y_lable= None, line_lable=None, save=False):
        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)

        plt.bar(x_list,y_list, label=line_lable, color="c")
        plt.legend()
        plt.grid(True)
        if save:
            plt.savefig("./math_kit/assets/plots/plot.png")
        plt.show()
        
    def plot_csv(self, path ,x_axis_attr,y_axis_attr,start=0,end=None, plt_name= None, x_lable= None ,y_lable= None, line_lable=None):
        """
        will read a csv file and plot one column in the x-axis vs another column in the y-axis,
        takes the path of the file , the name of the column to be used in the x-axis, the name of the colmun to be used in the y-axis, 
        a starting row and end row as numbers , plot name as string , x axis lable as string , y axis lable as string,line_lable as string
        """
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            row=next(csv_reader)
            csv_list=list(csv_reader)
        

        print(row)
        
        x_axis=[]
        y_axis=[]
        

        for row in csv_list:
           x_axis.append(row[x_axis_attr])
           y_axis.append(row[y_axis_attr])
        
        step=int((end-start)/15)
        tick_end=end+1
 
        plt.legend()
        plt.grid(True)

        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        plt.plot(x_axis[start:end:],y_axis[start:end:], label=line_lable)
        
        plt.xticks(x_axis[0:int(tick_end):step],rotation=90)
        plt.yticks(y_axis[0:int(tick_end):step],rotation=0)
        
        plt.show()
        


        




if __name__== "__main__": 

    """
    p3=Plotter()
    path=r"math_kit\assets\csv\gold.csv"
    x_axis_attr="Date"
    y_axis_attr="Close"
    p3.plot_csv(path,x_axis_attr,y_axis_attr,0,150,"xy","x","y")
    
    
    """


    """
    path=r"math_kit\assets\csv\gold.csv"
    x_axis_attr="Date"
    y_axis_attr="Close"
    
    with open(r"math_kit\assets\csv\gold.csv","r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row=next(csv_reader)
        csvlist=list(csv_reader)
        

        print(row)
        
        x_axis=[]
        y_axis=[]
        for row in csvlist:
           x_axis.append(row["Date"])
           y_axis.append(row["Close"])
        

 
        plt.legend()


        plt.title("example")
        plt.xlabel("x lable")
        plt.ylabel("y lable")
        plt.plot(x_axis[0:150:],y_axis[0:150:], label="testing")
        plt.xticks(x_axis[0:151:10],rotation=90)
        plt.yticks(y_axis[0:151:10],rotation=0)
        plt.grid(True)
        plt.show()
"""
            

"""
        for row in csv_reader:
            language_count.update(row['LanguagesWorkedWith'].split(";"))
    languages =[]
    pop=[]
    for item in language_count.most_common(15):
        languages.append(item[0])
        pop.append(item[1])

    print(language_count.most_common(15))   
    print(languages)
    print(pop) 
    plt.legend()


    plt.title("example")
    plt.xlabel("x lable")
    plt.ylabel("y lable")
    plt.bar(languages,pop, label="testing")
    plt.show()

"""





""" p1=Plotter()
    x=[1,4,7,10]
    y=[13,25,100,33]
    p1.line_plotter(x,y,"test", "testing x", "testing y","testline")
"""
                                                                

  

  
    


"""    
    p2=Plotter()
    p2.function_plotter(0,0,3,1,5,0,"func test", "funx","funy","funlable",-100,100,1)
"""
    

