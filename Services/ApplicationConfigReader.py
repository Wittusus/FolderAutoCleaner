class ApplicationConfigReader:

    def __init__(self, configFilePath: str):
        self.configFilePath = configFilePath

    def readExtensions(self):
        try:
            file = [i.split(':') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError


        result = list(filter(lambda x: x[0] == "extensions", file))[0][1].strip()
        result = result.split(',')
        result = [i.strip() for i in result]

        return result

    def readPath(self, arr_nr):

        try:
            file = [i.split(' ') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError

        result = file[arr_nr][1].strip()
        return result

    def readSource(self):
        return self.readPath(1)

    def readDestination(self):
        return self.readPath(2)
