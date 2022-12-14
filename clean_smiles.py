from rdkit import Chem


class SmilesCleaner:
    def __init__(self, smiles):
        self.smiles = smiles
        self.mols = []

    def getCanonicaSmiles(self):
        try:
            self.mols = [Chem.MolFromSmiles(smi) for smi in self.smiles]
            self.smiles = [Chem.MolToSmiles(mol) for mol in self.mols]
        except Exception as e:
            print(e)
            print("\n\n********** Check your SMILES or pdb file **********\n\n")
            exit()
        return self.smiles
