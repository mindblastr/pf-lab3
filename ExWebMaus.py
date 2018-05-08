#!/usr/bin/python

from scipy.io import wavfile
import requests
import csv
import urllib
from BeautifulSoup import BeautifulSoup
import sys

filename = '/home/ubuntu/Documents/PF/lab3/data/dev/' + sys.argv[1]
files = {
    'OUTFORMAT': (None, 'csv'),
    'PRESEG': (None, 'false'),
    'LANGUAGE': (None, 'deu-DE'),
    'WEIGHT': (None, 'default'),
    'MAUSSHIFT': (None, 'default'),
    'OUTSYMBOL': (None, 'sampa'),
    'MINPAUSLEN': (None, '5'),
    'INSPROB': (None, '0.0'),
    'SIGNAL': (sys.argv[1], open(filename, 'rb')),
}


response = requests.post('https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runMINNI',files=files)
name = sys.argv[1][:-4]
csvFile = open('./dev/' + name + '.csv', 'w')
soup = BeautifulSoup(response.content);
csvFile.write(urllib.urlopen(soup.webserviceresponselink.downloadlink.string).read())
