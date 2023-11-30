import random
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
        self.ouch_sound = None
        self.music = None
        self.shots = arcade.SpriteList()

    def setup(self):
        self.player = arcade.Sprite("Blue-05.png")
        self.player.scale = 2
        self.player.center_x = 32
        self.player.center_y  = WINDOW_HEIGHT/2
        self.targets = SpaceHelpers.make_rocks()
        self.ouch_sound = arcade.load_sound(":resources:sounds/hurt3.wav")
        self.music = arcade.load_sound(":resources:music/funkyrobot.mp3")

    def on_update(self, delta_time: float):
        self.move_player()
        for rock in self.targets:
            rock.center_x -= 1
            if rock.center_x <=0:
                rock.center_x = WINDOW_WIDTH+64
        for shot in self.shots:
            shot.center_x += 2
            if shot.center_x > WINDOW_WIDTH:
                self.shots.remove(shot)
        if arcade.check_for_collision_with_list(self.player, self.targets):
            self.ouch = True
            arcade.play_sound(self.ouch_sound)
            self.player.center_y = random.randint(self.player.height/2, WINDOW_HEIGHT)


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
        if symbol == arcade.key.SPACE:
            new_shot = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
            new_shot.center_y = self.player.center_y
            new_shot.center_x = self.player.center_x+self.player.width
            self.shots.append(new_shot)
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        self.shots.draw()
        if self.ouch:
            losetext = arcade.Text("Ouch!", WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4, arcade.color.LIGHT_BLUE, 30)
            losetext.draw()
            self.ouch = False
        arcade.finish_render()




def main():
    our_window = SpaceWindow()
    our_window.setup()
    arcade.play_sound(our_window.music, looping=True)
    arcade.run()

main()
