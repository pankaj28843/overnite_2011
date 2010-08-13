from django.db import models
from django.forms import ModelForm
from django import forms
from picklefield import PickledObjectField
from django.contrib.auth.models import User
#The programming problem
class Problem(models.Model):
    title = models.CharField('Title', max_length = 100)
    question = models.TextField('Question')
    def __unicode__(self):
        return self.title
    def total_marks(self):
        marks = 0
        for case in self.testcase_set.all():
            marks += case.marks
        return marks
    
#Input Output file for problem
class TestCase(models.Model):
    problem = models.ForeignKey(Problem)
    input_file = models.FileField('Input File', upload_to = 'files/inputs')
    output_file = models.FileField('Output File', upload_to = 'files/outputs')
    marks = models.IntegerField('Marks')
    def __unicode__(self):
        return self.problem.title + ': Input/Output'
    def weightage(self):
        weight = (float(self.marks)/float(self.problem.total_marks()))*100
        return str("%.2f"%(weight)+ " %")
    
#The submissions from a user are defined here
class Submission(models.Model):
    LANGUAGES = (
        ('c', 'C'),
        ('java', 'Java'),
    )
    user = models.ForeignKey(User)     
    language = models.CharField('Language', max_length = 10, choices=LANGUAGES)
    program = models.FileField('Program', upload_to = 'files/programs')
    problem = models.ForeignKey(Problem)
    time = models.DateTimeField('Time', auto_now_add=True)
    celery_task = PickledObjectField()  #This saves the result of the celery_task, It gives the key to access the celery task database.
    def get_absolute_url(self):
        return '/submission/%d/' %(self.id)
    def __unicode__(self):
        return 'Submission: ' + self.problem.title# + 'by ' + self.user
    #Get the current status of the process
    def status(self):
        ready = self.celery_task.ready()
        if ready:
            return 'Processed'
        else:
            return 'In Queue'
    def result(self):
        return str(self.celery_task.result)

#Form for a submission to be made by the user
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        exclude = ('celery_task','user')