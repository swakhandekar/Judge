import sys
import os,time
from sandbox import *
 
def sand(program_path, input_path,i,file_description):

    
    f_wr = os.open(str(i)+".out",os.O_TRUNC|os.O_RDWR|os.O_CREAT)
    
    cookbook = {
        'args': program_path,                               # targeted program
        'stdin': open(input_path, "r"),                     # input to targeted program
        'stdout': f_wr,                                     # output from targeted program
        'quota': dict(wallclock=int(file_description[1])+1,   # Time limit for infinite loop
                      cpu=int(file_description[1]),         # Time limit for the program
                      memory=(268435456),      # RAM size allocated for the program
                      disk=1978098813
                      )
                }       

    s = Sandbox(**cookbook)
    s.run()
    
    output = os.fdopen(f_wr)
    output.seek(0)
    output_string = output.read()
    verdict = s.result
    return verdict
