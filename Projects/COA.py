###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")


q1 = codesters.Square(100, 100, 200, 'black')
q2 = codesters.Square(-100, 100, 200, 'green')
q3 = codesters.Square(-100, -100, 200, 'black')
q4 = codesters.Square(100, -100, 200, 'green')


mySprite2 = codesters.Sprite("soccer2.png",100,-100)
mySprite1 = codesters.Sprite("harvester2.jpeg",100,100)
mySprite3 = codesters.Sprite("bass.png",-100,-100)
mySprite4 = codesters.Sprite("book.png",-100,100)
mySprite2.set_size(0.1)
mySprite1.set_size(0.2)
mySprite3.set_size(0.4)
mySprite4.set_size(0.15)

codesters.Text("Ryder Lawson",0,220)
codesters.Text("Intelligence is key",0,-220)