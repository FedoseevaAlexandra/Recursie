Volum=250
n=5
volume=[120,40,40,100,150]
preturi=[150,80,60,120,180]
pret_max=0
def Sol_Pos(a,b,c,d,e):  
    global pret_max, preturi
    if Volum>=(volume[0]*a+volume[1]*b+volume[2]*c+volume[3]*d+volume[4]*e) :
        pret=preturi[0]*a+preturi[1]*b+preturi[2]*c+preturi[3]*d+preturi[4]*e
        if pret_max<pret:
            pret_max=pret
            return True
    else:
        return False

def Prel_Sol(a,b,c,d,e):
    x=[a,b,c,d,e]
    return x


for a in range (2): 
    for b in range (2):
        for c in range (2):
            for d in range (2):
                for e in range (2):
                    if (Sol_Pos(a,b,c,d,e)):                        
                         y=Prel_Sol(a,b,c,d,e)
                    
print('In rucsac s-au introdus:')            
for i in range(5):
    if y[i]>0:
        print('- obiectul ',i+1,'(', volume[i], ',',  preturi[i], ')')