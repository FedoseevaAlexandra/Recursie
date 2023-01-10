Volum=int(input('volum max = '))
n=int(input('dati nr de obiecte = '))
volume=[]
preturi=[]
x=[]
for i in range(n):
    volume.append(int(input('volumul obiectului = ')))
    preturi.append(int(input('pretul obiectului = ')))
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
for i in range(1,n):
    if x[i]>0:
        print('- obiectul ',i,'(', vol[i]* x[i], ',',  pr[i], ')')
#Se va considera că se poate introduce și o parte dintr-un obiect care nu încape în rucsac, până la ocuparea întregului volum al rucsacului. 