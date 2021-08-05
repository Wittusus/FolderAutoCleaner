from os import listdir
import os

class FileManager:
    def __init__(self, src: str, dst: str):
        self.src = src
        self.dst = dst

    def getExtentions(self):
        files = [f for f in listdir(self.src)]
        extentions = [os.path.splitext(f)[1][1:] for f in files]
        return extentions

    def makeFolders(self):
        extentions = self.getExtentions()
        isFolder = min( [len(i) for i in extentions] ) == 0

        extentions = list(dict.fromkeys([str(i) for i in extentions if len(i)>=1]))
        extentions = [ i.upper()  for i in extentions  ]


        try:
            if isFolder: os.mkdir(self.dst+"/FOLDERS")
        except:
            pass

        for i in extentions:
            try:
                os.mkdir(self.dst+f"/{i}")
            except:
                pass

    def moveFiles(self):
        pass
