import os
from math import sqrt,isnan

def convert(dirname,tp,filename):
    retval = ""
    mfccFileName = dirname + "/MFCC" + tp + filename

    hnrFileName = dirname + "/HNR" + tp + filename
    hnrFileName = hnrFileName.replace("_mfcc","_hnr")

    with open(mfccFileName, 'r') as mfcc:
        with open(hnrFileName,'r') as hnr:
            values = []
            count = 0
            total = 0
            for line in mfcc:

                hnrline = hnr.readline()
                hnrvaluesStr = hnrline.split(',')
                hnrvalue= float(hnrvaluesStr[1])
                if(round(hnrvalue,5) == -1.00):
                    hnrvalue = float(0)

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
                values.append(hnrvalue)
        
            for i in range(len(values)):
                retval += str(values[i])
                if i < len(values) -1:
                    retval += ','

    return retval

def convertNHR(filename):
    with open(filename, 'r') as fp:
        for line in fp:
            line_values = line.split(',')
            line_values.pop(0)

def gather_dir(dirname,tp):
    with open(dirname + "/" + tp + "_converted.csv",'w') as output:     
        for filename in os.listdir(dirname + "/MFCC/" + tp):
            output.write(convert(dirname,"/"+tp+"/",filename))
            output.write('\n')
    print("Done")


#gather_dir(os.getcwd() + "/MFCC/train")
gather_dir(os.getcwd(), "train")
gather_dir(os.getcwd(), "dev")