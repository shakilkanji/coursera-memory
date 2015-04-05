# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global game_list, state, exposed, turns
    game_list = range(0,8) + range(0,8)
    random.shuffle(game_list)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    exposed = []
    for i in range(16):
        exposed.append(False)

     
# define event handlers
def mouseclick(pos):
    global state, exposed, click1, click2, turns
    # adds clicked spot to exposed
    def is_valid_click():
        for num in range(16):
            if pos[0] <= (num+1) * 50 and pos[0] >= num*50 and exposed[num] == False:
                return True
    
    def expose():
        for num in range(16):
            if pos[0] <= (num+1) * 50 and pos[0] >= num*50:
                exposed[num] = True
                return num
    if is_valid_click():
        if state == 0:
            state = 1
            click1 = expose()
        elif state == 1:
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
            click2 = expose()
        else:
            if game_list[click1] != game_list[click2]:
                exposed[click1] = False
                exposed[click2] = False
            state = 1
            click1 = expose()
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):    
    # expose selected card
    for num in range(16):
        if exposed[num]:
            card_pos = ((num+1) * 50 - 30, 50)
            canvas.draw_text(str(game_list[num]), card_pos, 20, "Blue")
        else:
            card_area = [((num)*50,0), ((num)*50, 100), 
                         ((num+1)*50, 100), ((num+1)*50, 0)]
            canvas.draw_polygon(card_area, 1, "Black", "Green")
           


# create frame and add button/labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
