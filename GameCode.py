
import random
import arcade
import EndScreen as ending

# --- Constants (other than powerups) ---
SPRITE_SCALING_PLAYER = .5
FISH_COUNT = 20

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Fish Eat Fish"
MOVEMENT_SPEED = 5

class enemy():
    
    def __init__(self,image,speed,image_size,size):
        self.image_size = image_size
        self.speed = speed
        self.image = image
        self.size = size
        

normal_fish = [enemy("images/""Enemy_0.png",2,.3,4),
                enemy("images/""Enemy_1.png",3,.4,10),
                enemy("images/""Enemy_2.png",1.5,.6,35),
                enemy("images/""Enemy_3.png",4,.2,2),
                enemy("images/""Enemy_4.png",1,.7,60),
                enemy("images/""Enemy_5.png",.25,.5,20)]

class power():

    def __init__(self,image,type):
        self.image = image
        self.image_size = .25
        self.speed = 0
        self.type = type

power_ups = [power("images/""Powerup_size.png","size"),
            power("images/""Powerup_speed.png","speed"),
            power("images/""Powerup_shield.png","shield")]

class Fish(arcade.Sprite):

    def __init__(self, typeoffish):

        self.typeoffish = typeoffish
        
        sprite_scaling = self.typeoffish.image_size
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
        self.num_of_fish = 0

        # Set up the player info
        self.player_sprite = None

        # As to not make the computer mad
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)
        self.background_color = arcade.color.BLEU_DE_FRANCE
        self._background_color = arcade.color.BLEU_DE_FRANCE

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.powerup_list = arcade.SpriteList()

        # Score
        self.score = 5

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
            self.num_of_fish += 1

        # Create the powerups
        for i in range(5):

            # Create the powerup instance
            powerup = Fish(power_ups[random.randint(0,2)])

            # Position the powerup
            powerup.center_x = random.randrange(SCREEN_WIDTH-140)+70
            powerup.center_y = random.randrange(SCREEN_HEIGHT-140)+70
            
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

    #def on_mouse_motion(self, x, y, dx, dy):
    def on_key_press(self, key, modifiers):
        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


        # Move the center of the player sprite to match the mouse x, y
        

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

        # Generate a list of all fish that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fish_list)
        
        # Loop through each colliding fish, remove it, and add to the score.
        if len(hit_list) > 0:
            for fish in hit_list:
                if self.can_eat(fish) == True:
                    fish.remove_from_sprite_lists()
                    self.increase_size(fish)
                    self.num_of_fish -= 1
                    fish.draw()
                else:
                    self.dead = True
                    self.on_finish

        # If the game is over
        if self.num_of_fish == 0:
            self.dead = False
            self.on_finish

        # Generate a list of all powerups that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.powerup_list)
        
        # Loop through each colliding powerup and remove it.
        for powerup in hit_list:
            if powerup.typeoffish.type == "size":
                for x in range(3):
                    self.increase_size("Powerup")
            powerup.remove_from_sprite_lists()

    def increase_size(self,fish):
        global SPRITE_SCALING_PLAYER
        self.player_sprite._scale += .05
        self.player_sprite._height += .05
        self.player_sprite._width += .05

        # Change score
        if fish == "Powerup":
            self.score += 1
        else:
            self.score += fish.typeoffish.size
        
        # Redraw everything
        self.all_sprites_list.draw()
    
    def on_finish(self):
        if self.dead == True:
            self.score = 0
        arcade.close_window()

    def can_eat(self,fish):
        if fish.typeoffish.size > self.score:
            return False
        else:
            return True


def main():
    window = MyGame()
    window.setup()
    arcade.run()