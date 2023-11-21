import random

import arcade
import frogHelpers

WINDOW_WIDTH = 1536
WINDOW_HEIGHT = 1000

class Comp151FirstWindow (arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Our First Real Arcade Window")
        self.player = None
        self.target = None
        self.score = None
        self.grass_list = None

    def setup(self):
        self.player = arcade.Sprite(":resources:images/enemies/frog.png")
        self.player.center_x = 100
        self.player.center_y = 200
        self.target = arcade.Sprite(":resources:images/enemies/fly.png")
        self.target.center_x = random.randint(0, WINDOW_WIDTH)
        self.target.center_y = random.randint(WINDOW_HEIGHT/2, WINDOW_HEIGHT)
        self.grass_list = frogHelpers.make_grass()

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(0,0, WINDOW_WIDTH, WINDOW_HEIGHT/2,
                                          arcade.color.OLIVE)
        arcade.draw_xywh_rectangle_filled(0,WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT/2,
                                          arcade.color.LIGHT_BLUE)
        self.grass_list.draw()
        self.player.draw()
        self.target.draw()
        arcade.finish_render()