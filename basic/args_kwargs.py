def func(x,y):
    print(x,y)

pairs = [(1,2),(3,4)]
for pair in pairs:
    func(*pair)

def func2(*args,**kwargs):
    print(args,kwargs)

func2(1,2,3,4,5,one=1,two=2)
