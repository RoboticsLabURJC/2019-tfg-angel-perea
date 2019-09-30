import os
import random

#os.system("cd /home/angel/TFG/prototype");
#os.system("ls -lish");
#os.system("python3 manage.py shell");
#os.system("from prototypePolls import Choice, Question");

from prototypePolls.models import Choice, Question
from django.utils import timezone

i=0
while(i != 10):
    q = Question(question_text="Test"+str(i)+"?", pub_date=timezone.now())
    q.save()
    votesFirst = random.randint(0,999);
    q.choice_set.create(choice_text='Yes', votes=votesFirst)
    votesSecond = random.randint(0,999);
    q.choice_set.create(choice_text='No', votes=votesSecond)
    i+=1
