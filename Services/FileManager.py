from os import listdir
import shutil
import os

from Services.Logger import Logger

class FileManager:
    def __init__(self, src: str, dst: str):
        self.src = src
        self.dst = dst
        self.extensions = []
        self.filesCount = 0
        self.logger = Logger("Logs/FileManagerLogs.log")

    def getExtentions(self):
        files = [f for f in listdir(self.src)]

        countfiles = [ i for i in files if not i.isupper()]
        self.filesCount = len(countfiles)

        extensions = [os.path.splitext(f)[1][1:] for f in files]
        return extensions

    def makeFolder(self, extension):
        try:
            os.mkdir(self.dst + f"/{extension}")
            self.logger.log_message("Add folder: " + self.dst + f"/{extension}")
        except:
            self.logger.log_message("Error adding folder: " + self.dst + f"/{extension}", "error")
            pass

    def makeFolders(self):
        extensions = self.getExtentions()
        extensions = list(dict.fromkeys([str(i) for i in extensions if len(i) >= 1]))
        extensions = [i.upper() for i in extensions]
        self.extensions = extensions

        folders = []

        self.makeFolder("FOLDERS")

        for i in extensions:
            self.makeFolder(i)
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