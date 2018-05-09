#!/usr/bin/python
from scipy.io import wavfile
import requests
import csv
import urllib
import defs
from BeautifulSoup import BeautifulSoup
import sys

i = 0

for filename in os.listdir(DATA_FOLDER + 'train/'):
    print(i)
    filepath = DATA_FOLDER + 'train/' + filename
    fileProperties = {
        'OUTFORMAT': (None, 'csv'),
        'PRESEG': (None, 'false'),
        'LANGUAGE': (None, 'deu-DE'),
        'WEIGHT': (None, 'default'),
        'MAUSSHIFT': (None, 'default'),
        'OUTSYMBOL': (None, 'sampa'),
        'MINPAUSLEN': (None, '5'),
        'INSPROB': (None, '0.0'),
        'SIGNAL': (filename, open(filepath, 'rb')),
    }

    name = filename[:-4]
    csvFile = open('./train/' + name + '.csv', 'w')
    response = requests.post('https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runMINNI',files=fileProperties)
    soup = BeautifulSoup(response.content);
    csvFile.write(urllib.urlopen(soup.webserviceresponselink.downloadlink.string).read())
    csvFile.close()
    i = i + 1
