import pygame
# Import the game objects
import objects.spaceship as spaceship
import objects.asteroids as asteroids
import objects.ufo as ufo
import objects.projectile as projectile
import objects.items as item
import objects.sounds as sound
from objects.text import Text
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
    
    #setting up titlescreen
    title_screen = True
    title = Text("ASTEROIDS", 80, "white", DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.35)
    press_key = Text("Press ENTER to START game", 40, "white", DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.66)

    #setting up endscreen
    end_screen = False
    game_over_start = None
    game_over = Text("GAME OVER", 45, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.25)
    enter_name = Text("Enter your NAME:", 40, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.38)
    player_name = Text("", 50, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.5)

    #setting up leaderboard
    
    

    # initiate sounds
    sounds = sound.Sounds()

    # initialize the clock for FPS calculation
    clock = pygame.time.Clock()

    # enter the infinite game loop
    print(f"entering game loop")
    running = True
    move_up = False
    rotate_left = False
    rotate_right = False
    shoot = False 
    cheat = False
   
    game = None

    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game when the window is closed

            if title_screen:    #creating title screen
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        title_screen = False
                        game = Game.Game(DISPLAY_HEIGHT, DISPLAY_WIDTH)
            elif end_screen:
                player_name.input_text(event)
                        
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

        # Clear the screen by filling it with black color
        surface.fill(pygame.Color("black"))
        #rendering screen
        if title_screen:
            title.draw(surface)
            press_key.draw(surface)            
        elif end_screen:
            game_over.draw(surface)
            enter_name.draw(surface)
            player_name.draw(surface)
            #score_end = Text(str(game.score), 40, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.78)
            #score_end.draw(surface)
#        
        if game != None:
            game.update_game(surface, rotate_right, rotate_left, move_up, shoot, cheat)
            cheat = False
            if game.gameover and not end_screen:
                if game_over_start is None:
                    game_over_start = pygame.time.get_ticks()
                game_over.draw(surface)      #transiotioning to the endscreen when spaceship dies

                if pygame.time.get_ticks() - game_over_start > 3000:
                    end_screen = True                
       

        # Normal game behavior
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.d