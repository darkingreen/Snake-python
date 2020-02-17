import pyxel
import random
import math
import var

class Vector2():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    pyxel.init(var.sx, var.sy, caption="snake", scale=20,
               fps=60, border_color=0, border_width=0)
    sort()
    var.snakePos.append(Vector2(10, 10))
    pyxel.run(update, draw)

def update():
    if pyxel.btn(pyxel.KEY_W) and (var.direction != 2 or len(var.snakePos) == 1):
        var.direction = 0
    elif pyxel.btn(pyxel.KEY_D) and (var.direction != 3 or len(var.snakePos) == 1):
        var.direction = 1
    elif pyxel.btn(pyxel.KEY_S) and (var.direction != 0 or len(var.snakePos) == 1):
        var.direction = 2
    elif pyxel.btn(pyxel.KEY_A) and (var.direction != 1 or len(var.snakePos) == 1):
        var.direction = 3
     
    if pyxel.frame_count%20 == 0:
        movement()
        if colide():
            var.snakePos.clear()
            var.fruits.clear()
            var.snakePos.append(Vector2(10, 10))
            sort()
    
    if verify():
        var.snakePos.append(Vector2(var.snakePos[0].x, var.snakePos[0].y))
        
    pass
        
def draw():
    pyxel.cls(9)
    
    for f in var.fruits:
        pyxel.pix(f.x, f.y, 8)
        
    for i in var.snakePos:
        pyxel.pix(i.x, i.y, 7)
    pass

def movement():
    for i in range(len(var.snakePos), 1, -1):
        var.snakePos[i-1].x = var.snakePos[i-2].x
        var.snakePos[i-1].y = var.snakePos[i-2].y
        
    if var.direction == 0:
        var.snakePos[0].y -= 1
    elif var.direction == 1:
        var.snakePos[0].x += 1
    elif var.direction == 2:
        var.snakePos[0].y += 1
    elif var.direction == 3:
        var.snakePos[0].x -= 1
    
    var.snakePos[0].x = var.snakePos[0].x%pyxel.width
    var.snakePos[0].y = var.snakePos[0].y%pyxel.height
    pass
    
def sort():
    var.fruits.append(Vector2(random.randrange(0, 20), random.randrange(0, 20)))
    
def verify():
    for i in var.fruits:
        if math.floor(var.snakePos[0].x) == i.x and math.floor(var.snakePos[0].y) == i.y:
            var.fruits.remove(i)
            sort()
            return True
            
def colide():
    for i in var.snakePos:
        if var.snakePos[0].x == i.x and var.snakePos[0].y == i.y and i != var.snakePos[0]:
            return True

main()