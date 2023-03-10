import arcade
import arcade.gui
import FishEatFishHomepage as restart

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Fish Eat Fish"




# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

class End_Homepage(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title, score, dead):
        super().__init__(width, height, title)
        
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.score = score

        arcade.set_background_color(arcade.color.BABY_BLUE)
        
        self.background = None
        
        # Render button
        default_style = {
            "font_name": ("Kenney Blocks", "arial"),
            "font_size": 12,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.GOLD,

            # used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            "border_color_pressed": arcade.color.WHITE,  # also used when hovered
            "font_color_pressed": arcade.color.GOLD
        }
        
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # show score
        if dead == True:
            restart_button = arcade.gui.UILabel(text=f"Your final score (before dying): {self.score}!", style = default_style,font_size=20,text_color=(255,0,255,255))
            self.v_box.add(restart_button.with_space_around(bottom=1.5))
        else:
            restart_button = arcade.gui.UILabel(text=f"Your final score: {self.score}!", style = default_style,font_size=20,text_color=(255,0,255,255))
            self.v_box.add(restart_button.with_space_around(bottom=1.5))


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box))


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        # sets up background
        self.background = arcade.load_texture("images/""EndScreen_Background.png")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        
        self.manager.draw()

    def on_end(self,event):
        arcade.close_window()

def main(score,dead):
    game = End_Homepage(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, score, dead)
    game.setup()
    arcade.window_commands.set_window(game)
    arcade.run()