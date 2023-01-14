Volum=250
n=5
volume=[120,40,40,100,150]
preturi=[150,80,60,120,180]
x=[]
raport=[]
for i in range(n):
   raport.append(preturi[i]/volume[i])
print(raport)
raport_sortat=sorted(raport,reverse=True)
vol=[]
pr=[]
for i in range(n):
    vol.append(volume[raport.index(raport_sortat[i])])
    pr.append(preturi[raport.index(raport_sortat[i])])
    x.append(0)
print(vol,pr)

def solutii():
  global Volum, n, vol, pr
  vt = pt = 0
  i=0
  while (vt<Volum) and (i<len(vol)):
    if (vt + vol[i] )<=Volum :
        x[i]=1
        pt=pt+pr[i]
        vt=vt+vol[i]
    i+=1
  return print('Pretul total al obiectelor din rucsac=', pt,   'Volumul ocupat=', vt)
solutii()
print('In rucsac s-au introdus:')
for i in range(5):
    if x[i]>0:
        print('- obiectul ',i+1,'(', vol[i]* x[i], ',',  pr[i], ')')
