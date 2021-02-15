import csv
import pandas as pd

provinceList = {'Newfoundland and Labrador':'A','Nova Scotia':'B','Prince Edward Island': 'C','New Brunswick': 'E','Eastern Quebec': 'G','Metropolitan Montreal': 'H','Western Quebec': 'J','Eastern Ontario': 'K','Central Ontario': 'L','Metropolitan Toronto': 'M','Southwestern Ontario': 'N','Northern Ontario': 'P','Manitoba': 'R','Saskatchewan': 'S','Alberta': 'T','British Columbia': 'V','Northwest Territories and Nunavut': 'X','Yukon': 'Y'}


keys = provinceList.keys()
values = provinceList.values()


csv_data = pd.read_csv(r'C:\Users\garci\Desktop\CSV TEST\CanadianPostalCodes.csv',usecols=[5])

#var = csv_data.where(csv_data == 'A','NO',inplace = False)
var = csv_data.replace(values,keys)

#print(csv_data)
#var.to_csv(r'C:\Users\garci\Desktop\CSV TEST\CanadianPostalCodes.csv', index = False)

df = pd.read_csv(r'C:\Users\garci\Desktop\CSV TEST\CanadianPostalCodes.csv')
df["Provinces"] = var
df.to_csv(r'C:\Users\garci\Desktop\CSV TEST\CanadianPostalCodes.csv', index=False)



