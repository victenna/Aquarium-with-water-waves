import turtle,time,random
wn=turtle.Screen()
wn.setup(850,600)
AQ=[]
for i in range(74):
    i1=str(i)
    AQ.append(i1+'.gif')
image11 = ("fi11.gif")
image12 = ("fi12.gif")
image31 = ("fi31.gif")
image32 = ("fi32.gif")
wn.addshape(image11)
wn.addshape(image12)
wn.addshape(image31)
wn.addshape(image32)
t=turtle.Turtle()
t.showturtle()
t.speed(10)
t.penup()
X,Y=90,-90
dx,dy=2,4
k,r=0,0
while True:
    r=r+1
    k=k+1
    k1=k%74
    r1=r%100
    wn.bgpic(AQ[k1])
    t.setposition(X+dx,Y+dy)
    X,Y=t.position()
    if dx>0 and r1<50:
        t.shape(image11)
    if dx>0 and r1>50:   
        t.shape(image12)
    if dx<0 and r1<50:
        t.shape(image31)
    if dx<0 and r1>50:   
        t.shape(image32)
    if X>250 or X<-260:
        dx=-dx
    if Y<-205 or Y>210:
        dy=-dy  
    
   
