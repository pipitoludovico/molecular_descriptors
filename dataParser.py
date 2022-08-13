import subprocess
import sys

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
            self.obabel_result = subprocess.check_output("obabel -i pdb " + sys.argv[1] + " -o smi", shell=True,
                                                         text=True)
            self.pdbRep = {}
            self.pdbRep['SMILES'] = str(self.obabel_result).split()[0]
            self.data = pd.DataFrame([self.pdbRep])
        if data.endswith('.xlml'):
            self.data = pd.read_excel(data)

    def getDf(self):
        return self.data

    def getSmiles(self):
        return self.data['SMILES']
