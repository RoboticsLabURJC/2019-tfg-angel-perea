import pymongo
import os
import glob
from datetime import datetime
'''
datetime_str = str(now)
datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
Simulation(
    type = "New",
    date = datetime.datetime.strptime(datetime_object, "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S"),
    username = "USUARIO",
    client_ip = "CLIENT_IP",
    simulation_type = "SIMULATION_TYPE",
    exercise_id = "EXERCISE_ID",
    host_ip = "HOST_IP",
    container_id = "CONTAINER_ID",
    user_agent = "USER_AGENT"
).save()

datetime_str = str(now)
datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
s = Session(
    type = "New",
    date = datetime.datetime.strptime(datetime_object, "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S"),
    username = "USUARIO",
    client_ip = "CLIENT_IP",
    user_agent = "USER_AGENT"
)
s.save()
'''

def formatDate(d):
    date = d.split(" ")[0]
    time = d.split(" ")[1]
    dateFormat = datetime(int(date[6:]), int(date[3:5]), int(date[0:2]), 
                        int(time[0:2]), int(time[3:5]), int(time[6:]))
    return dateFormat

path = 'temporalDir/'
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["kiboticsDDBB"]


print(mydb.list_collection_names())
for col in mydb.list_collection_names():
    mycol = mydb[col]
    mycol.drop() 



files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for file in files:
    print(file)
    f = open(file,"r")
    for line in f:
        #print(line.split(" | ")[:-2])
        lineList = line.split(" | ")
        if(lineList[0] == "1"):
            mycol = mydb["newSession"]
            mydict = {
                    "date": formatDate(lineList[1]), 
                    "username": lineList[2], 
                    "client_ip": lineList[3], 
                    "user_agent": lineList[4]
                     }
            x = mycol.insert_one(mydict)
        elif (lineList[0] == "2"):
            mycol = mydb["endSession"]
            mydict = {
                    "date": formatDate(lineList[1]), 
                    "username": lineList[2], 
                    "client_ip": lineList[3], 
                    "user_agent": lineList[4]
                     }
            x = mycol.insert_one(mydict)
        elif (lineList[0] == "3"):
            mycol = mydb["newSimulation"]
            mydict = {
                    "date": formatDate(lineList[1]), 
                    "username": lineList[2], 
                    "client_ip": lineList[3], 
                    "simulation_type": lineList[4],
                    "exercise_id": lineList[5],
                    "host_ip": lineList[6],
                    "container_id": lineList[7],
                    "user_agent": lineList[8]
                     }
            x = mycol.insert_one(mydict)
        elif (lineList[0] == "4"):

            mycol = mydb["endSimulation"]
            mydict = {
                    "date": formatDate(lineList[1]), 
                    "username": lineList[2], 
                    "client_ip": lineList[3], 
                    "simulation_type": lineList[4],
                    "exercise_id": lineList[5]
                     }
            x = mycol.insert_one(mydict)
    f.close

print(mydb.list_collection_names())


#myquery = {"username": "admin"}

mycol = mydb["newSession"]
usuariosSession = mycol.find({}).distinct("username")
print(usuariosSession);
for user in usuariosSession:
    entries = mycol.find({"username" : user})
    print(entries.count());


mycol = mydb["newSimulation"]
usuariosSimulation = mycol.find({}).distinct("username")
print(usuariosSimulation);


