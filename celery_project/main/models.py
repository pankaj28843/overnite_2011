from django.db import models
from django.forms import ModelForm
from django import forms
from picklefield import PickledObjectField

class Submission(models.Model):
    name = models.CharField('Name', max_length = 100)
    program = models.FileField('Program', upload_to = 'files')
    input_file = models.FileField('Input File', upload_to = 'files')
    output_file = models.FileField('Output File', upload_to = 'files')
    time = models.DateTimeField('Time', auto_now_add=True)
    celery_task = PickledObjectField()

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        exclude = ('celery_task',)
