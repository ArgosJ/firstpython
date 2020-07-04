import arcade
#contantes
SREEN_WIDTH = 1000
SCREEN_HEIGHT =  500
SCREEN_TITLE = "Mario Demo"

#contantes para  escalar los sprites 
CHARACTER_SCALING = 0.17
GROUND_SCALING = 0.20 
CYLINDER_SCALING = 0.20


 
class Mygame(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_HEIGHT,SREEN_WIDTH,SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWERS_BLUE)

        #Listas que contendran los 
        #Variable de jugador 
        self.player_sprite = None


    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

    # Crear jugador 
    imagen_source = "mario.png"
    self.player_sprite = arcade.sprite(imagen_source, CHARACTER_SCALING)
    self.player_sprite.center_x = 64
    self.player_sprite.center_y = 94 
    self.player_list.append(self.player_sprite)

       
    #Crea el piso  
        



    def setup(self):     
        pass

    def on_draw(self):
        arcade.start_render()

def main(): 
    window = Mygame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
     
    