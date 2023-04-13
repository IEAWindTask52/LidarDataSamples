[![build unified data sample file](https://github.com/IEAWindTask52/LidarDataSamples/actions/workflows/main.yml/badge.svg)](https://github.com/IEAWindTask52/LidarDataSamples/actions/workflows/main.yml)

# Lidar Data Samples

This repository provides links to wind lidar data samples with known provenance.

## Data samples

|    | Device   | Provider                                        | Description                            | Link to data                                                                                 | License                     |
|----|----------|-------------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------|
|  0 | ZX300    |                                                 | [ZX Lidars](https://www.zxlidars.com/) | [drive.google.com](https://drive.google.com/drive/folders/1Ji7zaT7CWh9GXMvuC7MeJ48VsPws_9PP) | [none](none)                |
|  1 | ZX300    | Copy of another file to test file concatenation | [ZX Lidars](https://www.zxlidars.com/) | [drive.google.com](https://drive.google.com/drive/folders/1Ji7zaT7CWh9GXMvuC7MeJ48VsPws_9PP) | [no license provided](none) |

## Add a data sample

If you would like to add a data sample, please []

# Data converters

<details>
<summary>Notes for maintainers</summary>
This repository contains the following files:

This repository contains the following files:

1. `README.md` is an automatically created index file. It uses the template in `README.stub`. Other data are imported into the file by a github action that runs whenever a commit happens. The data that are imported include:
  - `LidarDataSamples.json`
2. `LidarDataSamples.json` is created by processing and concatenating the .json files in `/Data_Samples`. 
  - To edit this file, edit the individual .json files in `/Data_Samples` then commit and push the data to Github, or run `concat_jsonfiles.py` locally.
3. To add a data sample, copy one of the existing .json files in `/Data_Samples` and update it with the new details.


</details>
