from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question


from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def readfile():
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




def plot1(request):
    filedata = readfile();

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
