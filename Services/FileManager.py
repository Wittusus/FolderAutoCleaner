from os import listdir
import shutil
import os


class FileManager:
    def __init__(self, src: str, dst: str):
        self.src = src
        self.dst = dst
        self.extenstions = []
        self.filesCount = 0

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
        self.extenstions = extentions

        folders = []

        try:
            folders.append(self.dst + "/FOLDERS")
            os.mkdir(self.dst+"/FOLDERS")
        except:
            pass

        for i in extentions:
            try:
                os.mkdir(self.dst+f"/{i}")
            except:
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
                        fileCounter-=1
                        movedCounter+=1

                    except:
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
                    pass


    def displayProgressBar(self, movedCounter):
        print(f"Files moved: {movedCounter}/{self.filesCount}")



