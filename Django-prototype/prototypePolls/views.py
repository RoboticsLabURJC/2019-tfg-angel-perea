from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render_to_response

from .models import Question, Session, Simulation


from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import datetime
from datetime import datetime, timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def formatStringDate(strDate):
    datetime_object = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S')
    return datetime.strptime(strDate, "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

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


def loadDDBB(request):
    fromDate = request.GET.get('from_date')
    toDate = request.GET.get('to_date')
    if(fromDate != ''and toDate != ""):
        start_date = date(int(fromDate.split(" ")[0]), int(fromDate.split(" ")[1]), int(fromDate.split(" ")[2]))
        end_date = date(int(toDate.split(" ")[0]), int(toDate.split(" ")[1]), int(toDate.split(" ")[2]))
        for single_date in daterange(start_date, end_date):
            file = single_date.strftime("%Y-%m-%d")+'-log.txt'
            try:
                dir = 'prototypePolls/logs/temporalDir/' + file
                print(dir)
                f = open(dir,"r")
                for line in f:
                    lineList = line.split(" | ")
                    if(lineList[0] == "1"):
                        addSession("New", lineList)
                    elif (lineList[0] == "2"):
                        addSession("End", lineList)
                    elif (lineList[0] == "3"):
                        addSimulation("New", lineList)
                    elif (lineList[0] == "4"):
                        addSimulation("End", lineList)
                f.close
            except FileNotFoundError as e:
                print(e)

    s = Session.objects.all()
    s2 = Simulation.objects.all()
    context = {'Session': s, 'Simulation': s2}
    return render(request, 'prototypePolls/interactivePlot.html', context)


def deleteDDBB(request):
    Simulation.objects.all().delete()
    Session.objects.all().delete()
    s = Session.objects.all()
    s2 = Simulation.objects.all()
    context = {'Session': s, 'Simulation': s2}
    return render(request, 'prototypePolls/interactivePlot.html', context)

def interactivePlot(request):
    s = Session.objects.all()
    s2 = Simulation.objects.all()
    context = {'Session': s, 'Simulation': s2}
    return render(request, 'prototypePolls/interactivePlot.html', context)






def readfile_OLD():
    f= open("prototypePolls/logs/login.log","r")
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


def home(request):
    return render(request, "prototypePolls/plot1.html")

def plot1(request):
    filedata = readfile_OLD();
    index = list(filedata.keys())
    entries = list(filedata.values())

    print(index)
    print(entries)

    f = plt.figure()
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(index, entries)
    axes.set_xlabel("Users")
    axes.set_ylabel("Entries")
    axes.set_title("PLOT 1")

    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    response = HttpResponse(buf.getvalue(), content_type='image/png')

    f.clear()

    response['Content-Length'] = str(len(response.content))

    return response


ignored_logs = ["Error ==> 500 Internal Server Error"]

def filter(line, param, pos):
    if("" == param):
        return True
    return line.split(" ")[pos] == param

def readfile(name="", simType="", exercise=""):
    paramsPos = [5, 7, 8]
    params = [name, simType, exercise]

    f= open("prototypePolls/logs/access_log_django.txt","r")
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

def logPlotAll(request):
    #argsList = args.split("#")
    data = readfile("", "", "")
#str(plotSimTYpe(data))+"@"+str(plotExercise(data))
    dataDict = plotSimTYpe(data)
    #return render(request, 'prototypePolls/blank.html', plotSimTYpe(data))

    index = []
    entries = []
    users = list(dataDict.keys())
    for d in users:
        index += list(dataDict[d].keys())
        entries += list(dataDict[d].values())

    f = plt.figure()
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(index, entries)
    axes.set_xlabel("Users")
    axes.set_ylabel("Entries")
    axes.set_title("PLOT 1")

    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    response = HttpResponse(buf.getvalue(), content_type='image/png')

    f.clear()

    response['Content-Length'] = str(len(response.content))

    return response

def logPlot(request, name):
    #argsList = args.split("#")
    data = readfile(name, "", "")
#str(plotSimTYpe(data))+"@"+str(plotExercise(data))
    dataDict = plotSimTYpe(data)
    #return render(request, 'prototypePolls/blank.html', plotSimTYpe(data))

    index = []
    entries = []
    users = list(dataDict.keys())
    for d in users:
        index += list(dataDict[d].keys())
        entries += list(dataDict[d].values())

    f = plt.figure()
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(index, entries)
    axes.set_xlabel("Users")
    axes.set_ylabel("Entries")
    axes.set_title("PLOT 1")

    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    response = HttpResponse(buf.getvalue(), content_type='image/png')

    f.clear()

    response['Content-Length'] = str(len(response.content))

    return response


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'prototypePolls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'prototypePolls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'prototypePolls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'prototypePolls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('prototypePolls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'prototypePolls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'prototypePolls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'prototypePolls/results.html'
