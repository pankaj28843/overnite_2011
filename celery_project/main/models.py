from django.db import models
from django.forms import ModelForm
from django import forms

class Submission(models.Model):
    submission = models.FileField(upload_to = 'files') 
    time = models.DateTimeField('Time', auto_now_add=True)
    result = models.TextField('Result', blank=True)

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ('submission',)

