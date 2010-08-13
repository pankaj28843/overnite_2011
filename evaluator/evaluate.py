#!/usr/bin/python

import os
import re
import timechecker

result=dict() #stores the result
testresult=list()
exectime=list()
response=dict()

def checkOutput(givenpath,samplepath):

  #opening a given file and a sample file
  givenfile=open(givenpath,'r')
  samplefile=open(samplepath,'r') 

  #reading firstline
  s1=samplefile.readline()
  s2=givenfile.readline()

  match_flag=1

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
       match_flag=0
       break

    #break if any file reaches the end
    elif((s1=='')or(s2=='')):
       break

    #read next line
    else:
       s1=samplefile.readline()
       s2=givenfile.readline()


  
  if(match_flag!=0):     
      #skipping blank lines at the end of file
      if(s1!=''):
          s1=samplefile.readline()
          x1=s1.split()
          while((len(x1)<1)and(s1!='')):
            s1=samplefile.readline()
            x1=s1.split() 
  
      if(s2!=''):
          s2=givenfile.readline()
          x2=s2.split()
          while((len(x1)<1)and(s1!='')):
            s2=samplefile.readline()
            x2=s2.split()

  #if both files a read successfully
  if((s1=='')and(s2=='')):
    testresult.append('correct')
  
  else:
    testresult.append('incorrect')


p=re.compile('\s*(#)(\s*)(include)(.*)')
comment=re.compile('(\s*)(//)')
q=re.compile('(\s*)(system)|(\s*)(srand)|(\s*)(popen)') #q r.e. compiles the system call tokens

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

    if(comment.match(s)==None and q.search(s)!=None): # If sytem call found, execution aborted.
      return 'true'
    s=cfile.readline()

  #closing the two files
  cfile.close()
  tempfile.close()



def checkcodeCPP(sourcepath):

  # opening the C++ file for reading
  cppfile=open(sourcepath,'r')

  # opening a temporary file for writing
  tempfile=open('files/temp/temp.cpp','w')

  #writing all required headers at the top
  tempfile.write("#include<cstdio>\n")
  tempfile.write("#include<cstdlib>\n")
  tempfile.write("#include<cmath>\n")
  tempfile.write("#include<cstring>\n")
  tempfile.write("#include<vector>\n")
  tempfile.write("#include<iostream>\n")
  tempfile.write("#include<string>\n")
  tempfile.write("#include<sstream>\n")
  tempfile.write("#include<complex>\n")

  #reading the C file line by line
  s=cppfile.readline()
  while(s!=''):

    #writing the line in the temp file, if its not a header
    if(p.match(s)==None):
      tempfile.write(s)

    if(comment.match(s)==None and q.search(s)!=None): # If sytem call found, execution aborted.
      return 'true'
    s=cppfile.readline()

  #closing the two files
  cppfile.close()
  tempfile.close()


p1=re.compile('\s*(import)(.*)')
def checkcodeJava(sourcepath):

  # opening the C file for reading
  javafile=open(sourcepath,'r')

  # opening a temporary file for writing
  tempfile=open('temp.java','w')

  #writing all required headers at the top
  tempfile.write("import java.lang.*;\n")
  tempfile.write("import java.util.*;\n")

  #reading the C file line by line
  s=javafile.readline()
  while(s!=''):

    #writing the line in the temp file, if its not a header
    if(p1.match(s)==None):
      tempfile.write(s)

    if(comment.match(s)==None and q.search(s)!=None): # If sytem call found, execution aborted.
      return 'true'
    s=javafile.readline()

  #closing the two files
  javafile.close()
  tempfile.close()


def evaluateC(sourcepath,testlist,timelimit):

  if(not(os.path.exists('files/temp'))):
        os.system('mkdir files/temp')
  os.system('rm files/temp/*')

  if(checkcodeC(sourcepath)=='true'):
        result['status']='Malicious code'
        result['executiontime']=-1
        return

  os.system('chmod 777 files/temp/temp.c') #granting all permissions to the temp
  os.system('gcc -std=c99 -o files/temp/a.out files/temp/temp.c') # compiling the C code


  #creating output file and comparing with the sample if a.out is generated
  if(os.path.exists('files/temp/a.out')):

     for i in testlist:
       inputpath=i['input']
       outputpath=i['output']
       runcmd='./files/temp/./a.out <' + inputpath + '> files/temp/output.out'
       response=timechecker.execute(runcmd,timelimit)
       
       # response={'status':'ok/runtime exceeded/runtime error','executiontime':'time/-1'}
       if (response['run_status']=="ok"):
           checkOutput('files/temp/output.out',outputpath)
           exectime.append(response['runtime'])
       else:
           testresult.append(response['run_status'])
           exectime.append(response['runtime'])
      
     
     result['status']=testresult
     result['executiontime']=exectime

  #status=error is a.out is not generated
  else:
     result['status']='errors'
     result['executiontime']=-1



def evaluateCPP(sourcepath,testlist,timelimit):

  if(not(os.path.exists('files/temp'))):
        os.system('mkdir files/temp')
  os.system('rm files/temp/*')

  if(checkcodeCPP(sourcepath)=='true'):
        result['status']='Malicious code'
        result['executiontime']=-1
        return

  os.system('chmod 777 files/temp/temp.cpp') #granting all permissions to the temp
  os.system('g++ -o files/temp/a.out files/temp/temp.cpp') # compiling the C++ code


  #creating output file and comparing with the sample if a.out is generated
  if(os.path.exists('files/temp/a.out')):

     for i in testlist:
       inputpath=i['input']
       outputpath=i['output']
       runcmd='./files/temp/./a.out <' + inputpath + '> files/temp/output.out'
       response=timechecker.execute(runcmd,timelimit)
       
       # response={'status':'ok/runtime exceeded/runtime error','executiontime':'time/-1'}
       if (response['run_status']=="ok"):
           checkOutput('files/temp/output.out',outputpath)
           exectime.append(response['runtime'])
       else:
           testresult.append(response['run_status'])
           exectime.append(response['runtime'])
      
     
     result['status']=testresult
     result['executiontime']=exectime

  #status=error is a.out is not generated
  else:
     result['status']='errors'
     result['executiontime']=-1

def evaluateJava(sourcepath,testlist,timelimit):

  if(not(os.path.exists('files/temp'))):
        os.system('mkdir files/temp')
  os.system('rm files/temp/*')
  os.system('rm *.class')
  os.system('rm *.java')

  if(checkcodeJava(sourcepath)=='true'):
        result['status']='Malicious code'
        result['executiontime']=-1
        return

  source=sourcepath.split("/")
  filename=source[len(source)-1]
  classname=filename.split(".")[0]

  os.system('chmod 777 temp.java') #granting all permissions to the temp
  os.system('javac temp.java') # compiling the java code


  #creating output file and comparing with the sample if a.out is generated
  if(os.path.exists('./'+classname+'.class')):

     for i in testlist:
       inputpath=i['input']
       outputpath=i['output']
       runcmd='java '+classname+' < ' + inputpath + ' > files/temp/output.out'
       print runcmd
       response=timechecker.execute(runcmd,timelimit)
       
       # response={'status':'ok/runtime exceeded/runtime error','executiontime':'time/-1'}
       if (response['run_status']=="ok"):
           checkOutput('files/temp/output.out',outputpath)
           exectime.append(response['runtime'])
       else:
           testresult.append(response['run_status'])
           exectime.append(response['runtime'])
      
     
     result['status']=testresult
     result['executiontime']=exectime

  #status=error is a.out is not generated
  else:
     result['status']='errors'
     result['executiontime']=-1

  



def evaluate(language,sourcepath,testlist,timelimit): # testlist is a list of test dictionaries : {'input':'inputpath','output':'outputpath'}
  if(language=='C'):
    evaluateC(sourcepath,testlist,timelimit)
  if(language=='C++'):
    evaluateCPP(sourcepath,testlist,timelimit)
  if(language=='Java'):
    evaluateJava(sourcepath,testlist,timelimit)
  return result;


if __name__=='__main__':
  test=[{'input':'input/sort.in','output':'output/sort.out'},{'input':'input/sort2.in','output':'output/sort2.out'}]
  res=evaluate('Java','javacodes/sort.java',test,1)
  print result
