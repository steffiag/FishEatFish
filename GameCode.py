import random
import arcade

# --- Constants (other than powerups) ---
SPRITE_SCALING_PLAYER = .5
FISH_COUNT = 20

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Fish Eat Fish"

class enemy():
    
    def __init__(self,image,speed,size):
        self.size = size
        self.speed = speed
        self.image = image
        

normal_fish = [enemy("images/""Enemy_0.png",2,.3),
                enemy("images/""Enemy_1.png",3,.4),
                enemy("images/""Enemy_2.png",1.5,.6),
                enemy("images/""Enemy_3.png",4,.2),
                enemy("images/""Enemy_4.png",1,.7),
                enemy("images/""Enemy_5.png",.25,.5)]

class power():

    def __init__(self,image):
        self.image = image
        self.size = .25
        self.speed = 0

power_ups = [power("images/""Powerup_size.png"),
            power("images/""Powerup_speed.png"),
            power("images/""Powerup_shield.png")]

class Fish(arcade.Sprite):

    def __init__(self, typeoffish):

        self.typeoffish = typeoffish
        
        sprite_scaling = self.typeoffish.size
        filename = self.typeoffish.image
        super().__init__(filename, sprite_scaling)

        self.change_x = (self.typeoffish.speed)*(random.randint(-1,1))
        self.change_y = (self.typeoffish.speed)*(random.randint(-1,1))
        
        

    def update(self):

        # Move the fish
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.fish_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.powerup_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("images/""Player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        # Create the fish
        for i in range(20):

            # Create the fish instance
            fish = Fish(normal_fish[random.randint(0,5)])

            # Position the fish
            fish.center_x = random.randrange(SCREEN_WIDTH-30)+15
            fish.center_y = random.randrange(SCREEN_HEIGHT-30)+15
            randnum1 = random.randint(-1,1)
            while randnum1 == 0:
                randnum1 = random.randint(-1,1)
            randnum2 = random.randint(-1,1)
            while randnum2 == 0:
                randnum2 = random.randint(-1,1)
            fish.change_x = (fish.typeoffish.speed)*randnum1
            fish.change_y = (fish.typeoffish.speed)*randnum2

            # Add the fish to the lists
            self.all_sprites_list.append(fish)
            self.fish_list.append(fish)

        # Create the powerups
        for i in range(5):

            # Create the powerup instance
            powerup = Fish(power_ups[random.randint(0,2)])

            # Position the powerup
            powerup.center_x = random.randrange(SCREEN_WIDTH-60)+30
            powerup.center_y = random.randrange(SCREEN_HEIGHT-60)+30
            
            # Add the powerups to the lists
            self.all_sprites_list.append(powerup)
            self.powerup_list.append(powerup)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = f"Size: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

        # Generate a list of all fish that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fish_list)
        
        # Loop through each colliding fish, remove it, and add to the score.
        for fish in hit_list:
            fish.remove_from_sprite_lists()
            self.score += 1

        # Generate a list of all powerups that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.powerup_list)
        
        # Loop through each colliding powerup and remove it.
        for powerup in hit_list:
            if powerup == power_ups[0]:
                self.size()
            powerup.remove_from_sprite_lists()

    def size(self):
        # Create larger sprite in the same place
        self.player_sprite2 = arcade.Sprite("images/""Player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite2.center_x = self.player_sprite.center_x
        self.player_sprite2.center_y = self.player_sprite.center_y

        # Remove old sprite
        self.player_sprite.remove_from_sprite_lists()

        # Remake sprite
        SPRITE_SCALING_PLAYER += .25
        self.player_sprite = arcade.Sprite("images/""Player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = self.player_sprite2.center_x
        self.player_sprite.center_y = self.player_sprite2.center_y

        self.all_sprites_list.append(self.player_sprite)

        # Change score
        self.score += 5
        
        # Redraw everything
        self.all_sprites_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()