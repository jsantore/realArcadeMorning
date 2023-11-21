import arcade
from SpaceHelpers import WINDOW_HEIGHT
from SpaceHelpers import WINDOW_WIDTH
import SpaceHelpers

class SpaceWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Program")
        self.targets = None
        self.player = None

    def setup(self):
        self.player = arcade.Sprite("Blue-05.png")
        self.player.center_x = 16
        self.player.center_y  = WINDOW_HEIGHT/2
        self.targets = SpaceHelpers.make_rocks()

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()



def main():
    our_window = SpaceWindow()
    our_window.setup()
    arcade.run()

main()
