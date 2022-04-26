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





    
