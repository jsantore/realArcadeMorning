import arcade
WINDOW_WIDTH = 1536

def make_grass():
    #make an arcade spritelist full on grass tiles
    grass_list = arcade.SpriteList()
    for xLoc in range(64,WINDOW_WIDTH, 128):
        grass_tile = arcade.Sprite(":resources:images/tiles/grass.png")
        grass_tile.center_y = 64
        grass_tile.center_x = xLoc
        grass_list.append(grass_tile)
    return grass_list