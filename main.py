# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import GameCode as game
import FishEatFishHomepage as homepage
import EndScreen as ending

play = True

# Press the green button in the gutter to run the script.
def main():
    homepage.main()
    game.main(None)
    ending.main()

main()

# while play == True:
#     main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
