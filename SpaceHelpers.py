import random

import arcade

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 1500


def make_rocks():
    rock_list = arcade.SpriteList()
    file_names = [":resources:images/space_shooter/meteorGrey_big2.png",
                  ":resources:images/space_shooter/meteorGrey_big1.png",
                  ":resources:images/space_shooter/meteorGrey_big3.png"]

    for rock_number in range(10):
        file_name = random.choice(file_names)
        rock = arcade.Sprite(file_name)
        rock.center_x = random.randint(150, WINDOW_WIDTH)
        rock.center_y = random.randint(0, WINDOW_HEIGHT)
        rock_list.append(rock)
    return rock_list