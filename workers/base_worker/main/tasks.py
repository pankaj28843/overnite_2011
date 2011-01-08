from celery.decorators import task
from celery.task import Task
from django.core.files.temp import NamedTemporaryFile
from evaluator import evaluate
from settings import ROOT_PATH  #Directory of manage.py
'''
Returns the absolute path of the file
'''
def get_path(f):
    return str(ROOT_PATH)+'/'+f.name

def submit(name, language,program,filename, tests, time_limit):
    n = len(tests)
    testlist = []
    program_file = file('files/temp/programs/'+filename, 'w+b')    #Temp. File for the program    
    program_file.write(program)
    for i in range(n):
        input_file = file('files/temp/inputs/input_file-%d.in' %(i+1), 'w+b')
        output_file = file('files/temp/outputs/output_file-%d.out' %(i+1), 'w+b')
        input_file.write(tests[i]['input'])                                            #Writing data from the list of input/output files supplied
        output_file.write(tests[i]['output'])                                          #to temp files and
        testlist.append({'input':get_path(input_file),'output':get_path(output_file)})    #Getting their path to be supplied to evaluator.
        input_file.close()
        output_file.close()
    program_file.close()
    result =  evaluate.evaluate(language, get_path(program_file), testlist, time_limit)
    result['successful'] = True
    result['marks'] = 0
    for (i, case) in enumerate(result['status']):
        if case == 'correct':
            test = tests[i]            
            time_taken = result['executiontime'][i]
            result['marks'] += round(test['marks']*((test['time_limit'] - time_taken)/test['time_limit']))            
        else:            
            result['successful'] = False
        i+=1

    if not result['successful']:
        result['marks'] = 0
    return result

'''
A djcelry task.
This supplies the info to evaluator and fetches the result of the compilation
and execution of the code.
'''
class SubmitTask(Task):
    def run(self,name, language,program,filename, tests, time_limit):
        return submit(name, language,program,filename, tests, time_limit)
