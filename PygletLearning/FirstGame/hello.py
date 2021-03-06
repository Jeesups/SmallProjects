import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()
image = pyglet.resource.image('proxy.jpg')

label = pyglet.text.Label('Hello, World',
font_name = 'Times New Roman',
font_size = 16,
x=window.width//2,
y=window.height//2,
anchor_x ='center',
anchor_y ='center')

@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

@window.event
def on_draw():
    window.clear()
    #label.draw()
    image.blit(0,0)

@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        print("The left mouse button was pressed")


pyglet.app.run()