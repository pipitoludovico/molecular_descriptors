from dataParser import *
from clean_smiles import *
from filter import *
from fetch_descriptors import *
from rdkit.Chem import PandasTools


def main():
    reader = Parser(sys.argv[1])
    cleaner = SmilesCleaner(reader.getSmiles())
    canonical = cleaner.getCanonicaSmiles()
    reader.data['SMILES'] = canonical
    filtered = Filter(reader.data).getFiltered()

    df = pd.DataFrame(filtered)
    desc = FetchDescriptors(df)
    Mol_desc, desc_name = desc.getDescr()
    df_full_descr = pd.DataFrame(Mol_desc, columns=desc_name)
    clean_df = df_full_descr[
        ['ExactMolWt', 'HeavyAtomCount', 'NumHAcceptors', 'NumHDonors', 'NumAromaticRings', 'NumRotatableBonds',
         'MolLogP']]
    ddf = df.join(clean_df, how='left')
    # ddf.to_excel('test.xls')
    PandasTools.AddMoleculeColumnToFrame(ddf, smilesCol='SMILES')
    ddf.dropna(axis=1, how="any", inplace=True)
    PandasTools.SaveXlsxFromFrame(ddf, 'output.xlsx', molCol='ROMol')
    print(ddf)


if __name__ == '__main__':
    main()
