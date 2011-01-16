from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from main.models import *
from settings import MEDIA_URL, MAX_SUBMISSIONS
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response('main/index.html',context_instance=RequestContext(request))

def credits(request):
    return render_to_response('main/credits.html',context_instance=RequestContext(request))

@login_required
def contest_index(request):
    problem_list = []
    if not request.user.is_active:
        request.user = testuser
    user = request.user
    if request.user.is_superuser:
        problems = Problem.objects.all()
    else:
        problems = Problem.objects.filter(is_public=True)
    for problem in problems:
        problem.is_solved = problem.solved(user)
        problem_list.append(problem)

    if request.user.is_superuser:
        submissions = Submission.objects.filter(is_latest=True).order_by('-time')[:10] 
    else:
        submissions = Submission.objects.filter(is_latest=True, problem__is_public=True).order_by('-time')[:10] 
    return render_to_response('main/contest_index.html', {
        'problems': problem_list,
        'submissions':submissions,        
        'total_marks': get_total_marks(user),
    },context_instance=RequestContext(request))

@login_required
def problem_detail(request, problem_id):
    if request.user.is_superuser:
        problem = get_object_or_404(Problem, pk=problem_id)
    else:
        problem = get_object_or_404(Problem, pk=problem_id, is_public=True)
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

    left_submissions = MAX_SUBMISSIONS - last_submission.attempts()  if last_submission else MAX_SUBMISSIONS
    submission_limit_reached = left_submissions <= 0
    
    return render_to_response('main/problem_detail.html', {
        'problem': problem,
        'public_testcases':public_testcases,
        'form': form,
        'left_submissions':left_submissions,
        'total_marks': get_total_marks(user),
        'submission_limit_reached':submission_limit_reached,        
        'media_prefix':MEDIA_URL,
        'last_submission':last_submission,},
        context_instance=RequestContext(request))
   
@login_required
def problem_input(request, problem_id, testcase_id):
    testcase = get_object_or_404(TestCase, pk=testcase_id)
    if testcase.is_public:
        return HttpResponse(testcase.input_file.read(),mimetype="text/in")
    else:
        raise Http404

@login_required
def problem_output(request, problem_id, testcase_id):
    testcase = get_object_or_404(TestCase, pk=testcase_id)
    if testcase.is_public:
        return HttpResponse(testcase.output_file.read(),mimetype="text/out")
    else:
        raise Http404
       
       
def reg_team(request, team_id, team_name, password, email):
    if request.GET.get('pass', False) == "paswrd":
        user = User(username=team_id, first_name=team_name)
        user.set_password(password)
        user.save()
        user.email = email
        user.save()
        return HttpResponse()        
    else:
        raise Http404  
    
