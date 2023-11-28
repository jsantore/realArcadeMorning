import time

import arcade
from SpaceHelpers import WINDOW_HEIGHT
from SpaceHelpers import WINDOW_WIDTH
import SpaceHelpers

class SpaceWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Program")
        self.targets = None
        self.player = None
        self.dy = 0
        self.ouch = False

    def setup(self):
        self.player = arcade.Sprite("Blue-05.png")
        self.player.scale = 2
        self.player.center_x = 32
        self.player.center_y  = WINDOW_HEIGHT/2
        self.targets = SpaceHelpers.make_rocks()

    def on_update(self, delta_time: float):
        self.move_player()
        for rock in self.targets:
            rock.center_x -= 1
            if rock.center_x <=0:
                rock.center_x = WINDOW_WIDTH+64
        if arcade.check_for_collision_with_list(self.player, self.targets):
            self.ouch = True


    def move_player(self):
        self.player.center_y += self.dy
        if self.player.center_y >= WINDOW_HEIGHT:
            self.player.center_y = WINDOW_HEIGHT
        elif self.player.center_y <= 0:
            self.player.center_y = 0


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.DOWN:
            self.dy = -2
        elif symbol == arcade.key.UP:
            self.dy = 2

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.DOWN or symbol == arcade.key.UP:
            self.dy = 0
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        if self.ouch:
            losetext = arcade.Text("Ouch!", WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4, arcade.color.LIGHT_BLUE, 30)
            losetext.draw()
            self.ouch = False
        arcade.finish_render()




def main():
    our_window = SpaceWindow()
    our_window.setup()
    arcade.run()

main()
