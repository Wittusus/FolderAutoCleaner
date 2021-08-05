from Services.ApplicationConfigReader import ApplicationConfigReader


class Program:

    def __init__(self):
        self.configReaderService = ApplicationConfigReader("Config/config.txt")

    def run(self):
        try:
            print("App started")
            print(self.configReaderService.readExtensions())
            print(self.configReaderService.readSource())
            print(self.configReaderService.readDestination())
        except:
            raise Exception("App could not be started")
