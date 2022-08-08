class Filter:
    def __init__(self, df):
        self.dataset_new = None
        self.df = df.drop_duplicates(subset=['SMILES']).reset_index(drop=True)

    def getFiltered(self):
        return self.df
