from Tkinter import *
#import Player
root=Tk()
root.title("Choose your Pokemon!")
def callback():
    root.destroy()
def call1():
    callback()
    import BattleFire
def call2():
    callback()
    import BattleWater
def call3():
    callback()
    import BattleGrass
a=Button(root,command = call1)
photo1=PhotoImage(file="Delphox.gif")
a.config(image=photo1,width=photo1.width(),height=photo1.height())
b=Button(root,command = call2)
photo2=PhotoImage(file="Greninja.gif")
b.config(image=photo2,width=photo2.width(),height=photo2.height())
c=Button(root,command = call3)
photo3=PhotoImage(file="Chestnaught.gif")
c.config(image=photo3,width=photo3.width(),height=photo3.height())
a.pack(side =LEFT)
b.pack(side = RIGHT)
c.pack(side = TOP)
root.mainloop()
