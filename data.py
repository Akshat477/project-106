#inversly corelated data set
from asyncio import sleep
import plotly.express as px 
import csv 
import numpy as np

def get_data(datapath) : 
    days_present = []
    marks = []
    with open(datapath)as data : 
        df  = csv.DictReader(data)
        for row in df :
           days_present.append(float(row["Days Present"]))
           marks.append(float(row["Marks In Percentage"]))
        return{"x": days_present,"y":marks}    
        #fig = px.scatter(df,x = "Temperature",y = "Ice-cream Sales")
        #fig.show()
def find_correlation(dataSource) :
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between marks and days present :",correlation[0,1]) 
def setup() :
    datapath = "data 3.csv"
    dataSource = get_data(datapath) 
    find_correlation(dataSource)
setup()     
     