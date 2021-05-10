import plotly.figure_factory as ff 
import statistics 
import random
import pandas as pd 
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()
print(statistics.mean(data))
def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    smean=statistics.mean(dataset)
    sdev=statistics.stdev(dataset)
    print(smean)
    print(sdev)
    return smean

def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()



