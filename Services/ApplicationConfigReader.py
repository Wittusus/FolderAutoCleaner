class ApplicationConfigReader:

    def __init__(self, configFilePath: str):
        self.configFilePath = configFilePath

    def readPath(self, option):

        try:
            file = [i.split(' ') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError


        result = list(filter(lambda x: x[0] == option + ":", file))[0][1]
        return result.strip()

    def readSource(self):
        return self.readPath("src_folder")

    def readDestination(self):
        return self.readPath("dst_folder")
