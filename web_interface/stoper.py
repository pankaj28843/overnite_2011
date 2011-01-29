import time
import datetime
from main.models import *

problem_set = Problem.objects.all()
def stop():
    while 1:
        time.sleep(5)
        now = datetime.datetime.now
        print now().hour
        if now().hour == 22:
            for p in problem_set:
                p.is_public = False

            
        
    
