from tkinter import Frame, Label
import csv
import statistics


class StatsPage:

       
    def __init__(self, master, tools):
    
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.stats_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.stats_frame)
        
        Label(self.stats_frame, text="stats").pack()

    
    @staticmethod    
    def statistics_csv(path,attr):
        """
        this function takes the path of a csv file and the column name 
        returns stadard deviation , mean and median for the data set
        """

        
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            row=next(csv_reader)
            csv_list=list(csv_reader)
        

        print(row)
        
        col_list=[]
        
        

        for row in csv_list:
           col_list.append(float(row[attr]))
        
        print(col_list)


        print(statistics.stdev(col_list))
        print(statistics.mean(col_list))
        print(statistics.median(col_list))


    @staticmethod
    def statistics_list(input_list):
        """
        this function takes a list of integers 
        returns stadard deviation , mean, median , maximum and minimum """

        print(statistics.stdev(input_list))
        print(statistics.mean(input_list))
        print(statistics.median(input_list))
        print(min(input_list))
        print(max(input_list))

        

        

        


if __name__== "__main__":

    """
    path=r"math_kit\assets\csv\gold.csv"
    s1=StatsPage()
    
    s1.statistics(path,"Close")
    """
    
