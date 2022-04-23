import imp
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import Counter
from tkinter import Frame, Label


class Plotter():
    def __init__(self, master, tools):
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
        takes a,b,c,d,e,f as integers , plat name as string , x axis lable as string , y axis lable as string,line_lable as string
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
        
    def plot_csv(self, path ,attr_name, spliter="," ,length =1):
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
        count= Counter()

        row=next(csv_reader)
        print(row[attr_name].split(spliter))

        for row in csv_reader:
            count.update(row[attr_name].split(spliter))
        attr =[]
        numbers=[]
        for item in count.most_common(length):
            attr.append(item[0])
            numbers.append(item[1])

         
        
        plt.legend()


        plt.title("example")
        plt.xlabel("x lable")
        plt.ylabel("y lable")
        plt.bar(attr,numbers, label="testing")
        plt.show()



        


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
    p3=Plotter()
    p3.plot_csv(r"math_kit\assets\csv\data.csv",'LanguagesWorkedWith',';',15)



    """
    with open(r"math_kit\assets\csv\data.csv","r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        language_count= Counter()

        row=next(csv_reader)
        print(row['LanguagesWorkedWith'].split(";"))

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
    

