# import pymongo
import os
import glob
from datetime import datetime


from django_elasticsearch_dsl import Document, Text, Date
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)

EXERCISEIDs = []

class SessionDocument(Document):
    type = Text()
    date = Date()
    username = Text()
    client_ip = Text()
    user_agent = Text()

    class Index:
        # Name of the Elasticsearch index
        name = 'kibotics_session_log'
        # See Elasticsearch Indices API reference for available settings
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

class SimulationDocument(Document):
    type = Text()
    date = Date()
    username = Text()
    client_ip = Text()
    simulation_type = Text()
    exercise_id = Text()
    user_agent = Text()

    class Index:
        # Name of the Elasticsearch index
        name = 'kibotics_simulation_log'
        # See Elasticsearch Indices API reference for available settings
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }


def formatDate(d):
    date = d.split(" ")[0]
    time = d.split(" ")[1]
    dateFormat = datetime(int(date[6:]), int(date[3:5]), int(date[0:2]),
                        int(time[0:2]), int(time[3:5]), int(time[6:]), 000)
    return dateFormat

path = 'LOGS/'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for file in files:
    print(file)
    f = open(file,"r")
    for line in f:
        lineList = line.split(" | ")
        if(lineList[0] == "1"):
            SessionDocument(
                type=1,
                date=formatDate(lineList[1]),
                username=lineList[2],
                client_ip=lineList[3],
                user_agent=lineList[4][:-1]
            ).save()
        elif (lineList[0] == "2"):
            SessionDocument(
                type=2,
                date=formatDate(lineList[1]),
                username=lineList[2],
                client_ip=lineList[3],
                user_agent=lineList[4][:-1]
            ).save()
        elif (lineList[0] == "3"):
            SimulationDocument(
                type=1,
                date= formatDate(lineList[1]),
                username=lineList[2],
                client_ip=lineList[3],
                simulation_type=lineList[4],
                exercise_id=lineList[5],
                user_agent=lineList[8][:-1]
            ).save()
            if lineList[5] not in EXERCISEIDs:
                EXERCISEIDs += [lineList[5]]
        elif (lineList[0] == "4"):
            SimulationDocument(
                type=2,
                date= formatDate(lineList[1]),
                username=lineList[2],
                client_ip=lineList[3],
                simulation_type=lineList[4],
                exercise_id=lineList[5],
                user_agent=lineList[8][:-1]
            ).save()
            if lineList[5] not in EXERCISEIDs:
                EXERCISEIDs += [lineList[5]]
    f.close

print(EXERCISEIDs)
