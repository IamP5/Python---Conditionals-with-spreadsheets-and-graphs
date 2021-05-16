"""
  Use this spreadsheet: https://www.dropbox.com/s/s108a7yp3whqtf8/fake-classrooms-correl09.csv?dl=1
  
  Write a program that:
    
    a) Read the name of two columns of the spreadsheet (col1 and col2), knowing that col1 (X) it will be used as a independent variable
    and  col2 (Y) as a dependent variable.
    b) Calculate and print the correlation of the columns.
    c) Calculate and show the linear equation.
    d) Read a int number "x" representing a value of col1 that will be used to make the prediction.
    e) If the absolute value of the correlation is < 0.35, show the message "Correlação < 0.35. Predição não exibida!".
    f) If the absolute value of the correlation is >= 0.8, the program should calculate and print the value of y (prediction) for the x
  read and show the message "Correlação >= 0.8".
    g) If the absolute value of the correlation is greater or equal 0.35 and minor than 0.8, the program should calculate and print the
  value of y (prediction) for the x read and the message "Correlação < 0.8. Atenção com a predição!" 
    

"""

import pandas as pd
import numpy as np

df = pd.read_csv("https://www.dropbox.com/s/s108a7yp3whqtf8/fake-classrooms-correl09.csv?dl=1")

col1 = input()
col2 = input()

corr = round(df[col1].corr(df[col2]), 2)

x = int(input())

(a, b) = np.polyfit(df[col1], df[col2], deg = 1)

if abs(corr)< 0.35:
  print("Correlação < 0.35. Predição não exibidda!")

elif abs(corr) >= 0.8:
  y = a*x + b
  print(f"Correlação entre {col1} e {col2} = {corr} \n Equação: y = {'%.2f' %a}x + {'%.2f' %b} \n Predição de {col1} para {col2} = {'%.2f' %x} é {'%.2f' %y}. \n Correlação >= 8")

elif 0.35 <= abs(corr) < 0.8:
  y = a*x + b
  print(f"Correlação entre {col1} e {col2} = {corr} \n Equação: y = {'%.2f' %a}x + {'%.2f' %b} \n Predição de {col1} para {col2} = {'%.2f' %x} é {'%.2f' %y}. \n Correlação < 0.80. Atenção com a predição!")


