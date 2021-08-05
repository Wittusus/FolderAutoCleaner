from Services.ApplicationConfigReader import ApplicationConfigReader
from Services.FileManager import FileManager

class Program:

    def __init__(self):
        self.configReaderService = ApplicationConfigReader("Config/config.txt")
        self.fileManagerService = FileManager(self.configReaderService.readSource(), self.configReaderService.readDestination())

    def run(self):
        try:
            print("App started")
            print(self.fileManagerService.moveFiles())


        except:
            raise Exception("App could not be started")
