import os
from math import sqrt,isnan

def convert(filename):
    retval = ""
    with open(filename, 'r') as fp:
        values = []
        count = 0
        total = 0
        for line in fp:
            line = line.rstrip('\n')
            line_values = line.split(',')
            line_values.pop(0)
            if len(line_values) > 1 :
                for value in line_values:
                    if len(value) < 2 or value == '\n':
                        continue
                    values.append(float(value))
                    total += float(value)
                    count+=1
            else:
                    values.append(float('nan'))
    
        for i in range(len(values)):
            retval += str(values[i])
            if i < len(values) -1:
                retval += ','

    retval += '\n'
    return retval
def gather_dir(dirname):
    with open(dirname + "_converted.csv",'w') as output:     
        for filename in os.listdir(dirname):
            output.write(convert(dirname + "/" + filename))

    print("Done")


#gather_dir(os.getcwd() + "/MFCC/train")
gather_dir(os.getcwd() + "/MFCC/train")
gather_dir(os.getcwd() + "/MFCC/dev")