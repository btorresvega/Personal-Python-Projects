import csv
import pandas as pd
import re
import string

#provinceList = {'Newfoundland and Labrador':'A','Nova Scotia':'B','Prince Edward Island': 'C','New Brunswick': 'E','Eastern Quebec': 'G','Metropolitan Montreal': 'H','Western Quebec': 'J','Eastern Ontario': 'K','Central Ontario': 'L','Metropolitan Toronto': 'M','Southwestern Ontario': 'N','Northern Ontario': 'P','Manitoba': 'R','Saskatchewan': 'S','Alberta': 'T','British Columbia': 'V','Northwest Territories and Nunavut': 'X','Yukon': 'Y'}
place_nameList = {'Riviere-Verte':'Rivi�Re-Verte','St. John\'s':'St. John&#39;S','St. John\'s':'St.John&#39;S','Pointe-Du-Chene':'POINTE-DU-CH�NE','Pointe-Du-Chene':'Pointe-Du-Ch�Ne','Cap-Pele':'CAP-PEL�'} #Trois-Rivieres

#provinceKeys = provinceList.keys()
#provinceValues = provinceList.values()

place_nameKeys = place_nameList.keys()
place_nameValues = place_nameList.values()


#provincesData = pd.read_csv(r'C:\Users\garci\Desktop\CSV TEST\Test\Test.csv',usecols=[4],encoding='utf_8_sig')
place_nameData = pd.read_csv(r'C:\Users\garci\Desktop\CSV TEST\Test\Test.csv',usecols=[4],encoding='utf_8_sig')

#provincesReplacement = provincesData.replace(provinceValues,provinceKeys)
place_nameReplacement = place_nameData.replace(place_nameValues,place_nameKeys)


df = pd.read_csv(r'C:\Users\garci\Desktop\CSV TEST\Test\Test.csv',encoding='utf_8_sig')
df["Place Name"] = place_nameReplacement
df.to_csv(r'C:\Users\garci\Desktop\CSV TEST\Test\Test.csv',index=False,encoding='utf_8_sig')

print(place_nameData.iloc[72984])