from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from main.models import Problem, SubmissionForm, Submission, TestCase
from settings import MEDIA_URL
from django.contrib.auth.models import User
from django.template import RequestContext

def home(request):
    return render_to_response('main/index.html',context_instance=RequestContext(request))

def about(request):
    return render_to_response('main/about.html',context_instance=RequestContext(request))

def contest_index(request):
    problems = Problem.objects.all()
    submissions = Submission.objects.filter(is_latest=True).order_by('-time')[:10] 
    return render_to_response('main/contest_index.html', {
        'problems': problems,
        'submissions':submissions,
    },context_instance=RequestContext(request))

def problem_detail(request, problem_id):
    testuser = get_object_or_404(User, username = 'test')
    if not request.user.is_active:
        request.user = testuser
    problem = get_object_or_404(Problem, pk=problem_id)
    public_testcases = problem.testcase_set.filter(is_public=True)
    user = request.user
    last_submission = []
    user_submissions = Submission.objects.filter(user = user, problem = problem).order_by('-time')
    if user_submissions:
        last_submission  = user_submissions[0]
         
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        #Saving the form if it is valid
        if form.is_valid():
            new_submission = form.save(commit=False)
            #Calling the worker to perform the task submit through celery
            new_submission.save(user = user, problem = problem)            
            #Redirect to the results of the submission
            return HttpResponseRedirect(problem.get_absolute_url())
    else:
        #New form for a submission                             
        form = SubmissionForm()
    return render_to_response('main/problem_detail.html', {
        'problem': problem,
        'public_testcases':public_testcases,
        'form': form,
        'media_prefix':MEDIA_URL,
        'last_submission':last_submission,},
        context_instance=RequestContext(request))
   

def problem_input(request, problem_id, testcase_id):
    testcase = get_object_or_404(TestCase, pk=testcase_id)
    if testcase.is_public:
        return HttpResponse(testcase.input_file.read(),mimetype="text/in")
    else:
        raise Http404
    
def test():
    import django
    
    return None