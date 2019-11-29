class MyException(Exception):
    def __init__(self, args):
        self.args=args
    def __str__(self, args):
        print(args)

a=int(input())
b=int(input())
       
def xyz(a,b):
    return (a+b)

if(xyz(a,b)<150):
        raise MyException("Custom Exception Occurred")
else:
    print(a+b)


