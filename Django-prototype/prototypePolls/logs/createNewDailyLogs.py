'''
//LOGIN
traze = "1 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + username + " | " + client_ip + " | " + user_agent + "\n"

// LOGOUT
traze = "2 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + username + " | " + client_ip + " | " + user_agent + "\n"

// NEW SIMULATION
traze = "3 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + user.username + " | " + client_ip + " | " + simulation_type + " | " + exercise_id + " | " + host.ip + " | " + container.id + " | " + user_agent + "\n"

// END SIMULATION?
traze = "4 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + user.username + " | " + client_ip + " | " + simulation_type + " | " + exercise_id + " | " + host.ip + " | " + container.id + " | " + user_agent + "\n"


// ERROR
traze = "5 | 500 Internal Server Error" + "\n"

//NOMBRE FICHEROS DE LOG
"/logs/" + str(date.today()) + "-log.txt"
'''



from datetime import date, datetime, timedelta
import random
import string



users = ["admin", "cawadall", "donperfecto","legion_55", "curso02", "NATHAN", "Daniel", "naflash2016", "extremeplus_58"]
exercise = ["cuadrado_tello", "introduccion_python", "choca_gira_us", "mbot_dummy_example"]
simulator = ["real", "simulator"]

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))







for i in range(30):
    filename = str(date.today() - timedelta(days=i)) + "-log.txt"
    f= open("temporalDir/" + filename,"w+")

    loopReg = random.randint(0, 999)
    for j in range(loopReg):
        caseReg = random.randint(0,3)
        if(caseReg == 0):
            traze = "1 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + users[random.randint(0, len(users)-1)] + " | " + "00.00.00.00" + " | " + "user_agent" + "\n"
        elif(caseReg == 1):
            traze = "2 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + users[random.randint(0, len(users)-1)] + " | " + "00.00.00.00" + " | " + "user_agent" + "\n"
        elif(caseReg == 2):
            traze = "3 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + users[random.randint(0, len(users)-1)] + " | " + "00.00.00.00" + " | " + simulator[random.randint(0, len(simulator)-1)] + " | " + exercise[random.randint(0, len(exercise)-1)] + " | " + "00.00.00.00" + " | " + randomString(64) + " | " + "user_agent" + "\n"
        elif(caseReg == 3):
            traze = "4 | " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " | " + users[random.randint(0, len(users)-1)] + " | " + "00.00.00.00" + " | " + simulator[random.randint(0, len(simulator)-1)] + " | " + exercise[random.randint(0, len(exercise)-1)] + " | " + "00.00.00.00" + " | " + randomString(64) + " | " + "user_agent" + "\n"
        else:
            traze = "5 | 500 Internal Server Error" + "\n"

        f.write(traze)
    f.close()
