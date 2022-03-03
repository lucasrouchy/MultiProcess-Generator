
import multiprocessing
import time
import sys
import csv
import tkinter as tk
from unittest import result

data_filename = 'AllStates.csv'
year_str = sys.argv[1]
state_sel= sys.argv[2]
input_filename = year_str + data_filename

large = int(10000000)
medium = int(4000000)
smaller = int(1500000)

class GUI:
    def __init__(self):
        None
        
    def window(self):
        
        window = tk.Tk()
        window.geometry("600x400")
        year_label = tk.Label(window, text = "Year:")
        state_label = tk.Label(window, text = "State:")
        year = tk.Entry(window, textvariable=year_label)
        state = tk.Entry(window, textvariable=state_label)

        label = tk.Label(text="US Population Generator 2010-2019")
        entry = tk.Button(window, text="Find Population", command=submit)
        label.grid(row = 0, column=0)
        year_label.grid(row=1,column=0)

        state_label.grid(row=2, column=0)
        year.grid(row=1, column=1)
        state.grid(row=2,column=1)
        entry.grid(row=3, column=0)
        
        quit = tk.Button(window, text= "Quit", command=window.destroy)
        quit.grid(row=4, column=0)
        
        window.mainloop()
        time.sleep(1)
        
def evaluatesize():
    population=getfirstDataRowValue(input_filename,1,state_sel)
    p = int(population)
    if p <= smaller:
        print("Super Small State")
    elif p <= medium:
        print("Small State")
    elif p <= large:
        print("Medium Sate")
    else:
        print("Large State")

def submit():
        
        year_str = sys.argv[1]
        data_filename = 'AllStates.csv'
        input_filename = year_str + data_filename
        state_sel= sys.argv[2]
        result=getfirstDataRowValue(input_filename,1,state_sel)
        print(result) 

def getInputFilename():
    return sys.argv[1]

def getfirstDataRowValue(input_filename, col_number,state):
    
    population = -1
    with open(input_filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        # next(csvfile)
        for row in reader:
            data = row[col_number]
            # print(data)
            if data == state:
                population=row[2]
    return population
    
    
def getInputtedYearFromCSV(input_filename):
    return getfirstDataRowValue(input_filename,0)

def getInputtedStateFromCSV(input_filename):
    return getfirstDataRowValue(input_filename,1)

def getStatePopulationFromDataFile(input_filename):
    population = ''
    with open(data_filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            state = row[0]
            if state == input_filename:
                population = row[1]
    return getfirstDataRowValue(input_filename,2)
def main():
    gui = GUI()
    
    name = gui.window()
    print(name)
  
    print(sys.argv)
    year_sel = int(sys.argv[1])
    print('year_sel=%d' % year_sel)
    print('year = %s' % year_str)
    
    print(input_filename)
    
    result1=getfirstDataRowValue(input_filename,1,state_sel)
    print(result1)
    
if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=main)
    p2 = multiprocessing.Process(name='p2', target=evaluatesize)
    p2.start()
    p1.start()
    