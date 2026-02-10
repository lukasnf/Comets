import pygame
# Import the game objects
import objects.sounds as sound
from objects.highscore import Highscore
from objects.titlescreen import Titlescreen
from objects.endscreen import Endscreen
from objects.leaderboard import Leaderboard
import objects.game as Game


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    # window size in pixels: this game uses x-y coordinates like computer screens, not like math!
    # x=0, y=0 is top left corner, positive y is down, positive x is right
    #DISPLAY_WIDTH = 700
    #DISPLAY_HEIGHT = 700    
    
    # frame per second
    FPS = 50
    # angle rotation speed
    THETA = 6
    # scales how fast the spaceship accelerates
    THRUST = .3
    # initiate maximum speed
    MAX_SPEED = 10
    # Bullet speed
    B_SPEED = MAX_SPEED + 5
    # Cooldown between the shots
    SHOT_COOLDOWN = .2 # in s
    # Cooldown which allows to take damage
    DMG_COOLDOWN = .5 # in s
    # Maximum spaceship hp
    MAX_HP = 210
    # obtained damage
    DAMAGE = MAX_HP//3

    current_shot = 0
    current_dmg = 0
    
    # create the main screen
    #surface = pygame.display.set_mode(size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    DISPLAY_WIDTH, DISPLAY_HEIGHT = surface.get_size()
    

    #setting up state machine:
    state = "title"

    #setting up titlescreen
    title_screen = Titlescreen(DISPLAY_WIDTH, DISPLAY_HEIGHT)

    #setting up endscreen
    end_screen = Endscreen(DISPLAY_WIDTH, DISPLAY_HEIGHT)

    #setting up leaderboard
    leaderboard = Leaderboard(DISPLAY_WIDTH, DISPLAY_HEIGHT)

    # initiate sounds
    sounds = sound.Sounds()

    # initialize the clock for FPS calculation
    clock = pygame.time.Clock()

    # enter the infinite game loop
    print(f"entering game loop")
    running = True 
    cheat = False
   
    game = None

    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game when the window is closed

            if state == "title":
                new_state = title_screen.handle_event(event)
                if new_state == "play":
                    game = Game.Game(DISPLAY_HEIGHT, DISPLAY_WIDTH)
                    end_screen.player_name.set("")

                    move_up = False
                    rotate_left = False
                    rotate_right = False
                    shoot = False
                    cheat = False
                

                    state = "play"

            
                        
            elif state == "play":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        move_up = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        rotate_left = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        rotate_right = True
                    if event.key == pygame.K_SPACE:
                        shoot = True
                    if event.key == pygame.K_n:
                        cheat = True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        move_up = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        rotate_left = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        rotate_right = False
                    if event.key == pygame.K_SPACE:
                        shoot = False
                    if event.key == pygame.K_n:
                        cheat = False

            elif state == "endscreen":
                new_state = end_screen.handle_event(event)
                if new_state == "leaderboard":
                    hs = Highscore()
                    hs.load_highscore()
                    hs.write_highscore(end_screen.player_name.text_text, game.score)
                    leaderboard = Leaderboard(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                    state = "leaderboard"
            
            elif state == "leaderboard":
                new_state = leaderboard.handle_event(event)
                if new_state == "title":
                    state = "title"


        # Clear the screen by filling it with black color
        surface.fill(pygame.Color("black"))
        #rendering screen
        if state == "title":
            title_screen.draw(surface)
        elif state == "play":
            game.update_game(surface, rotate_right, rotate_left, move_up, shoot, cheat)
            cheat = False
            if game.gameover:
                state = "endscreen"
                continue
        elif state == "endscreen":
            end_screen.draw(surface)
        elif state == "leaderboard":
            leaderboard.draw(surface)        
       

        # Normal game behavior
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.d