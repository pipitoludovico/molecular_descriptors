import subprocess
import sys
from rdkit import Chem
from rdkit.Chem import Draw
import pandas as pd


class Parser:
    def __init__(self, data):
        if data is None:
            print("Please, input a .csv or excel file!")
        if data.endswith('.csv'):
            self.data = pd.read_csv(data)
        if data.endswith('.pdb'):
            try:
                self.obabel_result = subprocess.check_output("obabel -i pdb " + sys.argv[1] + " -o smi", shell=True,
                                                             text=True)
                self.pdbRep = {}
                self.pdbRep['SMILES'] = str(self.obabel_result).split()[0]
                self.draw = Chem.MolFromSmiles(str(self.obabel_result).split()[0])
                self.data = pd.DataFrame([self.pdbRep])
                Draw.MolToFile(self.draw, f"{str(sys.argv[1]).replace('.pdb', '.png')}")
            except:
                self.mol = Chem.MolFromPDBFile(data)
                self.smileFromMol = Chem.MolToSmiles(self.mol)
                self.pdbRep = {}
                self.pdbRep['SMILES'] = self.smileFromMol
                self.data = pd.DataFrame([self.pdbRep])
                Draw.MolToFile(self.mol, f"{str(sys.argv[1]).replace('.pdb', '.png')}")

        if data.endswith('.xlml'):
            self.data = pd.read_excel(data)

    def getDf(self):
        return self.data

    def getSmiles(self):
        return self.data['SMILES']
