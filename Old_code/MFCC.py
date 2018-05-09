#!/usr/bin/python

from scipy.io import wavfile
import scipy.stats
import csv
import sys
import re
from python_speech_features import mfcc
import numpy as np

filename = './dev/' + sys.argv[1]

newfile = open(sys.argv[1][:-4] + '_v_mfcc.csv', 'w')

with open(filename, 'r') as file:
    filedata = file.read()
    filedata = re.sub(';', ',', filedata)

with open(filename,'w') as file:
    file.write(filedata)

I = E = a = O = U = Y = _9  = arr = _6 = np.zeros(13)
i = e = E_ = a_ = o = u = y = _2 = np.zeros(13)
nI = nE = na = nO = nU = nY = n_9  = narr = n_6 = 0
ni = ne = nE_ = na_ = no = nu = ny = n_2 = 0
b = 0
aux = np.zeros(13)

audio = '/home/ubuntu/Documents/PF/lab3/data/dev/' + sys.argv[1][:-4] + '.wav'
fs, data = wavfile.read(audio)

with open(filename, 'r') as file:

    reader = csv.DictReader(file)

    for row in reader:

        start = int(np.floor(int(row['BEGIN'])))
        end = int(np.floor(int(row['BEGIN'])+int(row['DURATION'])))

        if(row['MAU'] == '@'):
            aux = mfcc(data,fs)
            print aux
            arr = arr + aux
            narr = narr + 1
            continue
        if(row['MAU'] == 'a'):
            aux = mfcc(data,fs)
            a = aux + a
            na = na + 1
            continue
        if(row['MAU'] == '9'):
            aux = mfcc(data,fs)
            _9 = aux + _9
            n_9 = n_9 + 1
            continue
        if(row['MAU'] == 'I'):
            aux = mfcc(data,fs)
            I = aux + I
            nI = nI + 1
            continue
        if(row['MAU'] == 'E'):
            aux = mfcc(data,fs)
            E = aux + E
            nE = nE + 1
            continue
        if(row['MAU'] == 'O'):
            aux = mfcc(data,fs)
            O = aux + O
            nO = nO + 1
            continue
        if(row['MAU'] == 'U'):
            aux = mfcc(data,fs)
            U = aux + U
            nU = nU + 1
            continue
        if(row['MAU'] == 'Y'):
            aux = mfcc(data,fs)
            Y = aux + Y
            nY = nY + 1
            continue
        if(row['MAU'] == '6'):
            aux = mfcc(data,fs)
            _6 = aux + _6
            n_6 = n_6 + 1
            continue

        if(row['MAU'] == 'i:'):
            aux = mfcc(data,fs)
            i = aux + i
            ni = ni + 1
            continue
        if(row['MAU'] == 'e:'):
            aux = mfcc(data,fs)
            e = aux + e
            ne = ne + 1
            continue
        if(row['MAU'] == 'E:'):
            aux = mfcc(data,fs)
            E_ = aux + E_
            nE_ = nE_ + 1
            continue
        if(row['MAU'] == 'a:'):
            aux = mfcc(data,fs)
            a_ =aux + a_
            na_ = na_ + 1
            continue
        if(row['MAU'] == 'o:'):
            aux = mfcc(data,fs)
            o = aux + o
            no = no + 1
            continue
        if(row['MAU'] == 'u:'):
            aux = mfcc(data,fs)
            u = aux + u
            nu = nu + 1
            continue
        if(row['MAU'] == 'y:'):
            aux = mfcc(data,fs)
            y = aux + y
            ny = ny + 1
            continue
        if(row['MAU'] == '2:'):
            aux = mfcc(data,fs)
            _2 = aux + _2
            n_2 = n_2 + 1
            continue
        end = 0;
        start = 0;
        aux = np.zeros(13)

if(narr == 0):
    arr = -1
    narr = 1
if(na == 0):
    a = -1
    na = 1
if(n_9 == 0):
    _9 = -1
    n_9 = 1
if(nI == 0):
    I = -1
    nI = 1
if(nE == 0):
    E = -1
    nE = 1
if(nO == 0):
    O = -1
    nO = 1
if(nU == 0):
    U = -1
    nU = 1
if(nY == 0):
    Y = -1
    nY = 1
if(n_6 == 0):
    _6 = -1
    n_6 = 1
if(ni == 0):
    i = -1
    ni = 1
if(ne == 0):
    e = -1
    ne = 1
if(nE_ == 0):
    E_ = -1
    nE_ = 1
if(na_ == 0):
    a_ = -1
    na_ = 1
if(no == 0):
    o = -1
    no = 1
if(nu == 0):
    u = -1
    nu = 1
if(ny == 0):
    y = -1
    ny = 1
if(n_2 == 0):
    _2 = -1
    n_2 = 1

newfile.write('@,' + str(arr/narr) + ',\n')
newfile.write('a,' + str(a/na) + ',\n')
newfile.write('_9,' + str(_9/_9) + ',\n')
newfile.write('I,' + str(I/nI) + ',\n')
newfile.write('E,' + str(E/nE) + ',\n')
newfile.write('O,' + str(O/nO) + ',\n')
newfile.write('U,' + str(U/nU) + ',\n')
newfile.write('Y,' + str(Y/nY) + ',\n')
newfile.write('6,' + str(_6/n_6) + ',\n')
newfile.write('i:,' + str(i/ni) + ',\n')
newfile.write('e:,' + str(e/ne) + ',\n')
newfile.write('E:,' + str(E_/nE_) + ',\n')
newfile.write('a:,' + str(a_/na_) + ',\n')
newfile.write('o:,' + str(o/no) + ',\n')
newfile.write('u:,' + str(u/nu) + ',\n')
newfile.write('y:,' + str(y/ny) + ',\n')
newfile.write('2:,' + str(_2/n_2) + ',\n')

newfile.close()
