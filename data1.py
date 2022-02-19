#inversly corelated data set
from asyncio import sleep
import plotly.express as px 
import csv 
import numpy as np

def get_data(datapath) : 
    coffe = []
    sleep_hrs = []
    with open(datapath)as data : 
        df  = csv.DictReader(data)
        for row in df :
            coffe.append(float(row["Coffee in ml"]))
            sleep_hrs.append(float(row["sleep in hours"]))
        return{"x": coffe,"y":sleep_hrs}    
        #fig = px.scatter(df,x = "Temperature",y = "Ice-cream Sales")
        #fig.show()
def find_correlation(dataSource) :
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between coffe and sleep :",correlation[0,1]) 
def setup() :
    datapath = "data 4.csv"
    dataSource = get_data(datapath) 
    find_correlation(dataSource)
setup()     
     