from JDfile import *

#Helps to look at start of debug
print('--Game Start--')

game = Game(800,600,'Test')

maps = {
    
    'level1':[[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,1],
              [0,0,0,0,0],
              [0,0,0,0,0]],
    'level2':[[0,1,0],
              [0,1,0],
              [1,1,1],
              [1,1,1]]
}

#Current State
state = State('menu')

#Assign curMap a map object
curMap = Map(maps['level2'], game)

blk = blocks(curMap,game)
state.change('menu')

p1 = player(200,200,game)
ch = Image('SSimg\\crosshair.png',game)

while not game.over:
    game.processInput()
    if str(state.st) == 'menu':
        game.clearBackground((37))
        
        ch.moveTo(mouse.x,mouse.y)
        ch.draw()
        if mouse.LeftButton:
            state.change('prep')
    elif str(state.st) == 'pre':
        curMap.render(blk)
        curMap.collided(p1)
        p1.move()
    game.update(60)
game.quit()
