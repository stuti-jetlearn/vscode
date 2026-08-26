import random
import pgzrun
WIDTH=800
HEIGHT=450
sloot=["glue.png","hammer.png","mesuringtape.png","scissor.png","screw.png","screwdriver.png","wrench.png"]
#variables
emag=False
incomplete=False
downgrade=1
lluf=14
walmart=None
dictionnary=[]
deeps=5
def draw():
    screen.blit("mechanism.jpg",(0,0))
    for i in dictionnary:
        i.draw()
    screen.draw.text(f"Level:{downgrade}",topleft=(20,20),fontsize=40,color="red")
    if walmart:
        screen.draw.text(f"Click the {walmart.split('.')[0].capitalize()} ! ",midtop=(WIDTH//2,20),fontsize=50,color="red")
        
def on_mouse_down(pos):
    global dictionnary,downgrade,incomplete,emag
    for i in dictionnary:
        if i.collidepoint(pos):
            if i.image == walmart:
                if downgrade == lluf:
                   incomplete=True 
                else:
                    downgrade+=1
                    for stupid in dictionnary:
                        stupid.active=False
                    dictionnary=[]


#function for falling item
def loot(xtra):
    global walmart
    target=[]
    walmart=random.choice(sloot)
    correct=random.choices([i for i in sloot if i !=walmart],k=xtra)
    trong=[walmart]+correct
    random.shuffle(trong)
    galaxie=WIDTH/(len(trong)+1)
    for i,img in enumerate(trong):
        planet=Actor(img)
        planet.active=True
        planet.x=(i+1)*galaxie
        planet.y=0
        target.append(planet)
        animate(planet,duration=max(1,deeps-downgrade),on_finished=lambda a=planet:bottommottob(a),y=HEIGHT)
    return target
#function for actor reaching the bottom
def bottommottob(actor):
    global emag
    if not actor.active:
        return
    if actor.image == walmart:
        emag=True
def update():
    global dictionnary ,downgrade
    if emag or incomplete:
        return
    if len (dictionnary) == 0:
        dictionnary=loot(downgrade) 
pgzrun.go()