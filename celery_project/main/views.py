from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from main.models import *
from main import tasks

def home(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        #Saving the form if it is valid
        if form.is_valid():
            new_submission = form.save()
            problem = new_submission.problem
            tests = []
            #Reading Text from the inputoutput fields of the problem and appending them to the tests list.
            for in_out in problem.inputoutput_set.all():
                tests.append({'input':in_out.input_file.read(), 'output':in_out.output_file.read()})
            #Calling the worker to perform the task submit through celery
            new_submission.celery_task = tasks.submit.apply_async(args = [new_submission.problem, new_submission.language, new_submission.program.read(),tests])
            new_submission.save()
            #Redirect to the results of the submission
            return HttpResponseRedirect(new_submission.get_absolute_url())                             
        #If the form is invalid it is re-rendered with the errors.
    else:
        #New form for a submission                             
        form = SubmissionForm()
    return render_to_response('main/home.html', {
        'form': form,
    })

def result(request, sub_id):
    submission = get_object_or_404(Submission, pk = sub_id)
    return render_to_response('main/result.html', {
        'submission': submission,
    })
