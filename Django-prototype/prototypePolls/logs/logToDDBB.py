'''
from prototypePolls.models import Simulation, Session
from datetime import date, datetime, timedelta
import datetime

Simulation.objects.all()
Session.objects.all()

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


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

Simulation.objects.all()
Session.objects.all()
'''


from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def formatStringDate(strDate):
    datetime_object = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S')
    return datetime.datetime.strptime(datetime_object, "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

def addSession(type, data):
    datetime_str = str(data[1])
    datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
    s = Session(
        type = type,
        date = formatStringDate(data[1]),
        username = data[2],
        client_ip = data[3],
        user_agent = data[4]
    )
    s.save()

def addSimulation(type, data):
    datetime_str = str(data[1])
    datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
    Simulation(
        type = type,
        date = formatStringDate(data[1]),
        username = data[2],
        client_ip = data[3],
        simulation_type = data[4],
        exercise_id = data[5],
        host_ip = data[6],
        container_id = data[7],
        user_agent = data[8]
    ).save()

start_date = date(2019, 9, 1)
end_date = date(2019, 10, 19)
for single_date in daterange(start_date, end_date):
    file = single_date.strftime("%Y-%m-%d")+'-log.txt'
    try:
        dir = 'temporalDir/' + file
        print (dir)
        f = open(dir,"r")
        for line in f:
            print(line.split(" | ")[:-2])
            lineList = line.split(" | ")
            if(lineList[0] == 1):
                addSession("New", lineList)
            elif (lineList[0] == 2):
                addSession("End", lineList)
            elif (lineList[0] == 3):
                addSimulation("New", lineList)
            elif (lineList[0] == 4):
                addSimulation("End", lineList)
        f.close
    except FileNotFoundError as e:
        print(e)
