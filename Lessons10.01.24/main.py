import tkinter
import random
from tkinter import  PhotoImage

def prepare_and_start():
    global player

    canvas.delete('all')
    player_pos = (random.randint(1, n_x - 1) * ster
                  random.randint(1, n_x - 1) * ster)

    player = canvas.create_image(
        (player_pos[0], player[1], image=player_pik, async='пп')

    label.config(text='Найти выход!')
    master.bind('KeyPress>', key_pressed)

def move_wrap(obj, move_x, move_y)
    xy = canvas.coords(odj)
    canvas.move(odj, move_x, move_y)
    print(xy)
    if xy[o] <= 0:
         canvas.move(odj, WIDTH, 0)
    if xy[o] >= WIDTH:
         canvas.move(odj, WIDTH, 0)
    if xy[o] <= 0:
         canvas.move(odj, 0, HEIGHT)
    if xy[1] <= 0:
         canvas.move(odj, 0, -HEIGHT)

def key_pressed(event):
    if event.keysym == 'up':
         move_wrap(player, 0, -step)
    elif event.keysym






