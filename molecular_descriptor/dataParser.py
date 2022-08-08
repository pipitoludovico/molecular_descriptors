import pandas as pd
from clean_smiles import *


class Parser:
    def __init__(self, data):
        if data is None:
            print("Please, input a .csv or excel file!")
        if data.endswith('.csv'):
            self.data = pd.read_csv(data)
        else:
            self.data = pd.read_excel(data)

    def getDf(self):
        return self.data

    def getSmiles(self):
        return self.data['SMILES']
