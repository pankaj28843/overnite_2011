#!/usr/bin/python

import os
import re


result=dict()       #stores the result
testresult=list()
exectime=list()

def checkOutput(givenpath,samplepath):

  #opening a given file and a sample file
  givenfile=open(givenpath,'r')
  samplefile=open(samplepath,'r') 

  #reading firstline
  s1=samplefile.readline()
  s2=givenfile.readline()

  while((s1!='')and(s2!='')):        #condition for end of file

    #splitting to omit white space
    x1=s1.split()                   
    x2=s2.split()

    #skipping blank lines 
    while((len(x1)<1)and(s1!='')):
       s1=samplefile.readline()
       x1=s1.split()
    while((len(x2)<1)and(s2!='')):
       s2=samplefile.readline()
       x2=s1.split()
    
    #break in case of mismatch
    if(x1!=x2):
       break

    #break if any file reaches the end
    elif((s1=='')or(s2=='')):
       break

    #read next line
    else:
       s1=samplefile.readline()
       s2=givenfile.readline()


  #if both files a read successfully
  if((s1=='')and(s2=='')):
       testresult.append('correct')
  
  #if both files are not read successfully
  else:
       testresult.append('incorrect')



p=re.compile('\s*(#)(\s*)(include)(.*)')
comment=re.compile('(\s*)(//)')
q=re.compile('(\s*)(system)|(\s*)(popen)')		#q r.e. compiles the system call tokens
def checkcodeC(sourcepath):

  # opening the C file for reading
  cfile=open(sourcepath,'r')  

  # opening a temporary file for writing
  tempfile=open('files/temp/temp.c','w')

  #writing all required headers at the top
  tempfile.write("#include<stdio.h>\n")
  tempfile.write("#include<stdlib.h>\n")
  tempfile.write("#include<math.h>\n")
  tempfile.write("#include<string.h>\n")

  #reading the C file line by line
  s=cfile.readline()
  while(s!=''):

    #writing the line in the temp file, if its not a header
    if(p.match(s)==None):
      tempfile.write(s)

   # if(comment.match(s)==None and q.search(s)!=None):	# If sytem call found, execution aborted.
    #  return 'true'
    s=cfile.readline()

  #closing the two files
  cfile.close()
  tempfile.close()


 
    
     

def evaluateC(sourcepath,testlist,timelimit):


  if(not(os.path.exists('files/temp'))):
        os.system('mkdir files/temp')
  os.system('rm files/temp/*')  

  if(checkcodeC(sourcepath)=='true'):
	result['status']='Malicious code'
        result['executiontime']=-1
	return	

  os.system('chmod 777 files/temp/temp.c')                 #granting all permissions to the temp 
  os.system('cc -o files/temp/a.out files/temp/temp.c')    # compiling the C code


  #creating output file and comparing with the sample if a.out is generated
  if(os.path.exists('files/temp/a.out')):
     for i in testlist:
       inputpath=i['input']
       outputpath=i['output']
       runcmd='./a.out <' + inputpath +  '> files/temp/output.out'
       response=runfile(runcmd,timelimit)
       # response={'status':'ok/timeexceeded/runtimeerror','executiontime':'time/-1'}
       if(response['status']=='ok'):
         checkOutput('files/temp/output.out',outputpath)
         exectime.append(response['executiontime']) 
     result['status']=testresult
     result['executiontime']=exectime

  #status=error is a.out is not generated
  else:
     result['status']='errors'
     result['executiontime']=-1



def evaluate(language,sourcepath,testlist,timelimit):     # testlist is a list  of test dictionaries : {'input':'inputpath','output':'outputpath'}
  if(language=='C'):
    evaluateC(sourcepath,testlist,timelimit)
  return result;


if __name__=='__main__':
  test=[{'input':'input/sort.in','output':'output/sort.out'},{'input':'input/sort2.in','output':'output/sort2.out'}]
  print evaluate('C','ccodes/sort.c',test,10)
