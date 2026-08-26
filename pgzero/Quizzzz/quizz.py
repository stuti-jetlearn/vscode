import pgzrun
TITLE="Quizizz"
HEIGHT=800
WIDTH=1200

marquee=Rect(0,0,1200,80)
main=Rect(0,0,900,135)
m1=Rect(0,0,435,240)
m2=Rect(0,0,435,240)
m3=Rect(0,0,435,240)
m4=Rect(0,0,435,240)
skip=Rect(0,0,250,500)
timer=Rect(0,0,250,135)
marquee.move_ip(0,0)
main.move_ip(15,115)
m1.move_ip(15,280)
m2.move_ip(15,540)
m3.move_ip(480,280)
m4.move_ip(480,540)
timer.move_ip(935,115)
skip.move_ip(935,280)

#variables
score=0
timee=20
questionfile="questions.txt"
gameo=False
l1q=[]
index=0
questionc=0

l1=[m1,m2,m3,m4]
def draw():
    screen.draw.filled_rect(marquee,"light blue")
    screen.draw.filled_rect(main,"blue")
    screen.draw.filled_rect(timer,"darkgreen")
    screen.draw.filled_rect(skip,"darkgreen")
    for i in l1:
        screen.draw.filled_rect(i,"purple")
    mess="Welcome to Quizizz-"
    mess=mess+f"Q: {index} of {questionc}"
    screen.draw.textbox(mess,marquee,color="white")
    screen.draw.textbox(str(timee),timer,color="black",shadow=(0.5,0.5),scolor="lightgreen")
    screen.draw.textbox("SKIP",skip,color="black",shadow=(0.5,0.5),scolor="lightgreen",angle=-90)
    screen.draw.textbox(question[0].strip(),main,color="black",shadow=(0.5,0.5),scolor="lightblue")
    count=1
    for i in l1:
        screen.draw.textbox(question[count].strip(),i,color="black",shadow=(0.5,0.5),scolor="pink")
        count+=1
def move():
    marquee.x-=3
    if marquee.right<0:
        marquee.left=1200
def read():
    global questionc,index,l1q
    file=open(questionfile,"r")
    for question in file:
        l1q.append(question)
        #l1q.append(question.strip().split(","))
        questionc+=1
    file.close()
def nextq():
    global index
    index+=1
    return l1q.pop(0).split(",")
def update():
    pass
    move()
def updatetime():
    global timee
    if timee>0:
        timee-=1
    else:
        gameofunc()
def gameofunc():
    global question,timee,gameo
    gameo=True
    timee=0
    mess=f"The game is over,score is {score}"
    question=[mess,"-","-","-","-",5]
def skipfunc():
    global question,timee
    if l1q and not gameo:
        question=nextq()
        timee=20
    else:
        gameofunc()
def on_mouse_down(pos):
    ind=1
    for box in l1:
        if box.collidepoint(pos):
            if ind==int(question[5]):
                correctans()
            else:
                gameofunc()
        ind+=1
    if skip.collidepoint(pos):
        skipfunc()
def correctans():
    global timee,question,score,l1q
    score+=1
    if l1q:
        question=nextq()
        timee=20
    else:
        gameofunc()
read()
question=nextq()
clock.schedule_interval(updatetime,1)
pgzrun.go()