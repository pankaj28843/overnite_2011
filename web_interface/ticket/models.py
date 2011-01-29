from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User)
    query = models.TextField("Your Query")
    solved = models.BooleanField("Solved", default=False)
    time = models.DateTimeField(auto_now_add = True)
    
    def answered(self):
        return True if self.answer_set.count() else False
    def __unicode__(self):
        return self.query
    
class Answer(models.Model):
    user = models.ForeignKey(User)
    ticket = models.ForeignKey(Ticket)
    answer = models.TextField("Reply")
    time = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.answer
    