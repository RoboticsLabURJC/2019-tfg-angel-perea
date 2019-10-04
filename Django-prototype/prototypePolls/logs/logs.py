
import random
import time

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y %I:%M %p', prop)

#print(random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random()))
users = ["Jonatan", "Carlos", "Mariví", "Adrian", "Luis", "Oscar", "Rita", "Felipe", "Rocio", "Angel", "Fernando", "Rapha", "Jaime", "Criss"]



f= open("login.log","a")


for i in range(99999):
    date = random_date("1/1/2018 1:01 AM", "31/12/2018 11:59 PM", random.random())
    user = users[random.randint(0,len(users)-1)]
    f.write(date + " - " + user +'\n')


f.close()
