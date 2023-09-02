import pygame as py

import settings as sett


class Map:
    def __init__(self):
        self.til_pics = py.image.load("rpg_tileset.png")
        self.map_csv_lists = []
        self.file_to_list()
        self.tiles_pic_list = []
        self.get_til_pics()
        self.til_list = []
        self.born_tile()
        self.map_size_x = sett.MAP_TILE_PIC_SIZE_FINISH * len(self.map_csv_lists[0])
        self.map_size_y = sett.MAP_TILE_PIC_SIZE_FINISH * len(self.map_csv_lists)

    def get_til_pics(self):
        for f1 in range(8):
            for f2 in range(17):
                til_pic_start = self.til_pics.subsurface([f2 * sett.MAP_TILE_PIC_SIZE_START, f1 * sett.MAP_TILE_PIC_SIZE_START], [sett.MAP_TILE_PIC_SIZE_START, sett.MAP_TILE_PIC_SIZE_START])
                til_pic_finish = py.transform.scale(til_pic_start, [sett.MAP_TILE_PIC_SIZE_FINISH, sett.MAP_TILE_PIC_SIZE_FINISH])
                self.tiles_pic_list.append(til_pic_finish)

    def file_to_list(self):
        scv_file = open("RPG_map..csv", "r")
        for f1 in scv_file:
            f2 = f1.split(",")
            self.map_csv_lists.append(f2)

    def born_tile(self):
        g1 = -1
        for f1 in self.map_csv_lists:
            g1 += 1
            g2 = -1
            for f2 in f1:
                g2 += 1
                til_pic = self.tiles_pic_list[int(f2)]
                pic_x = g2 * sett.MAP_TILE_PIC_SIZE_FINISH
                pic_y = g1 * sett.MAP_TILE_PIC_SIZE_FINISH
                d = Tile([pic_x, pic_y], til_pic, int(f2))
                self.til_list.append(d)

    def draw(self, window, camera):
        for f in self.til_list:
            f.draw(window, camera)


class Tile:
    def __init__(self, x_y, picture, tile_num):
        self.box = py.rect.Rect(x_y, [sett.MAP_TILE_PIC_SIZE_FINISH, sett.MAP_TILE_PIC_SIZE_FINISH])
        self.pic = picture
        self.number = tile_num

    def draw(self, window, camera):
        new_box = camera.o_box_n_box(self)
        window.blit(self.pic, new_box)