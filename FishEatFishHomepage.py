"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import GameCode as gc
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Fish Eat Fish"




# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

class Homepage(arcade.Window):
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

        arcade.set_background_color(arcade.color.BLUE)
        
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

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start!",width=150, style = default_style)
        self.v_box.add(start_button.with_space_around(bottom=3.5))
        start_button.on_click = self.on_start
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box))
        
        # Create the buttons
        instructions_button = arcade.gui.UIFlatButton(text= "Instructions",width=150, style = default_style)
        self.v_box.add(instructions_button.with_space_around(bottom=-50))
        instructions_button.on_click = self.on_click_open
        
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box))
            
    def on_click_open(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text=(
                "You are the pink fish. You need to eat fish that are smaller than you. Eating a smaller fish increases your size. If you eat a fish thats bigger than you, you die and game over!"
            ),
            callback=self.on_message_box_close,
            buttons=["Ok"]
        )
        
        self.manager.add(message_box)

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
        
    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

    def on_start(self, event):
        # may not work
        arcade.close_window()
        gc.main()
        

        

def main():
    """ Main function """
    game = Homepage(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()