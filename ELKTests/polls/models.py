from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

#################ELASTICSEARCH##################
class Car(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])

#################TFG##################DONE
class Session(models.Model):
    type = models.IntegerField(choices=[
        (1, "New"),
        (2, "End"),
    ])
    date = models.DateField()
    username = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=200)


class Simulation(models.Model):
    type = models.IntegerField(choices=[
        (1, "New"),
        (2, "End"),
    ])
    date = models.DateField()
    username = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=200)
    simulation_type = models.CharField(max_length=200)
    exercise_id = models.CharField(max_length=200)
    host_ip = models.CharField(max_length=200)
    container_id = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=200)
