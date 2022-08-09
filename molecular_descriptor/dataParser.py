import os
import pandas as pd
from biopandas.pdb import PandasPdb
from clean_smiles import *


class Parser:
    def __init__(self, data):
        if data is None:
            print("Please, input a .csv or excel file!")
        if data.endswith('.csv'):
            self.data = pd.read_csv(data)
        if data.endswith('.pdb'):
            self.mol = Chem.MolFromPDBFile(data)
            self.smileFromMol = Chem.MolToSmiles(self.mol)
            self.pdbRep = {}
            self.pdbRep['SMILES'] = self.smileFromMol
            self.data = pd.DataFrame([self.pdbRep])
            print(self.pdbRep)

        else:
            self.data = pd.read_excel(data)

    def getDf(self):
        return self.data

    def getSmiles(self):
        return self.data['SMILES']
