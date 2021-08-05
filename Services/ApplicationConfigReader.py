class ApplicationConfigReader:

    def __init__(self, configFilePath: str):
        self.configFilePath = configFilePath

    def readPath(self, arr_nr):

        try:
            file = [i.split(' ') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError

        result = file[arr_nr][1].strip()
        return result

    def readSource(self):
        return self.readPath(0)

    def readDestination(self):
        return self.readPath(1)
