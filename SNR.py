#!/usr/bin/python

from scipy.io import wavfile
import scipy.stats
import defs
import csv
import sys
import re

filename = './dev/' + sys.argv[1]

newfile = open('vowel_loud.csv', 'w')

with open(filename, 'r') as file:
    filedata = file.read()
    filedata = re.sub(';', ',', filedata)

with open(filename,'w') as file:
    file.write(filedata)

I = E = a = O = U = Y = _9  = arr = _6 = 0
_i = _e = E_ = a_ = o = u = y = _2 = 0
nI = nE = na = nO = nU = nY = n_9  = narr = n_6 = 0
n_i = n_e = nE_ = na_ = no = nu = ny = n_2 = 0
aux = 0

audio = DATA_FOLDER + 'dev/' + sys.argv[1][:-4] + '.wav'
fs, data = wavfile.read(audio)

with open(filename, 'r') as file:

    reader = csv.DictReader(file)

    for row in reader:

        if(row['MAU'] == '@'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            arr = arr + aux
            narr = narr + 1
            continue
        if(row['MAU'] == 'a'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            a = a + aux
            na = na + 1
            continue
        if(row['MAU'] == '9'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            _9 = _9 + aux
            n_9 = n_9 + 1
            continue
        if(row['MAU'] == 'I'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            I = I + aux
            nI = nI + 1
            continue
        if(row['MAU'] == 'E'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            E = E + aux
            nE = nE + 1
            continue
        if(row['MAU'] == 'O'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            O = O + aux
            nO = nO + 1
            continue
        if(row['MAU'] == 'U'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            U = U + aux
            nU = nU + 1
            continue
        if(row['MAU'] == 'Y'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            Y = Y + aux
            nY = nY + 1
            continue
        if(row['MAU'] == '6'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            _6 = _6 + aux
            n_6 = n_6 + 1
            continue

        if(row['MAU'] == 'i:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            _i = _i + aux
            n_i = n_i + 1
            continue
        if(row['MAU'] == 'e:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            _e = _e + aux
            n_e = n_e + 1
            continue
        if(row['MAU'] == 'E:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            E_ = E_ + aux
            nE_ = nE_ + 1
            continue
        if(row['MAU'] == 'a:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            a_ = a_ + aux
            na_ = na_ + 1
            continue
        if(row['MAU'] == 'o:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            o = o + aux
            no = no + 1
            continue
        if(row['MAU'] == 'u:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            u = u + aux
            nu = nu + 1
            continue
        if(row['MAU'] == 'y:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            y = y + aux
            ny = ny + 1
            continue
        if(row['MAU'] == '2:'):
            aux = scipy.stats.signaltonoise(data[foor(fs*row[BEGIN]):floor(fs*row[BEGIN]+row[DURATION])])
            _2 = _2 + aux
            n_2 = n_2 + 1
            continue


newfile.append('@ =', arr/narr)
newfile.append('a =', a/na)
newfile.append('_9 =', _9/n_9)
newfile.append('I =', I/nI)
newfile.append('E =', E/nE)
newfile.append('O =', O/nO)
newfile.append('U =', U/nU)
newfile.append('Y =', Y/nY)
newfile.append('6 =', _6/n_6)
newfile.append('i: =', _i/n_i)
newfile.append('e: =', _e/n_e)
newfile.append('E: =', E_/nE_)
newfile.append('a: =', a_/na_)
newfile.append('o: =', o/no)
newfile.append('u: =', u/nu)
newfile.append('y: =', y/ny)
newfile.append("2: =", _2/n_2)

newfile.close()
