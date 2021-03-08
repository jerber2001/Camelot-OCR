# Camelot-OCR

Program Description: 
Take an image or PDF containing tabular data, and convert it into a Pandas Dataframe, .csv, .xlsx or any other usable data structure. The progam will need to read a given PDF or image, initiate text recognition for characters, and place characters in a formated data structure.

Package Candidates: 
  Optical Character Recognition: 
  - pytesseract (Dependencies: opencv-py)
  Tabular Data Extraction
  - tabula-py (Dependencies: PIL)
  - camelot-py (Dependencies: Ghostscript)

Packages Needed: 
- pytesseract
- camelot-py

Current Challenges:
- pytesseract: Add a sys.path.append command to the opencv-py/cv2 module, current data extraction places characters into a dataframe that describes position
- camelot-py: Table cannot be reached in .core, modules and their submodules are not communticating
