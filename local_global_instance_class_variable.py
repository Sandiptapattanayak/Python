x=10
class Test:
  x=5
  def __init__(self):
    self.x=4
  def show(self):
    x=6
    print("local variable",x)
    print("global variable=",globals()['x'])
    print("Class variable=",Test.x)
    print("Instance variable",self.x)
    print(globals()['x'],Test.x,self.x,x) 
t=Test()
t1=Test()
t2=Test()
t.show()
t1.show()
