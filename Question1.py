"""
  Read this spreadsheet: https://www.dropbox.com/s/kwibw8umms9yh9w/NotasAjuste.csv?dl=1
  This contain the grades of a subject. The program should:
    Read the link of the spreadsheet
    Receive from the user the name of one test (Exame 1, Exame2...)
    Add a new column named "Adjustment" with the grades of the tests received from the user
    adjusted by the follow rules:
      
      If the average of the test is < 50, the grade adjusted have a increase of 20%.
      If the average of the test is between 50 and 70, the grade adjusted have a increase of 10%.
      If the average of the test is between 70 and 80, the grade adjusted have a increase of 5%.
      Otherwise, there is no adjustment (The "Adjustment" column have the same values of the tests)
    
"""

import pandas as pd 

df = pd.read_csv("https://www.dropbox.com/s/kwibw8umms9yh9w/NotasAjuste.csv?dl=1")

inputExam = input()

df["Adjustment"] = df[inputExam]
if df[inputExam].mean() < 50:
  df["Adjustment"] = df[inputExam] * 1.20
elif 50 <= df[inputExam].mean() <= 70:
  df["Adjustment"] = df[inputExam] * 1.10
elif 70 <= df[inputExam].mean() <= 80:
  df["Adjustment"] = df[inputExam] * 1.05
else:
  df["Adjustment"] = df[inputExam] 
  

print(df)
