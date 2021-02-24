from datetime import datetime

class DBHelper:

    def __init__(self):
        pass

    def writeBars(self, bars:list, period="day"):
        pass

    def writeFactors(self, factors:dict):
        pass


class BaseDataHelper:

    def __init__(self):
        self.isAuthed = False
        pass

    def __check__(self):
        if not self.isAuthed:
            raise Exception("This module has not authorized yet!")

    def auth(self, **kwargs):
        pass

    def dmpCodeListToFile(self, filename:str, hasIndex:bool=True, hasStock:bool=True):
        pass

    def dmpAdjFactorsToFile(self, codes:list, filename:str):
        pass

    def dmpBarsToFile(self, folder:str, codes:list, start_date:datetime=None, end_date:datetime=None, period:str="day"):
        pass

    def dmpAdjFactorsToDB(self, dbHelper:DBHelper, codes:list):
        pass

    def dmpBarsToDB(self, dbHelper:DBHelper, codes:list, start_date:datetime=None, end_date:datetime=None, period:str="day"):
        pass