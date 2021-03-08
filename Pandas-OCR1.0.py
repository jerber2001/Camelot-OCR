import sys
sys.path.append('/usr/local/lib/python3.9/site-packages/pytesseract')
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import pandas as pd
import numpy as np 
import csv
#import openpyxl



# filename = "OCR_CSV.csv"

# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)

#--------Path-----------
path = '/Users/jycai/Downloads/SIMMARON/'
df = pytesseract.image_to_data(Image.open(path+'Page_1_Cropped.png'),lang='eng', output_type='data.frame')
df_pandas = pd.DataFrame(data=df)
df_pandas.to_csv(path+'OCR_CSV_Cropped.csv')
print(df_pandas.head())
# print(df_pandas)
# df.to_excel("output.xlsx")

##------------- Camelot-py ---------------
##Camelot-py plugin: https://www.thepythoncode.com/article/extract-pdf-tables-in-python-camelot
#sys.path.append('/usr/local/lib/python3.9/site-packages/camelot')
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.9/bin')
# import camelot
# file = 'Page_1_Cropped.png'
# tables = camelot.read_pdf(file)
# print("Total tables extracted:", tables.n)
# print(tables[0].df)
# tables[0].to_csv("Page_1_Cropped.csv")

#------------- Tabula-py ----------------
import tabula
import os

from tabula import read_pdf
file = 'Page_1_Cropped.png'

tables = tabula.read_pdf(file, pages="all")

# save them in a folder
folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# iterate over extracted tables and export as excel individually
for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

# convert all tables of a PDF file into a single CSV file
# supported output_formats are "csv", "json" or "tsv"
tabula.convert_into(file, "output.csv", output_format="csv", pages="all")
