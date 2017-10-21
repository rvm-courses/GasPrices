import zipfile
import sys
import argparse
import os.path
from xml.etree import cElementTree

def generate_prices(filename, header=False):
    """Generate prices to csv file from XML"""

    if header:
        print(';'.join(['id', 'cp', 'pop', 'lat', 'long', 'date', 'type', 'name', 'prix']))
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename) as zfile:
            file = zfile.open(zfile.namelist()[0])
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
        zfile.close()
    return

def generate_stations(filename, header=False):
    """Generate stations (pdv) to csv file from XML"""

    if header:
        print(';'.join(['id', 'cp', 'pop', 'lat', 'long', 'date', 'type', 'name', 'prix']))
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename) as zfile:
            file = zfile.open(zfile.namelist()[0])
    else:
        file = filename

    tree = cElementTree.parse(file)
    pdvs = tree.getroot()
    for pdv in pdvs:
        id_pdv = pdv.attrib['id']
        pop = pdv.attrib['pop']
        lat = pdv.attrib['latitude']
        lon = pdv.attrib['longitude']
        adresse = pdv.find('adresse').text
        ville = pdv.find('ville').text
        cp_pdv = pdv.attrib['cp']
        row = '|'.join([id_pdv, cp_pdv, pop, lat, lon, adresse, ville])
        print(row)
    if filename.endswith('.zip'):
        file.close()
        zfile.close()
    return

def generate_services(filename, header=False):
    """Generate services to csv file from XML"""

    if header:
        print(';'.join(['id', 'cp', 'pop', 'lat', 'long', 'services']))
    if filename.endswith('.zip'):
        with zipfile.ZipFile(filename) as zfile:
            file = zfile.open(zfile.namelist()[0])
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
        services = ','.join([service.text for service in pdv.iter('service')])
        row = '|'.join([id_pdv, cp_pdv, pop, lat, lon, services])
        print(row)
    if filename.endswith('.zip'):
        file.close()
        zfile.close()
    return

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Extract gas stations data to flat files.')
    PARSER.add_argument('file', help='XML file to process')
    PARSER.add_argument('--services', help='to extract services information', \
                        action="store_true")
    PARSER.add_argument('--stations', help='to extract services information', \
                        action="store_true")
    PARSER.add_argument('--header', help='to add header to the file', \
                        action="store_true")
    ARGS = PARSER.parse_args()

    if not os.path.isfile(ARGS.file):
        print("Unable to find file")
    elif ARGS.services:
        generate_services(ARGS.file, header=ARGS.header)
    elif ARGS.stations:
        generate_stations(ARGS.file, header=ARGS.header)
    else:
        generate_prices(ARGS.file, header=ARGS.header)
