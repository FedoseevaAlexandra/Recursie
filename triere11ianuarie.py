Volum=int(input('volum max = '))
n=int(input('dati nr de obiecte = '))
volume=[]
preturi=[]
pret_max=0
for i in range(n):
    volume.append(int(input('volumul obiectului = ')))
    preturi.append(int(input('pretul obiectului = ')))
def Sol_Pos(a,b,c,d,e):    
    if volume[a]<=Volum and volume[b]<=Volum and volume[c]<=Volum and volume[d]<=Volum and volume[e]<=Volum and(volume[0]*a+volume[1]*b+volume[2]*c+volume[3]*d+volume[4]*e<=Volum) :
        return True
    else:
        return False

def Prel_Sol(a,b,c,d,e):
    x=[0,0,0,0,0]
    global pret_max
    pret=preturi[0]*a+preturi[1]*b+preturi[2]*c+preturi[3]*d+preturi[4]*e
    if pret>pret_max:
        pret_max=pret
        x=[a,b,c,d,e]
    return x

for a in range (2): 
    for b in range (2):
        for c in range (2):
            for d in range (2):
                for e in range (2):                  
                  if (Sol_Pos(a,b,c,d,e)):                        
                     x=Prel_Sol(a,b,c,d,e)

for i in range(5):
    if x[i]>0:
        print('- obiectul ',i,'(', volume[i], ',',  preturi[i], ')')