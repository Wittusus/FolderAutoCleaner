class Program:

    def __init__(self):
        try:
            print("App started")
        except:
            raise Exception("App could not be started")