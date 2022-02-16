# Purpose:  Atari Phong Game

# import library
from cis552 import *

# Constants
WINDOW_H = 400   # window height
WINDOW_W = 400   # window width
PADDLE_H = 80    # paddle height
PADDLE_W = 20    # paddle width
MOVING_S = 2     # moving speed
LPADDLE_UP = "a"    # left paddle up
LPADDLE_DOWN = "z"  # left paddle down
RPADDLE_UP = "k"    # right paddle up
RPADDLE_DOWN = "m"  # right paddle down
NEW_GAME = " "      # new game
QUIT_GAME = "q"     # quit game
BALL_R = 5          # ball radius
V = 5               # magnitude of horizontal velocity
DT = 1              # time increment

# Global variables
lp_x = 0                     # x coordinate of left paddle
lp_y = 0                     # y coordinate of left paddle
rp_x = WINDOW_W-PADDLE_W     # x coordinate of right paddle
rp_y = WINDOW_H-PADDLE_H     # y coordinate of right paddle
b_x = WINDOW_W/2            # x coordinate of ball
b_y = WINDOW_H/2            # y coordinate of ball
vx = V                     # horizontal velocity of ball
vy = V/4                     # vertical velocity of ball
lp_up = False                # flag for left paddle up
lp_down = False             # flag for left paddle down
rp_up = False                # flag for right paddle up
rp_down = False              # flag for right paddle down
new = False                  # flag for a new game

# Functions
def draw_frame():
    global lp_x, lp_y, rp_x, rp_y
    global b_x, b_y, vx, vy, lp_up, lp_down, rp_up, rp_down, exit, new

    if new == True:
        lp_x = 0  # x coordinate of left paddle
        lp_y = 0  # y coordinate of left paddle
        rp_x = WINDOW_W - PADDLE_W  # x coordinate of right paddle
        rp_y = WINDOW_H - PADDLE_H  # y coordinate of right paddle
        b_x = WINDOW_W / 2  # x coordinate of ball
        b_y = WINDOW_H / 2  # y coordinate of ball
        vx = V  # horizontal velocity of ball
        vy = V / 4  # vertical velocity of ball
        lp_up = False  # flag for left paddle up
        lp_down = False  # flag for left paddle down
        rp_up = False  # flag for right paddle up
        rp_down = False  # flag for right paddle down
        new = False

    set_clear_color(0.0, 0.0, 0.0)
    clear()

    disable_stroke()
    set_fill_color(1, 0, 0)
    draw_rectangle(lp_x, lp_y, PADDLE_W, PADDLE_H)
    draw_rectangle(rp_x, rp_y, PADDLE_W, PADDLE_H)

    # update y coordinate of left paddle
    lpy2 = lp_y
    if lp_up == True and (lp_y-DT*V >0):
        lpy2 = lp_y - DT*V
        lp_up = False                 # apply the movement just once
    elif lp_down == True and (lp_y+DT*V <WINDOW_H-PADDLE_H):
        lpy2 = lp_y + DT*V
        lp_down = False
    lp_y = lpy2

    # update y coordinate of right paddle
    rpy2 = rp_y
    if rp_up == True and (rp_y - DT * V > 0):
        rpy2 = rp_y - DT * V
        rp_up = False
    elif rp_down == True and (rp_y + DT * V < WINDOW_H - PADDLE_H):
        rpy2 = rp_y + DT * V
        rp_down = False
    rp_y = rpy2

    # calculate temporary new coordinates of ball
    bx2 = b_x + vx*DT     # new x coordinate of ball
    by2 = b_y + vy * DT  # new y coordinate of ball

    # test horizontally
    if by2 > lp_y and by2 < lp_y+PADDLE_H and bx2 < BALL_R+PADDLE_W:       # test on left paddle
        vx = -vx
    elif by2 > rp_y and by2 < rp_y+PADDLE_H and bx2 > WINDOW_W-BALL_R-PADDLE_W:       # test on right paddle
        vx = -vx
    elif bx2 > WINDOW_W-BALL_R or bx2 < BALL_R:   # test on right or left side walls
        vx = -vx

    # test vertically
    elif bx2 > lp_x and bx2 < lp_x+PADDLE_W and (by2>lp_y-BALL_R or by2<lp_y+PADDLE_H+BALL_R):   # test on left paddle
        vy = -vy
    elif bx2 > rp_x and bx2 < rp_x+ PADDLE_W and (by2>rp_y-BALL_R or by2<rp_y+PADDLE_H+BALL_R): # test on right paddle
        vy = -vy
    elif by2 > WINDOW_H-BALL_R or by2 < BALL_R:   # test on lower and upper side walls
        vy = -vy

    # update coordinates of ball and draw the ball
    b_x += vx*DT
    b_y += vy*DT
    set_fill_color(0.8, 0.8, 0.8)
    draw_circle(b_x, b_y, BALL_R)

def keydown(key):
    global lp_up, lp_down, rp_up, rp_down, new

    if key == "a":
        lp_up = True
        lp_down = False
    elif key == "z":
        lp_up = False
        lp_down = True
    elif key == "k":
        rp_up = True
        rp_down = False
    elif key == "m":
        rp_up = False
        rp_down = True
    elif key == "q":
        cs1_quit()
    elif key == " ":
        new = True

start_graphics(draw_frame, 2400, key_press=keydown)






