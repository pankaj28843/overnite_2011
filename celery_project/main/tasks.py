from celery.decorators import task
@task
def submit(name,  program, input_file, output_file):
    result = program
    return result
