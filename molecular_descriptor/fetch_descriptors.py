from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors


class FetchDescriptors:
    def __init__(self, dataframe):
        self.mols = []
        self.Mol_descriptors = []
        self.dataframe = dataframe
        self.mols = [Chem.MolFromSmiles(i) for i in dataframe['SMILES']]
        self.calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
        self.desc_names = self.calc.GetDescriptorNames()
        for mol in self.mols:
            self.mol = Chem.AddHs(mol)
            self.descriptors = self.calc.CalcDescriptors(self.mol)
            self.Mol_descriptors.append(self.descriptors)

    def getDescr(self):
        return self.Mol_descriptors, self.desc_names
