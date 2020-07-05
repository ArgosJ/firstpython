import arcade
# contantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Mario Demo"

# contantes para  escalar los sprites
CHARACTER_SCALING = 0.17
GROUND_SCALING = 0.20
CYLINDER_SCALING = 0.20

#velocidad.del.jugador
PLAYER_MOVEMENT_SPEED = 5  
GRAVITY = 1
PLAYER_JUMP_SPEED =20

class Mygame(arcade.W indow):

    def __init__(self):
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Listas que contendran nuestos sprites
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Variable de jugador
        self.player_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Crear jugador
        imagen_source = "mario.png"
        self.player_sprite = arcade.Sprite(imagen_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 94
        self.player_list.append(self.player_sprite)

    # Crea el piso
    for x in range(0,1250,64)
    wall = arcade.Sprite("ground.png",GROUND_SCALING)
    wall.center_x = x
    wall.center_y= 32
    self.wall_list.append(wall

    #crea los cilinfros con un lista 
    coordinate_list = [[512,110],
                        [256, 110],
                        [768, 110]]

    for coordinate in coordinate_list:
        #add a creater on the ground 
        wall = arcade.sprite("cilinder.png".CYLINDER_SCALING)
        wall.position = coordinate
        self.wall_list.append(wall)

    #motor de fisica 
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                            self.wall_list ;GRAVITY)    


                                        




def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
        self.wall_list.draw()


def on_key_press(self, key, modifiers):

    in key ==arcade.key.UP:
        if.physics_engine.can_jump():
        self.player_sprite.change_y = PLAYER_JUMP_SPEED

    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

    elif key == arcade.key.LEFT:
        self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

    elif key == arcade.key.RIGHT:
        self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED

def on_key_release(self, key. modifiers):
   
    if key == arcade.key.LEFT:
        self.player_sprite.change_y = 0

    elif key == arcade.key.RIGHT:
        self.player_sprite.change_y = 0


    def on_update(self, data_time):

        self.physics_engine.update()




def main():
    window = Mygame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
