
ignored_logs = ["Error ==> 500 Internal Server Error"]

def filter(line, param, pos):
    if("" == param):
        return True
    return line.split(" ")[pos] == param

def readfile(name="", simType="", exercise=""):
    paramsPos = [5, 7, 8]
    params = [name, simType, exercise]

    f= open("access_log_django.txt","r")
    lines = f.readlines()
    #print(len(lines))
    filedata = [];

    for line in lines:
        if line[:-1] not in str(ignored_logs):
            i = 0
            filtered = True
            #print(line)
            for param in params:
                if (not filter(line, param, paramsPos[i])):
                    filtered = False
                #print("\t"+str(filtered))
                i+=1

            if filtered:
                filedata.append(line)
    f.close()
    return filedata

def plotSimTYpe(data):
    baseDataSim = {}

    for d in data:
        name = d.split(" ")[5]
        simType = d.split(" ")[7]
        exercise = d.split(" ")[8]

        if(name in baseDataSim):
            if(simType in baseDataSim[name]):
                baseDataSim[name][simType] += 1
            else:
                baseDataSim[name][simType] = 1
        else:
            baseDataSim[name] = {}
            baseDataSim[name][simType] = 1


    return baseDataSim


def plotExercise(data):
    baseDataExer = {}

    for d in data:
        name = d.split(" ")[5]
        simType = d.split(" ")[7]
        exercise = d.split(" ")[8]

        if(name in baseDataExer):
            if(exercise in baseDataExer[name]):
                baseDataExer[name][exercise] += 1
            else:
                baseDataExer[name][exercise] = 1
        else:
            baseDataExer[name] = {}
            baseDataExer[name][exercise] = 1

    return baseDataExer


if __name__ == "__main__":
    data = readfile("admin", "", "")

    print(plotSimTYpe(data))
    print(plotExercise(data))
