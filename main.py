import pygame as py

# ===================================================================

import settings as sett
import sprites as spr
import functions as fun
import camera as cam
import map

# ===================================================================

window = py.display.set_mode([sett.WIDTH, sett.HEIGHT])

time = py.time.Clock()

# ===================================================================

human_main = spr.Human()
map_main = map.Map()
print(map_main.map_csv_lists)
camera = cam.Camera(human_main)


# ===================================================================


while_number = False

while while_number == 0:
    window.fill("#000000")

    map_main.draw(window, camera)

    camera.beholder([map_main.map_size_x, map_main.map_size_y])

    human_main.draw(window, camera)
    human_main.control()

    # ===================================================================
    py.display.update()
    events = py.event.get()
    for f in events:
        if f.type == py.QUIT:
            while_number += 1

    time.tick(60)






























