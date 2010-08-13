from celery.decorators import task
from django.core.files.temp import NamedTemporaryFile
from evaluator import evaluate
from settings import ROOT_PATH  #Directory of manage.py
'''
Returns the absolute path of the file
'''
def get_path(f):
    return str(ROOT_PATH)+'/'+f.name

'''
A djcelry task defined throudh @task decorator.
This supplies the info to evaluator and fetches the result of the compilation
and execution of the code.
'''
@task
def submit(name, language,program, tests):
##
    n = len(tests)
    testlist = []
    timelimit = 15
    program_file = file('files/program.'+language, 'w+b')    #Temp. File for the program
    program_file.write(program)
    for i in range(n):
        input_file = file('files/input_file-%d.in' %(i+1), 'w+b')
        output_file = file('files/output_file-%d.out' %(i+1), 'w+b')
        input_file.write(tests[i]['input'])                                            #Writing data from the list of input/output files supplied
        output_file.write(tests[i]['output'])                                          #to temp files and
        testlist.append({'input':get_path(input_file),'output':get_path(output_file)})    #Getting their path to be supplied to evaluator.
        input_file.close()
        output_file.close()
    program_file.close()
    result =  evaluate.evaluate('C',get_path(program_file), testlist, timelimit)
    return result
