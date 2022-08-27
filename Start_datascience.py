from re import L
import pandas as pd
from openpyxl import load_workbook

a = pd.DataFrame()

l = ['Great Britain','China','Russia','United States','Korea','Japan', 'Germany']
a = pd.DataFrame(l)

print(l)

df = pd.read_excel('Data.xlsx')


b = pd.DataFrame(df)

print(b)


