import os
import glob
import pathlib
import pandas
import json
import shutil

directory = 'Data_Samples'
file_type = ".json"

# generate a list of files
files = list(pathlib.Path(directory).glob('*' + file_type))

# concatenate all of the json data into one big file
with open("LidarDataSamples.json", "w") as t:
    t.write('{\n')
    t.write('\t"Data samples":  {\n')
    t.write('\t\t"Data sample":  [\n')
    i = 1
    for file in files:
        print(file)
        t.write('\t\t\t{\n')
        t.write('\t\t\t\t"id": "' + str(int(i)) + '",\n\t\t\t\t')
        # get the file content
        content = file.open().readlines()
        # write it out
        t.write('\t\t\t\t'.join(content))
        if len(list(files)) > 1:
            if i == len(list(files)):
                t.write('\n\t\t\t}\n')
            else:
                t.write('\n\t\t\t},\n')
        else:
            t.write('\n\t\t\t}\n')
        i = i+1.0
    t.write('\t\t]\n')
    t.write('\t}\n')
    t.write('}')

# read the table and convert to markdown
# with open("LidarDataSamples.json", "r") as t:
#    data = t.read()
