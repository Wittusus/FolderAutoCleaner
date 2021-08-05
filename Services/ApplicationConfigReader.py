class ApplicationConfigReader:

    def __init__(self, configFilePath: str):
        self.configFilePath = configFilePath

    def readExtensions(self):
        try:
            file = [i.split(':') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError
        option = "extensions"
        result = list(filter(lambda x: x[0] == option, file))[0][1].strip()
        result= result.split(',')
        result=[i.strip() for i in result]
        return result
    def readSource(self):
        try:
            file = [i.split(' ') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError
        result = file[1][1].strip()
        return result
    def readDestination(self):
        try:
            file = [i.split(' ') for i in open(self.configFilePath)]

        except:
            return FileNotFoundError
        result = file[2][1].strip()
        return result
