from django.db import models
from django import forms
from picklefield import PickledObjectField
from django.contrib.auth.models import User
from django.forms import HiddenInput
from main.tasks import submit, SubmitTask
from django.core.files.storage import FileSystemStorage
import settings, os, datetime
STORAGE_PATH = os.path.join(settings.ROOT_PATH, 'files')
fs = FileSystemStorage(location=STORAGE_PATH)
#The programming problem
class Problem(models.Model):
    title = models.CharField('Title', max_length = 100)
    question = models.TextField('Question')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/contest/problem/%d/' %(self.id)
    def no_of_test_cases(self):
        return self.testcase_set.count()
    def status(self):
        submissions = self.submission_set.filter(is_latest=True)
        latest_submissions = submissions.filter(is_latest=True).order_by('-time')
        successful_submissions = 0
        success_rate = 0
        total_submissions = submissions.count()
        for submission in submissions:
            if submission.ready() and submission.correct():
                successful_submissions+=1        
        if total_submissions:
            success_rate = int(100.0*successful_submissions/total_submissions)
        return {'total_submissions':total_submissions, 'successful_submissions':successful_submissions, 'success_rate': success_rate, 'latest_submissions': latest_submissions[:10]}            
    def total_marks(self):
        marks = 0
        for case in self.testcase_set.all():
            marks += case.marks
        return marks
#Input Output file for problem
class TestCase(models.Model):   
    problem = models.ForeignKey(Problem)
    input_file = models.FileField('Input File', upload_to = 'inputs', storage=fs)
    output_file = models.FileField('Output File', upload_to = 'outputs', storage=fs)
    time_limit = models.FloatField('Time Limit (Seconds)', default = 1)
    is_public = models.BooleanField('Is Public', default = False)
    marks = models.IntegerField('Marks', default = 10)
    def __unicode__(self):
        return self.problem.title + ': Input/Output'
    def input_url(self):
        return '/contest/problem/%d/input/%d/testinput.in' %(self.problem.id, self.id)
    def output_url(self):
        return '/contest/problem/%d/output/%d/testoutput.out' %(self.problem.id, self.id)
    def weightage(self):
        weight = (float(self.marks)/float(self.problem.total_marks()))*100
        return str("%.2f"%(weight)+ " %")
    
#The submissions from a user are defined here
class Submission(models.Model):
    LANGUAGES = (
        ('c', 'C'),
        ('c++', 'C++'),
        ('java', 'Java'),
    )
    user = models.ForeignKey(User)     
    language = models.CharField('Language', max_length = 10, choices=LANGUAGES)
    program = models.FileField('Code', upload_to = 'programs', storage=fs)
    problem = models.ForeignKey(Problem)
    filename = models.CharField('Filename', max_length = 50)
    time = models.DateTimeField('Time', auto_now_add=True)
    is_latest = models.BooleanField('Latest', default = True)
    celery_task = PickledObjectField()  #This saves the result of the celery_task, It gives the key to access the celery task database.
    class Meta:
        ordering = ['-time'] 
        get_latest_by = 'time'
    def __unicode__(self):
        return self.problem.title + ' by ' + str(self.user) + ', File: ' + str(self.program)
    #Get the current status of the process
    def attempts(self):
        total_attempts = Submission.objects.filter(user = self.user, problem = self.problem).count()
        return total_attempts 
    def correct(self):
        return True if self.result()['successful'] else False
    def delete(self,*args, **kwargs ):
        old_submissions = Submission.objects.exclude(pk=self.id).filter(user = self.user, problem = self.problem)
        self.set_latest(old_submissions)
        super(Submission, self).delete(*args, **kwargs)
    def day_diff(self):
        days = (datetime.datetime.now()-self.time).days
        return days
    def result(self):
        return self.celery_task.result
    def ready(self):
        return self.celery_task.ready()
    def status(self):
        if self.ready():
            return 'Correct' if self.correct() else 'Wrong'
        else:
            return 'Processing'
    def save(self,user=None,problem=None,*args, **kwargs):
        if not self.celery_task:
            if user:
                self.user = user
            if problem: 
                self.problem = problem 
            self.filename = str(self.program)
            self.celery_task = SubmitTask.apply_async(args = self.task_detail())
            self.update_old_submissions()
        super(Submission, self).save(*args, **kwargs)
    
    def set_latest(self, submissions):
        latest_submission = submissions.latest()
        latest_submission.is_latest = True
        latest_submission.save()
        print latest_submission, latest_submission.is_latest
        return latest_submission
    
    def update_old_submissions(self):
        old_submissions = Submission.objects.filter(is_latest =True, user = self.user, problem = self.problem)
        for submission in old_submissions:
            submission.is_latest=False
            submission.save()
                
    def task_status(self):
        ready = self.celery_task.ready()
        if ready:
            return 'Processed'
        else:
            return 'In Queue'
    def task_detail(self):                
        tests = []
        time_limit = None
        for case in self.problem.testcase_set.all():            
            time_limit = max(timelimit, case.time_limit) if time_limit else case.time_limit
            tests.append({'input':case.input_file.read(), 'output':case.output_file.read(), 'time_limit':case.time_limit, 'marks': case.marks})
        return [self.problem, self.language, self.program.read(),self.filename,tests, time_limit]

#Form for a submission to be made by the user
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['language','program']
        filename = forms.CharField(widget=HiddenInput())
        
