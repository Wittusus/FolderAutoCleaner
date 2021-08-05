from os import listdir
import shutil
import os

from Services.Logger import Logger

class FileManager:
    def __init__(self, src: str, dst: str):
        self.src = src
        self.dst = dst
        self.extentions = []
        self.filesCount = 0
        self.logger = Logger("Logs/FileManagerLogs.log")

    def getExtentions(self):
        files = [f for f in listdir(self.src)]

        countfiles = [ i for i in files if not i.isupper()]
        self.filesCount = len(countfiles)

        extentions = [os.path.splitext(f)[1][1:] for f in files]
        return extentions

    def makeFolders(self):
        extentions = self.getExtentions()
        extentions = list(dict.fromkeys([str(i) for i in extentions if len(i)>=1]))
        extentions = [ i.upper()  for i in extentions  ]
        self.extentions = extentions

        folders = []

        try:
            folders.append(self.dst + "/FOLDERS")
            os.mkdir(self.dst+"/FOLDERS")
            self.logger.log_message("Add folder: "+ self.dst+"/FOLDERS")
        except:
            self.logger.log_message("error", "Error adding folder: " + self.dst + "/FOLDERS")
            pass

        for i in extentions:
            try:
                os.mkdir(self.dst+f"/{i}")
                self.logger.log_message("Add folder: " + self.dst+f"/{i}")
            except:
                self.logger.log_message("error", "Error adding folder: " + self.dst+f"/{i}")
                pass
            folders.append(self.dst + f"/{i}")


        return set(folders)

    def moveFiles(self):
        files = listdir(self.src)
        folders = self.makeFolders()
        fileCounter = self.filesCount
        movedCounter = 1



        for file in files:
            for folder in folders:
                if [os.path.splitext(file)[1][1:].upper()][0] == folder.split('/')[-1]:
                    try:

                        self.displayProgressBar(movedCounter)
                        shutil.move(self.src+"/"+file, folder)
                        self.logger.log_message("Moved "+self.src+"/"+file+" to "+folder)
                        fileCounter-=1
                        movedCounter+=1

                    except:
                        self.logger.log_message("error ","Couldn't add file"+self.src+"/"+file+" to "+folder)
                        pass

        files = listdir(self.src)
        for file in files:
            if (not file.isupper()):
                try:
                    self.displayProgressBar(movedCounter)
                    shutil.move(self.src + "/" + file, self.dst+"/FOLDERS")
                    fileCounter -= 1
                    movedCounter+=1
                except:
                    self.logger.log_message("error ", self.src + "/" + file+ " to " + self.dst+"/FOLDERS")
                    pass


    def displayProgressBar(self, movedCounter):
        print(f"Files moved: {movedCounter}/{self.filesCount}")




