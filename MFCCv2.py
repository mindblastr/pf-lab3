#!/usr/bin/python

from scipy.io import wavfile
import scipy.stats
import csv
import sys
import os
import re
import defs
from python_speech_features import mfcc
import numpy as np

class Character:

    def __init__(self):
        self.data = np.zeros(13)
        self.n = 0

    def data(self):
        return self.data

    def count(self):
        return self.n

    def add(self, n_d):
        self.data = np.add(n_d, self.data)
        self.n += 1

    def divide(self):
        self.data = self.data / self.n
        return self.data

    def set(self, n_d):
        self.data = n_d
        self.n = 1

    def isEmpty(self):
        return self.n == 0

    def clean(self):
        self.data = np.zeros(13)
        self.n = 0

vowels = {
    'I' : Character(),
    'E' : Character(),
    'a' : Character(),
    'O' : Character(),
    'U' : Character(),
    'Y' : Character(),
    '9' : Character(),
    '6' : Character(),
    'i:' : Character(),
    'e:' : Character(),
    'E:' : Character(),
    'a:' : Character(),
    'o:' : Character(),
    'u:' : Character(),
    'y:' : Character(),
    '2:' : Character(),
    '@': Character()
}

count = 0
folder = 'test/'
for filename in os.listdir(SRC_FOLDER + folder):
    count = count + 1

    newfile = open(SRC_FOLDER + 'MFCC/' + folder + filename[:-4] + '_v_mfcc.csv', 'w')

    with open(SRC_FOLDER+ folder + filename, 'r') as file:
        filedata = file.read()
        filedata = re.sub(';', ',', filedata)

    with open(SRC_FOLDER + folder + filename, 'w') as file:
        file.write(filedata)

    audio = DATA_FOLDER + folder + filename[:-4] + '.wav'
    fs, data = wavfile.read(audio)

    with open(SRC_FOLDER + folder + filename, 'r') as file:

        reader = csv.DictReader(file)

        for row in reader:

            start = int(np.floor(int(row['BEGIN'])))
            end = int(np.floor(int(row['BEGIN'])+int(row['DURATION'])))

            if vowels.get(row['MAU']) != None:
                data_ = mfcc(data[start:end],fs)
                aux = np.zeros(data_[0].size)

                k = 0
                for property in data_.T:
                    aux[k] = np.sum(property) / property.size
                    k+=1

                vowels[row['MAU']].add(aux)


    for key,value in vowels.items():
        if vowels[key].isEmpty():
           vowels[key].set(-1)

    a = 0
    for key,value in vowels.items():

        a = a + 1
        store = vowels[key].divide()

        newfile.write(key + ',')

        if(isinstance(store, np.ndarray)):
            np.savetxt(newfile, store, fmt='%.5f', newline=',')
        else:
            newfile.write('-1')

        newfile.write('\n')

    for key,value in vowels.items():
        vowels[key].clean()

    newfile.close()
