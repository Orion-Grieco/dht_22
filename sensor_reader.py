import pandas as pd
import numpy as np
import os

file = pd.read_csv("natureCenterDataExample.csv")
frame = pd.DataFrame(file, columns =["Date","Time","Entrance Humidity","Entrance C Temp","Entrance F Temp","Entrance C Heat Index","Entrance F Heat Index","Pond Humidity","Pond C Temp","Pond F Temp","Pond C Heat Index","Pond F Heat Index","Stadium Humidity","Stadium C Temp","Stadium F Temp","Stadium C Heat Index","Stadium F Heat Index"])
frame.fillna(0) # Replaces all null values represented by NaN to 0, and inherently formats the data of the data-frame into a data-table and then subsequently prints the data-table. Works in this manner only when the method is called/used by itself, otherwise it only replaces NaN values


frameNew = frame.fillna(0)
print(frameNew)
frame.fillna(0)


import pandas as pd
file = pd.read_csv("natureCenterDataExample.csv")
entranceTempFrame = pd.DataFrame(file, columns =["Entrance C Temp","Entrance F Temp","Entrance C Heat Index","Entrance F Heat Index"])
#entranceTempFrame["Total"]= entranceTempFrame["Entrance C Temp"].sum()
print(entranceTempFrame["Entrance C Temp"].sum()/(39-19),": Mean of Entrance C Temperature Values")
print(entranceTempFrame["Entrance F Temp"].sum()/(39-19),": Mean of Entrance F Temperature Values")
print(entranceTempFrame["Entrance C Heat Index"].sum()/(39-19),": Mean of Entrance C Heat Index Values")
print(entranceTempFrame["Entrance F Heat Index"].sum()/(39-19),": Mean of Entrance F Heat Index Values")

print("\n")

odd = pd.DataFrame(file,columns=[])
odds = odd[odd.index%2==1]
print(odds)
value = odds.sum()
print(value)
#print(entranceTempFrame["Entrance C Temp"].sum()/(odd[odd.index%2==1]),": Mean of Entrance C Temperature Values")
#print(entranceTempFrame["Entrance F Temp"].sum()/(odd[odd.index%2==1]),": Mean of Entrance F Temperature Values")
#print(entranceTempFrame["Entrance C Heat Index"].sum()/(odds),": Mean of Entrance C Heat Index Values")
#print(entranceTempFrame["Entrance F Heat Index"].sum()/(odds),": Mean of Entrance F Heat Index Values")
print("\n")

odd2 = pd.DataFrame(file,columns = [])
oddIndex = odd2.index%2==1
oddsum1 = oddIndex.sum()
print("(",oddsum1,")","      SUM OF ODD ROWS, AS EVENS ARE DISCARDED FOR HOLDING NULL VALUES")
print("\n")
print(entranceTempFrame["Entrance C Temp"].sum()/(oddsum1),": Mean of Entrance C Temperature Values")
print(entranceTempFrame["Entrance F Temp"].sum()/(oddsum1),": Mean of Entrance F Temperature Values")
print(entranceTempFrame["Entrance C Heat Index"].sum()/(oddsum1),": Mean of Entrance C Heat Index Values")
print(entranceTempFrame["Entrance F Heat Index"].sum()/(oddsum1),": Mean of Entrance F Heat Index Values")


