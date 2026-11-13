import json,os
from urllib.request import*
V=(0,100,320,330,500,900,20000)
O=(-33,-31,-18,-14,14,18,31,33)
A=(-17,-15,15,17)
Q=(-16,-1,1,16)
DT=(0,0,O,A,Q,A+Q,A+Q)
l=range(128)
h=10**5
P=[[0]*64 for _ in range(8)]
for i in l[:64]:
 s,f=i//8,i%8;x=6-abs(f-3.5)-abs(s-3.5)
 P[1][i]=s*(s+2)
 for t in(2,3,4,5):P[t][i]=(5,4,1,2)[t-2]*x+(-18,-8,0,-5)[t-2]
 P[6][i]=(16,20,8,0)[min(f,7-f)]if s==0 else-12*s
CM=[15]*128
for i,v in((4,12),(116,3),(0,13),(7,14),(112,7),(119,11)):CM[i]=v
B=[0]*128;U=[];H=[0]*16384
class e(Exception):pass
def b():
 global S,C,E
 B[:]=[0]*128
 for i,v in enumerate((4,2,3,5,6,3,2,4)):B[i]=v;B[i+16]=1;B[i+96]=-1;B[i+112]=-v
 S=1;C=15;E=-1;U.clear()
def a(q,y):
 for D,V,L in(((-15*y,-17*y),(1,),0),(O,(2,),0),(A+Q,(6,),0),(A,(3,5),1),(Q,(4,5),1)):
  for d in D:
   t=q+d
   while not t&0x88:
    p=B[t]
    if p:
     if p*y>0 and abs(p)in V:return 1
     break
    if not L:break
    t+=d
 return 0
def g():
 ms=[]
 P=lambda o:ms.append(q|(o<<7)|5*((o>>4)==v)<<14)
 for q in l:
  p=B[q]
  if p*S>0:
   t=abs(p)
   if t==1:
    u=16*S;v=7*(S>0);o=q+u
    if B[o]==0:
     P(o)
     if(q>>4)==(1,6)[S<0]and B[q+2*u]==0:ms.append(q|((q+2*u)<<7))
    for d in(u-1,u+1):
     o=q+d
     if not o&0x88 and(B[o]*S<0 or o==E):P(o)
   else:
    for d in DT[t]:
     o=q+d
     while not o&0x88 and(w:=B[o])*S<=0:
      ms.append(q|(o<<7));o+=d
      if w or t in(2,6):break
 z=4+112*(S<0)
 for w,i in((1,1),(-1,2)):
  i*=1+3*(S<0);d=z+2*w
  if C&i and B[z+w]==B[d]==0 and(w>0 or B[z-3]==0)and not(a(z,-S)or a(z+w,-S)or a(d,-S)):ms.append(z|(d<<7))
 return ms
def m(v):
 global S,C,E
 f=v&127;u=v>>7&127;r=v>>14;p=B[f];t=abs(p);w=B[u]
 U.append((B[:],S,C,E))
 if t==1 and u==E and w==0:B[u-16*S]=0
 B[f]=0;B[u]=r*S or p
 if t==6 and abs(u-f)==2:
  j,k=(f+3,f+1)if u>f else(f-4,f-1)
  B[k],B[j]=B[j],0
 C&=CM[f]&CM[u]
 E=f+16*S if t==1 and abs(u-f)==32 else-1
 S=-S
def u():
 global S,C,E
 B[:],S,C,E=U.pop()
def c():return a(B.index(-6*S),S)
def v():
 global N
 s=q=0
 for x in l:
  p=B[x]
  if p:
   t=abs(p);r=x>>4;f=x&7;w=p<0;e=1-2*w;z=(r*e+7*w)*8+f
   s+=(V[t]+P[t][z])*e;q+=V[t]*(1<t<6)
 N=q
 return s*S
def o(ms):
 ms.sort(key=lambda m:10**6+10*V[abs(B[u])]-V[abs(B[m&127])]//10 if B[u:=(m>>7)&127]else H[m&16383],reverse=True)
 return ms
def y(d,A,b,p):
 global n,S,C,E
 n+=1
 if n>=4e4:raise e
 if d<-2:return v()
 w=-h-1
 if d<1:
  K=a(B.index(6*S),-S)
  if not K:
   st=v()
   if st>=b:return st
   if st+1100<A:return st
   A=max(A,st);w=A
 elif d>2 and p and not a(B.index(6*S),-S)and(st:=v())>=b and N>0:
  E0=E;E=-1;S=-S
  s=-y(d-3,-b,1-b,p+1)
  S=-S;E=E0
  if s>=b:return s
 f=0;z=0
 for q in o(g()):
  if d<1 and not K and(B[k:=(q>>7)&127]==0==q>>14 and k!=E or B[k]and V[abs(B[k])]<V[abs(B[q&127])]and q>>14==0):continue
  m(q)
  if c():u();continue
  f+=1;s=-y(d-1,-b,-A,p+1);u()
  if s>w:w=s;z=q
  if s>=b:H[q&16383]+=d*d;break
  A=max(A,s)
 if f==0:return -h+p if(K if d<1 else a(B.index(6*S),-S))else(A if d<1 else 0)
 return w
def z(v):
 f=v&127;u=v>>7&127;r=v>>14
 s="".join(chr(97+(x&7))+chr(49+(x>>4))for x in(f,u))
 if r:s+="nbrq"[r-2]
 return s
def w(u):
 f=int(u[1])*16+ord(u[0])-113;t=int(u[3])*16+ord(u[2])-113
 return f|(t<<7)|(("nbrq".find(u[4:])+2)*(len(u)>4)<<14)
def t(v):
 global n
 j=set(v);o=[]
 for q in g():m(q);z(q)in j and not c()and o.append(q);u()
 d=[[q,0]for q in o];n=0
 D=lambda:d.sort(key=lambda x:-x[1])
 try:
  for R in range(64):
   D();a=-h-1
   for f in d:m(f[0]);f[1]=-y(R,-h-1,-a,1);u();a=max(a,f[1])
   D()
 except e:pass
 D()
 return[z(q)for q,_ in d]
def p(g):
 b();[m(w(u))for u in g["moves"]];L=g["legal_moves"]
 try:return t(L)or L
 except Exception:return L
J=os.environ["MAKEFUN_ENV_URL"]
def j(p,b):
 try:return json.load(urlopen(J+p,json.dumps(b).encode()))
 except HTTPError:return{"_http":1}
def q():
 while 1:
  g=j("/game",{})
  if g.get("status")=="done"or"_http"in g:break
  while g["status"]=="your_move":
   for c in p(g):
    r=j("/move",{"game":g["game"],"move":c})
    if"_http"not in r:break
   else:j("/resign",{"game":g["game"]});break
   g=r
if __name__[2]=="m":q()
