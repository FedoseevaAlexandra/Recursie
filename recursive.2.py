a=int(input('dati a='))
b=int(input('dati b='))
def putere(x,y):
    if (y>0):
      return x*putere(x,y-1)
    if y==0:
        return 1
print(a,'**',b,'=',putere(a,b))
