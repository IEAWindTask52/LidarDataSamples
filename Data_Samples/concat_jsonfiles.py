import os
import glob
import pathlib
import pandas
import json
import shutil
import tabulate
import urllib.parse

source_directory = 'Data_Samples'
source_file_type = ".json"
output_directory = "."
output_json_file = "LidarDataSamples.json"
output_md_file = "LidarDataSamples.md"

# generate a list of JSON files
files = list(pathlib.Path(source_directory).glob('*' + source_file_type))
print(files)

# concatenate all of the json data into one big file
with open(os.path.join(output_directory, output_json_file), "w") as t:
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

# read the JSON file and convert to a markdown table for Github
fileData = json.load(open(os.path.join(output_directory, output_json_file)))
df_in = pandas.DataFrame.from_dict(fileData)

# simplify the df
df = pandas.DataFrame(df_in['Data samples']['Data sample'])

# modify the df to have a short link to the data provider
df['Data provider md'] = "[" + df['Data provider'] + \
    "](" + df['Data provider URL'] + ")"

# modify the df to have a short link to the data


def md_formatted_link(url):
    return "[" + urllib.parse.urlparse(url).netloc + "](" + url + ")"


df['Data sample URL md'] = df.apply(
    lambda row: md_formatted_link(row['Data sample URL']), axis=1)

# modify the df to have a short link to the license
df['Data license md'] = "[" + df['Data sample license name'] + \
    "](" + df['Data sample license URL'] + ")"

# choose the outputs we want
tablecols = ['Title',
             'Data provider md',
             'Description',
             'Data sample URL md',
             "Data license md"]
tableheaders = ['Device',
                'Provider',
                'Description',
                'Link to data',
                'License']
with open(os.path.join(output_directory, output_md_file), "w") as t:
    t.write(tabulate.tabulate(df[df.columns.intersection(
        tablecols)], headers=tableheaders, tablefmt="github"))
