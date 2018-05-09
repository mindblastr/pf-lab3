#!/usr/bin/python

#!/usr/bin/python

from scipy.io import wavfile
import scipy.stats
import csv
import sys
import os
import re
from python_speech_features import mfcc
import numpy as np
import Signal_Analysis as sn

class Character:

    def __init__(self):
        self.data = 0
        self.n = 0

    def data(self):
        return self.data

    def count(self):
        return self.n

    def add(self, n_d):
        self.data = self.data + n_d
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
        self.data = 0
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
for filename in os.listdir('/home/ubuntu/Documents/PF/lab3/Development/' + folder):

    print count
    count = count + 1

    newfile = open('/home/ubuntu/Documents/PF/lab3/Development/' + 'HNR/' + folder + filename[:-4] + '_v_hnr.csv', 'w')

    with open('/home/ubuntu/Documents/PF/lab3/Development/' + folder + filename, 'r') as file:
        filedata = file.read()
        filedata = re.sub(';', ',', filedata)

    with open('/home/ubuntu/Documents/PF/lab3/Development/' + folder + filename, 'w') as file:
        file.write(filedata)

    audio = '/home/ubuntu/Documents/PF/lab3/data/'+ folder + filename[:-4] + '.wav'
    fs, data = wavfile.read(audio)

    with open('/home/ubuntu/Documents/PF/lab3/Development/' + folder + filename, 'r') as file:

        reader = csv.DictReader(file)

        for row in reader:

            start = int(np.floor(int(row['BEGIN'])))
            end = int(np.floor(int(row['BEGIN'])+int(row['DURATION'])))

            if vowels.get(row['MAU']) != None:
                data_ = sn.features.signal.get_HNR(data[start:end],fs)
                vowels[row['MAU']].add(data_)


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
