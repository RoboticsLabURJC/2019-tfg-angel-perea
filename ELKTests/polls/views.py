from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Session, Simulation
from .documents import SessionDocument, SimulationDocument
from datetime import datetime

class IndexView(generic.ListView):
    print("SESSION")
    NSES = SessionDocument.search().filter("term", type=1)

    NSES = SessionDocument.search().query("match", type=1)
    for hit in NSES:
        print(hit)
    print("SIMULATION")
    NSIM = SimulationDocument.search().filter("term", type=3)

    NSIM = SimulationDocument.search().query("match", type=3)
    for hit in NSIM:
        print(hit)

    '''
    s = CarDocument.search().filter("term", color="red")
    # or
    s = CarDocument.search().query("match", description="beautiful")

    for hit in s:
        print(
            "Car name : {}, description {}".format(hit.name, hit.description)
        )
    print("SECOND")
    s = CarDocument.search().filter("term", color="blue")[:30]
    qs = s.to_queryset()
    # qs is just a django queryset and it is called with order_by to keep
    # the same order as the elasticsearch result.
    for car in qs:
        print(car.name)
    '''
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    print("ADDING SESSION")
    Session(
        type = 1,
        date = datetime.now(),
        username = 'testUsername',
        client_ip = '127.0.0.1',
        user_agent = 'testUserAgent'
    ).save()
    ############DONE
    Session(
        type = 2,
        date = datetime.now(),
        username = 'testUsername',
        client_ip = '127.0.0.1',
        user_agent = 'testUserAgent'
    ).save()
    print("ADDING SIMULATION")
    ############DONE
    Simulation(
        type = 3,
        date = datetime.now(),
        username = 'testUsername',
        client_ip = '127.0.0.1',
        simulation_type = 'testSimulationType',
        exercise_id = 'testExerciseID',
        host_ip = '127.0.0.2',
        container_id = 'testContainerID',
        user_agent = 'testUserAgent'
    ).save()
    Simulation(
        type = 4,
        date = datetime.now(),
        username = 'testUsername',
        client_ip = '127.0.0.1',
        simulation_type = 'testSimulationType',
        exercise_id = 'testExerciseID',
        host_ip = '127.0.0.2',
        container_id = 'testContainerID',
        user_agent = 'testUserAgent'
    ).save()
    '''
    print("DETAIL")
    car = Car(
        name="Car one",
        color="red",
        type=1,
        description="A beautiful car"
    )
    print(car)
    car.save()
    '''
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))








        s
