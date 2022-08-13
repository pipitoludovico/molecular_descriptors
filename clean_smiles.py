from rdkit import Chem
from rdkit.Chem import rdmolops

from dataParser import *


class SmilesCleaner:
    def __init__(self, smiles):
        self.smiles = smiles
        self.mols = []

    def getCanonicaSmiles(self):
        self.mols = [Chem.MolFromSmiles(smi) for smi in self.smiles]
        self.smiles = [Chem.MolToSmiles(mol) for mol in self.mols]
        return self.smiles
