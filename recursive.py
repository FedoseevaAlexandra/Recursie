a=int(input('dati a='))
b=int(input('dati b='))
def putere(x,y):
    s=1
    for i in range(y):
        s*=x
    return s
print(a,'**',b,'=',putere(a,b))
