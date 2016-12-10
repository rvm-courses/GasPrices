import zipfile
import sys
import os.path
from xml.etree import cElementTree

def generate_flat(filename):
    """Generate csv file from XML"""
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename) as f:
            file = f.open(f.namelist()[0])
    else:
        file = filename

    tree = cElementTree.parse(file)
    pdvs = tree.getroot()
    for pdv in pdvs:
        id_pdv = pdv.attrib['id']
        pop = pdv.attrib['pop']
        lat = pdv.attrib['latitude']
        lon = pdv.attrib['longitude']
        cp_pdv = pdv.attrib['cp']
        for prix in pdv.iter('prix'):
            date = prix.attrib['maj'] if 'maj' in prix.keys() else ''
            id_prix = prix.attrib['id'] if 'id' in prix.keys() else ''
            valeur = prix.attrib['valeur'] if 'valeur' in prix.keys() else ''
            nom = prix.attrib['nom'] if 'nom' in prix.keys() else ''
            row = ';'.join([id_pdv, cp_pdv, pop, lat, lon, date, id_prix, nom, valeur])
            print(row)
    if filename.endswith('.zip'):
        file.close()
        f.close()
    return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_xml.py <filename.zip | filename.xml>")
    elif not os.path.isfile(sys.argv[1]):
        print("Unable to find file")        
    else:
        generate_flat(sys.argv[1])

#generate_flat("/Users/MIGNOT/Downloads/PrixCarburants_annuel_2016/PrixCarburants_annuel_2016.zip")
