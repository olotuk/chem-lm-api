from rdkit import Chem
from rdkit.Chem import Descriptors

properties = {"MolWt" : Descriptors.MolWt, 
              "MolLogP" : Descriptors.MolLogP, 
              "NumHDonors" : Descriptors.NumHDonors, 
              "NumHAcceptors" : Descriptors.NumHAcceptors, 
              "TPSA" : Descriptors.TPSA, 
              "NumRotatableBonds" : Descriptors.NumRotatableBonds}



def featurize(smiles):
    molecule =  Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError (f"{smiles} non valido")
    valori_p = {}
    for name_p, property in properties.items():
        valore_p = property(molecule)
        valori_p[name_p] = valore_p
    return valori_p



