import sys,os,shutil,glob
from sandy import sand
from subprocess import Popen, PIPE
import os
import comparator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

upload=BASE_DIR+"/Uploads/"
userfolder=BASE_DIR+"/Users/"
descr=BASE_DIR+"/Question/Description/"
inpath=BASE_DIR+"/Question/Input/"
outpath=BASE_DIR+"/Question/Output/"

def delall(userid):
      del1=glob.glob(userfolder+userid+"/*")
      for i in del1:
            os.remove(i)

def compile(extension,userid,filename):
      
      shutil.copy(upload+filename, userfolder+userid+"/" )
      os.chdir(userfolder+userid+"/")
      if extension=="c":
            a=os.system("gcc "+filename+" 2>stderr.txt") 
      else:
            a=os.system("g++ -std=c++11 "+filename+" 2>stderr.txt")
      if a!=0:
            return False
      else:
            return True
      
def call_box(exe_path,queno,user):
      description = open(descr+queno+"/1.txt","r")
      d = description.readlines()
      
      di = []
      for i in xrange(2):
            di.append(int(d[i].strip('\n')))

      array=[]
      for i in xrange(int(d[0].strip('\n'))):
            testinpath = inpath+queno+"/"+str(i)+".in"
            array.append(sand(exe_path,testinpath,i,di))
            
      return array
            

def judge(up_path):
      info=up_path.split('.')
      ext=info[-1]
      filename=os.path.split(up_path)
      info2=filename[1].split('_')
      userid=info2[0]
      queno=info2[1]

      ret=[]
      if compile(ext,userid,filename[1]):
            exe=userfolder+userid+"/a.out"
            if os.path.isfile(exe):
                  r=call_box(userfolder+userid+"/a.out",queno,userid)
                  score=0
                  count=0
                  for j in xrange(len(r)):
                        path2=userfolder+userid+"/"+str(j)+".out"
                        path1=outpath+queno+"/"+str(j)+".out"
                        if(r[j]==1 and os.path.isfile(path1) and os.path.isfile(path2)):
                              count+=1
                              if comparator.main(path1,path2):
                                    score+=1
                                    r[j]=100
                              else:
                                    r[j]=-100
                              
                  delall(userid)
                  ret.append(r)
                  ret.append(score)
                  return ret
            else:
                  delall(userid)
                  ret.append(-9)
                  return ret
      
      else:
            delall(userid)
            return -9
            
print judge(sys.argv[1])
