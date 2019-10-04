import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def readfile():
    f= open("login.log","r")
    lines = f.readlines()

    filedata = {};

    for line in lines:
        #print(line[:-1])
        data = line.split(" - ");
        date = data[0];
        name = data[1][:-1]
        if(name in filedata):
            #filedata[name].append(date)
            filedata[name] += 1
        else:
            #filedata[name] = [date]
            filedata[name] = 1

    f.close()
    return filedata

filedata = readfile();

for data in filedata:
    print(data + " : " + str(filedata[data]))

index = list(filedata.keys())
entries = list(filedata.values())

print(index)
print(entries)
mean = np.mean(entries)
print(int(mean))
df = pd.DataFrame({'entries': entries}, index=index)
ax = df.plot.bar(x='Users', y='entries', rot=int(mean))
plt.show()
#plt.close("all")
#pandasData = pandas.DataFrame(filedata, index=[0])
#pandasData.hist()

#plt.show()
