import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.BABY_BLUE)
        
        self.background = None
        
        # Render button
        default_style = {
            "font_name": ("Kenney Blocks", "arial"),
            "font_size": 12,
            "font_color": arcade.color.INDIGO,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.YELLOW,

            # used if button is pressed
            "bg_color_pressed": arcade.color.YELLOW,
            "border_color_pressed": arcade.color.YELLOW,  # also used when hovered
            "font_color_pressed": arcade.color.INDIGO
        }
        
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        restart_button = arcade.gui.UIFlatButton(text="Play again?",width=150, style = default_style)
        self.v_box.add(restart_button.with_space_around(bottom=3.5))
        restart_button.on_click = self.on_restart
        
        end_button = arcade.gui.UIFlatButton(text="Stop?",width=150, style = default_style)
        self.v_box.add(end_button.with_space_around(bottom=3.5))
        end_button.on_click = self.on_end

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box))


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        # sets up background
        self.background = arcade.load_texture("images/""FishHome.png")

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

    def on_restart(self,event):
        pass

    def on_end(self,event):
        arcade.window_commands.close_window

    
        

def main():
    game = End_Homepage(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()