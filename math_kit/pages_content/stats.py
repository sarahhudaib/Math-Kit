<<<<<<< HEAD
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



    
    def statistics_csv(self,path,attr):
        """
        this function takes the path of a csv file and the column name 
        returns standard deviation , mean and median for the data set


        
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



    def statistics_list(self,list):
        """
        """this function takes a list of integers 

        returns standard deviation , mean and median """


        print(statistics.stdev(list))
        print(statistics.mean(list))
        print(statistics.median(list))


        

        

        


if __name__== "__main__":

    """
    path=r"math_kit\assets\csv\gold.csv"
    s1=StatsPage()
    
    s1.statistics(path,"Close")
    """
    
=======
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
    def standard_deviation_csv(path,attr):
        """
        this function takes the path of a csv file and the column name 
        returns stadard deviation 
        """
              
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            row=next(csv_reader)
            csv_list=list(csv_reader)
        

        print(row)
        
        col_list=[]
        
        

        for row in csv_list:
           col_list.append(float(row[attr]))
        
        return statistics.stdev(col_list)


    
    @staticmethod    
    def mean_csv(path,attr):
        """
        this function takes the path of a csv file and the column name 
        returns stadard mean for the data set
        """
                
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            row=next(csv_reader)
            csv_list=list(csv_reader)
        

        print(row)
        
        col_list=[]
        
        

        for row in csv_list:
           col_list.append(float(row[attr]))
        
        return statistics.mean(col_list)
    
    @staticmethod    
    def median_csv(path,attr):
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
        
        return statistics.median(col_list)

    
    @staticmethod    
    def max_csv(path,attr):
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
        
        return max(col_list)

    @staticmethod    
    def min_csv(path,attr):
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
        
        return min(col_list)

    

    @staticmethod
    def standard_deviation_list(input_list):
        """
        """this function takes a list of integers 

        returns stadard deviation , mean, median , maximum and minimum """
        
        return statistics.stdev(input_list)
        
        
        
        

    @staticmethod
    def mean_list(input_list):
        return statistics.mean(input_list)


    @staticmethod
    def median_list(input_list):
        return statistics.median(input_list)


    @staticmethod
    def min_list(input_list):
        return min(input_list)

    @staticmethod
    def max_list(input_list):
        return max(input_list)




        

        


if __name__== "__main__":
    #print(StatsPage.max_list([10, 12, 23, 23, 16, 23, 21, 16,18,16,14,17,16]))
    
    path=r"math_kit\assets\csv\gold.csv"
    
    
    print(StatsPage.max_csv(path,"Close"))
    
    
>>>>>>> bac1ca7dce477a1a017afd7881653e8f0c2f49d8
