
# Create your models here.

import datetime

from django.db import models
#from django.utils import timezone

CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    priority = models.CharField(max_length=50,
                                choices=CHOICE,
                                null = True)
    duedate = models.DateField()
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title    

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
##    choice_text = models.CharField(max_length=200)
 #  votes = models.IntegerField(default=0)
 #   def __str__(self):
 #       return self.choice_text
