from datetime import datetime

class Logger:
    def __init__(self, file: str):
        self.file = file

    def log_message(self, message: str, log_level: str = "info"):
        with open(self.file, "a") as f:
            f.write("[" + log_level.upper() + "]" + " " + message + ": " + str(datetime.now()) + " \n")
