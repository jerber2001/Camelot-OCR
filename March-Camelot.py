#Command Line:
#  $ pip3 install camelot-py[cv] tabula-py
# Camelot pip package: https://pypi.org/project/camelot-py/
# Git Source Code: https://github.com/camelot-dev/camelot/issues/193
# *** Troubleshooting *** cv2 module not installed in the handlers.py

from camelot import *

# PDF file to extract tables from 
file = "Page_1_Cropped.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# Export Option 1: export individually as CSV
tables[0].to_csv("Page_1_camelot.csv")

# Export Option 2: export individually as Excel (.xlsx extension)
tables[0].to_excel("Page_1_camelot.xlsx")

from camelot import *

file = "Page_1_Cropped.pdf"

tables = camelot.read_pdf(file)

print("Total tables extracted:", tables.n)
print(tables[0].df)

tables[0].to_csv("Page_1_camelot.csv")
tables[0].to_excel("Page_1_camelot.xlsx")