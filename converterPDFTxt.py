from pathlib import Path
from PyPDF2 import PdfReader
import json

from src.file_manupulations import fileManipulations

file_manupulations = fileManipulations()

# create file object variable
#opening method will be rb
data_folder =Path(__file__).parent / r"data/pdf"

sourceFiles=file_manupulations.getFilesFromFolder('pdf',data_folder)

for file in sourceFiles:
    with open(data_folder/file, 'rb') as book:
        pages=[]
        book_reader = PdfReader(book)
        page_list = book_reader.pages
        for page in page_list:
            story_page = page
            page_text = story_page.extract_text()
            pages.append(page_text)
        # save as json
        with open(data_folder.parent/"txt"/(file.replace('pdf','json')), 'w', encoding='utf-8') as f:
            json.dump(pages, f, ensure_ascii=False, indent=4)
        # save as txt
        with open(data_folder.parent/"txt"/(file.replace('pdf','txt')), 'w') as f:
            f.write(' '.join(pages))
