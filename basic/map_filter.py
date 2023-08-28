x = [1,5,1,8,2,8,1,22,96,41,36,30]

mp = map(lambda i:i+2,x)
print(list(mp))

flt = filter(lambda n:n*2 == 4,x)
print(list(flt))