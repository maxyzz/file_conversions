import pdfkit
from pathlib import Path

from src.file_manupulations import fileManipulations

file_manupulations = fileManipulations()

# combine all html files to one html file
data_folder =Path(__file__).parent / r"data"

# getting all available data folders
sourceNames=file_manupulations.getFileSourcesNames(data_folder)

for sourceName in sourceNames:
    output_doc=file_manupulations.mergeHtmlFiles(data_folder/sourceName/"dita_html")

    f = open(data_folder/"pdf"/(sourceName+".html"), "wb")
    f.write(output_doc.encode('utf-8'))
    f.close()
    # convert html to pdf 
    pdfkit.from_file((data_folder/"pdf"/(sourceName+".html")).__str__(), (data_folder/"pdf"/(sourceName+".pdf").__str__()))
