#! /usr/bin/python3
# -*- coding: utf-8 -*-

# import required libraries

from pymongo import MongoClient
import json
from datetime import datetime
import dateutil.parser
from tqdm import tqdm

# connect to mongodb

client = MongoClient("mongodb://localhost:27017/")

sensordb = client["sensordb"]

# load json data

data = open("/jsondata/data_json.json")

jsonfile = json.load(data)

# loads data into database

for y,x in tqdm(enumerate(jsonfile)):

    # Creating variables for each value to insert

    StationId = jsonfile[y]['StationId']

    Datetime = dateutil.parser.parse(datetime.strptime(jsonfile[y]	
    ['Datetime'],'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    Particulate = jsonfile[0]['Environmental_Metrics'][0]['Particulate_Matter']

    Nitrogen = jsonfile[0]['Environmental_Metrics'][0]['Nitrogen_Compounds']

    Other = jsonfile[0]['Environmental_Metrics'][0]['Other_Pollutants']

    Air = jsonfile[0]['Air_Quality_index']
    
    # inserting data 

    sensordb.sensors.insert_one(
        {
          "metadata": {"StationId": StationId },
          "timestamp": Datetime,
          "particulate_matter" : Particulate,
          "nitrogen_compounds" : Nitrogen,
          "other_pollutants" : Other,
          "air_quality_index" : Air
       },
    )

