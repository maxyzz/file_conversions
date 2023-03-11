
import os
from bs4 import BeautifulSoup

class fileManipulations:

    def getFileSourcesNames(self,data_folder):
        sourceNames=[]
        for dir in os.listdir(data_folder):
            if dir not in ['txt','pdf']:
                if os.path.isdir(os.path.join(data_folder, dir)):
                    sourceNames.append(dir)

        return sourceNames
    
    def mergeHtmlFiles(self,dirPath):
        output_doc = BeautifulSoup()
        output_doc.append(output_doc.new_tag("html"))
        output_doc.html.append(output_doc.new_tag("body"))
        for file in os.listdir(dirPath):
            if not file.lower().endswith('.html'):
                continue

            with open(dirPath/file, 'r', encoding='utf8') as html_file:
                output_doc.body.extend(BeautifulSoup(html_file.read(), "html.parser").body)
        return output_doc
    
    def getFilesFromFolder(self,extension,dirPath):
        fileNames=[]
        for file in os.listdir(dirPath):
            if not file.lower().endswith(f'.{extension}'):
                continue
            fileNames.append(file)
        return fileNames