class classDemo(object):
    x = 1000
    nm = ''
    def __init__(self):
       print("const")
       self.x = 1000
    def __init__(self,name):
       self.name = name
    def __del__(self):
      print("dest")

print("test.x=>",id(classDemo.x))
t1 = classDemo()
print("t1.x=>",id(t1.x))
t2 = classDemo()
print("t2.x=>",id(t2.x))

t1.x = 1059
print("t1.x updated=>",id(t1.x))


t3 = classDemo("kunal")

print("t3.__init__()=>",t3.nm)
