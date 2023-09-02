import pygame as py

import settings as sett


class Human:
    def __init__(self):
        self.human_pics = py.image.load("human_pics.png")
        self.box = py.rect.Rect([96, 96], [sett.HU_PIC_SIZE_FINISH, sett.HU_PIC_SIZE_FINISH])
        self.speed_x = 0
        self.speed_y = 0
        self.hu_pics_up = []
        self.hu_pics_down = []
        self.hu_pics_left = []
        self.hu_pics_right = []
        self.hu_up_true = 1
        self.hu_down_true = 0
        self.hu_left_true = 0
        self.hu_right_true = 0
        self.get_hu_pics()
        self.pic_number = 0
        self.if_hu_speed = 0

    def get_hu_pics(self):
        for f in range(4):
            hu_pic_start = self.human_pics.subsurface([32 * f, 0], [31, 31])
            hu_pic_finish = py.transform.scale(hu_pic_start, [sett.HU_PIC_SIZE_FINISH, sett.HU_PIC_SIZE_FINISH])
            self.hu_pics_down.append(hu_pic_finish)
        for f in range(4):
            hu_pic_start = self.human_pics.subsurface([32 * f, 32], [31, 31])
            hu_pic_finish = py.transform.scale(hu_pic_start, [sett.HU_PIC_SIZE_FINISH, sett.HU_PIC_SIZE_FINISH])
            self.hu_pics_left.append(hu_pic_finish)
        for f in range(4):
            hu_pic_start = self.human_pics.subsurface([32 * f, 64], [31, 31])
            hu_pic_finish = py.transform.scale(hu_pic_start, [sett.HU_PIC_SIZE_FINISH, sett.HU_PIC_SIZE_FINISH])
            self.hu_pics_right.append(hu_pic_finish)
        for f in range(4):
            hu_pic_start = self.human_pics.subsurface([32 * f, 96], [31, 31])
            hu_pic_finish = py.transform.scale(hu_pic_start, [sett.HU_PIC_SIZE_FINISH, sett.HU_PIC_SIZE_FINISH])
            self.hu_pics_up.append(hu_pic_finish)

    def draw(self, window, camera):
        self.speed_prorisovka()
        new_box = camera.o_box_n_box(self)
        if self.hu_up_true == 1:
            window.blit(self.hu_pics_up[int(self.pic_number) % 4], new_box)
        if self.hu_down_true == 1:
            window.blit(self.hu_pics_down[int(self.pic_number) % 4], new_box)
        if self.hu_left_true == 1:
            window.blit(self.hu_pics_left[int(self.pic_number) % 4], new_box)
        if self.hu_right_true == 1:
            window.blit(self.hu_pics_right[int(self.pic_number) % 4], new_box)

    def speed_prorisovka(self):

        if self.if_hu_speed == 1:
            self.pic_number = (self.pic_number + 0.25)

    def t_f_wall(self, tile_all_list):
        for f in tile_all_list:
            if self.box.colliderect(f.box) and f.number in sett.TILE_NUMBER_WALLS_LIST:
                return True
        return False


    def control(self):
        keys = py.key.get_pressed()
        self.speed_y = 0
        self.speed_x = 0
        if keys[py.K_w] == 1:
            self.hu_up_true = 1
            self.hu_down_true = 0
            self.hu_left_true = 0
            self.hu_right_true = 0
            self.if_hu_speed = 1
            self.speed_y = -sett.HU_SPEED
        if keys[py.K_s] == 1:
            self.hu_up_true = 0
            self.hu_down_true = 0
            self.hu_left_true = 1
            self.hu_right_true = 0
            self.if_hu_speed = 1
            self.speed_y = +sett.HU_SPEED
        if keys[py.K_a] == 1:
            self.hu_up_true = 0
            self.hu_down_true = 1
            self.hu_left_true = 0
            self.hu_right_true = 0
            self.if_hu_speed = 1
            self.speed_x = -sett.HU_SPEED
        if keys[py.K_d] == 1:
            self.hu_up_true = 0
            self.hu_down_true = 0
            self.hu_left_true = 0
            self.hu_right_true = 1
            self.if_hu_speed = 1
            self.speed_x = +sett.HU_SPEED
        self.box.x = self.box.x + self.speed_x
        self.box.y = self.box.y + self.speed_y
        if keys[py.K_w] == 0 and keys[py.K_s] == 0 and keys[py.K_a] == 0 and keys[py.K_d] == 0:
            self.if_hu_speed = 0






