import os

def main(path1,path2):
      if os.path.isfile(path1) and os.path.isfile(path2):
            f1 = open(path1)
            f2 = open(path2)
            a = f1.read()
            a = a.strip('\n')
            b = f2.read()
            b = b.strip('\n')
            copypath = os.path.split(path2)
            actual = open(copypath[0]+"/actual.txt","a+r+w")
            expected = open(copypath[0]+"/expected.txt","a+r+w")
            actual.write(b)
            expected.write(a)
            
            actual.seek(0)
            expected.seek(0)
            f1.close()
            f2.close()
            
            comp1 = expected.readlines()
            comp2 = actual.readlines()
            if(len(comp1) != len(comp2)):
                  actual.close()
                  expected.close()
                  os.remove(copypath[0]+"/actual.txt")
                  os.remove(copypath[0]+"/expected.txt")
                  return False

            s = False
            for i in xrange(len(comp1)):
                  if comp2[i].strip() == comp1[i].strip():
                        s = True
                  else:
                        s = False
                        break           
                        
            actual.close()
            expected.close()
            os.remove(copypath[0]+"/actual.txt")
            os.remove(copypath[0]+"/expected.txt")
            return s
      else:
            return False