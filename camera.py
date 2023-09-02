import pygame as py

import settings as sett

class Camera:
    def __init__(self, human):
        self.hu = human
        self.smechenie = [sett.WIDTH//2, sett.HEIGHT//2]

    def beholder(self, list):
        now_x = self.hu.box.x * -1 + sett.WIDTH//2
        now_y = self.hu.box.y * -1 + sett.HEIGHT//2
        if self.hu.box.x <= sett.WIDTH // 2:
            now_x = 0
        if self.hu.box.y <= sett.HEIGHT // 2:
            now_y = 0
        if self.hu.box.x >= list[0] - sett.WIDTH // 2:
            now_x = (list[0] - sett.WIDTH // 2) * -1 + sett.WIDTH//2
        if self.hu.box.y >= list[1] - sett.HEIGHT // 2:
            now_y = (list[1] - sett.HEIGHT // 2) * -1 + sett.HEIGHT//2
        self.smechenie[0] = now_x
        self.smechenie[1] = now_y

    def o_box_n_box(self, object):
        new_box = py.Rect([object.box.x + self.smechenie[0], object.box.y + self.smechenie[1]], [object.box.w, object.box.h])
        return new_box





































