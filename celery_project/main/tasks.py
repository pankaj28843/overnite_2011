from celery.decorators import task
@task
def submit(submission):
    upfile = "http://10.106.6.108:8000/media/" + str(submission.submission)
    submission.result = upfile
    submission.save()
    return submission.result
