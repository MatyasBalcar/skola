import pyglet
from pyglet import shapes

window_size=[500,500]

window = pyglet.window.Window(window_size[0],window_size[1])
batch = pyglet.graphics.Batch()
#Line(x, y, x2, y2, width=1, color=(255, 255, 255, 255), batch=None, group=None)
line1 = shapes.Line(0, 0, 500, 0, width=2, batch=batch)
line2 = shapes.Line(0, 50, 500, 50, width=2, batch=batch)
line3 = shapes.Line(0, 100, 500, 100, width=2, batch=batch)
line4 = shapes.Line(0, 150, 500, 150, width=2, batch=batch)
line5 = shapes.Line(0, 200, 500, 200, width=2, batch=batch)
line6 = shapes.Line(0, 250, 500, 250, width=2, batch=batch)
line7 = shapes.Line(0, 300, 500, 300, width=2, batch=batch)
line8 = shapes.Line(0, 350, 500, 350, width=2, batch=batch)
line9= shapes.Line(0, 400, 500, 400, width=2, batch=batch)
line10= shapes.Line(0, 450, 500, 450, width=2, batch=batch)
line11= shapes.Line(0, 498, 500, 498, width=2, batch=batch)
h_line1 = shapes.Line(0, 0, 0, 500, width=2, batch=batch)
h_line2 = shapes.Line( 50,0,  50,500, width=2, batch=batch)
h_line3 = shapes.Line(100,  0, 100,500, width=2, batch=batch)
h_line4 = shapes.Line( 150,  0,150,500, width=2, batch=batch)
h_line5 = shapes.Line(200,0,   200,500, width=2, batch=batch)
h_line6 = shapes.Line(250,0,  250,500,  width=2, batch=batch)
h_line7 = shapes.Line(300,0,  300,500,  width=2, batch=batch)
h_line8 = shapes.Line(350,0,   350,500, width=2, batch=batch)
h_line9= shapes.Line(400, 0,  400,500, width=2, batch=batch)
h_line10= shapes.Line(450,0,   450,500, width=2, batch=batch)



#Rectangle(x, y, width, height, color=(255, 255, 255, 255), batch=None, group=None)
p1pos=[0,0]
p2pos=[450,450]

player1= shapes.Rectangle( p1pos[0],p1pos[1],50,50, color=(179, 11, 2), batch=batch)
player2= shapes.Rectangle( p2pos[0],p2pos[1],50,50, color=(52, 240, 19), batch=batch)




@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    latestp1dir=""
    latestp2dir=""
    ###---MOVEMENT---###
    if symbol == pyglet.window.key.D and player1.anchor_x>-450:
        player1.anchor_x-=50
        latestp1dir="right"
    if symbol == pyglet.window.key.A and player1.anchor_x<0:
        player1.anchor_x+=50
        latestp1dir="left"
    if symbol == pyglet.window.key.W and player1.anchor_y>-450:
        player1.anchor_y-=50
        latestp1dir="up"
        print(latestp1dir)
    if symbol == pyglet.window.key.S and player1.anchor_y<0:
        latestp1dir="down"
        player1.anchor_y+=50 
    if symbol == pyglet.window.key.L and player2.anchor_x>0:
        player2.anchor_x-=50
        latestp2dir="right"
    if symbol == pyglet.window.key.J and player2.anchor_x<450:
        latestp2dir="left"
        player2.anchor_x+=50
    if symbol == pyglet.window.key.I and player2.anchor_y>0:
        player2.anchor_y-=50
        latestp2dir="up"
    if symbol == pyglet.window.key.K and player2.anchor_y<450:
        player2.anchor_y+=50 
        latestp2dir="down"
    ###---SHOOTING---###
    if symbol == pyglet.window.key.Q:
        pass
pyglet.app.run()

