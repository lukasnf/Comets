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
import time
import random

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    # window size in pixels: this game uses x-y coordinates like computer screens, not like math!
    # x=0, y=0 is top left corner, positive y is down, positive x is right
    DISPLAY_WIDTH = 1000
    DISPLAY_HEIGHT = 1000    
    
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
    surface = pygame.display.set_mode(size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    
    #setting up titlescreen
    title_screen = True
    title = Text("ASTEROIDS", 80, "white", DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.35)
    press_key = Text("Press ENTER to START game", 40, "white", DISPLAY_WIDTH*0.5, DISPLAY_HEIGHT*0.66)

    #setting up endscreen
    end_screen = False
    game_over_start = pygame.time.get_ticks()
    game_over = Text("GAME OVER", 45, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.25)
    enter_name = Text("Enter your NAME", 40, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.38)
    player_name = Text("", 50, "white", DISPLAY_WIDTH*.5, DISPLAY_HEIGHT*.5)
    
    #setting up score-counter
    score = 0
    score_text = Text(str(score).zfill(6), 35, "white", DISPLAY_WIDTH*0.1, DISPLAY_HEIGHT*0.1)

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
    # Create game objects before entering the loop
    
    # Initialize spaceship
    ship = spaceship.Spaceship(color= "hotpink", width= 0)

    # Initialize asteroids
    flying_asteroids = asteroids.Asteroids(max_number= 10,min_number= 2, window_height= DISPLAY_HEIGHT, 
                                           window_width=DISPLAY_WIDTH, max_speed=5)
    
    # Initialize ufo Handler
    ufo_handler = ufo.Ufo_Handler(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)

    # Initialize Healthbar 
    health_bar = spaceship.Healthbar(pos= (score_text.text_x, score_text.text_y), height= 20, max_hp= MAX_HP) 

    # Projectile list
    bullets = []
    # List of active items
    ac_items = []
    # List of all item names
    item_names = ["Heart_Item", "Shield_Item", "Rapid_Fire_Item", "Extra_Point_Item", "Feather_Item", "Speed_Item"]
    # List of all item classes
    item_classes = [item.Heart_Item, item.Shield_Item, item.Rapid_Fire_Item, item.Extra_Point_Item, item.Feather_Item, item.Speed_Item]

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
                    game = Game.Game(DISPLAY_HEIGHT, DISPLAY_WIDTH, score_text)
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

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    rotate_left = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    rotate_right = False
                if event.key == pygame.K_SPACE:
                    shoot = False

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
#        else:
#
#            score_text.draw(surface) #draws score on surface
#            health_bar.draw(surface) #draws healthbar on surface

            
#        #* Spaceship Control
#            # Damage control
#            if ship.check_collision(flying_asteroids.collection, bullets) and ship.alive:
#                init_dmg = time.time()
#                if abs(current_dmg - init_dmg) >= DMG_COOLDOWN:
#                    sounds.dmg_sound.play()
#                    health_bar.hp -= DAMAGE
#                    ship.check_health(health_bar.hp)
#                    current_dmg = time.time()
#            else:
#                ship.draw(surface)
#                # Spaceship rotation logic
#            if rotate_right:
#                ship.rotate(THETA)
#            elif rotate_left:
#                ship.rotate(-THETA)
#                # Spaceship acceleration    
#            if move_up:
#                ship.velocity += ship.direction * THRUST 
#                if ship.velocity.length() > MAX_SPEED:
#                    ship.velocity = ship.velocity.normalize() * MAX_SPEED
#            else:
#                ship.decelerate()
#
#            ship.move()
#            ship.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT)
#
#            # Shooting control, with shoot cooldown
#            if shoot and ship.alive:
#                init_shot = time.time()
#                if abs(current_shot - init_shot) >= SHOT_COOLDOWN:
#                    sounds.shooting_sound.play()
#                    projectiles = projectile.Projectile(ship.coordinates[-1], ship.direction, 
#                                                        B_SPEED, "ship" ,radius= 2, color= "cyan")
#                    bullets.append(projectiles)
#                    current_shot = time.time()
#
#        #* Asteroids Control
#            flying_asteroids.cyclic_boundary_condition()
#            flying_asteroids.collision_detection()
#            hit_list = flying_asteroids.hit_detection(bullets)
#            for aster in flying_asteroids.collection:
#                aster.move()
#                aster.draw(surface)
#
#
#         #* Bullet & Item control
#         #* Ufo control
#            ufo_handler.check_period()
#            if ufo_handler.ufo != None:      
#                ufo_handler.draw_ufo(surface)
#                if ufo_handler.ufo.shoot():
#                    bullets.append(ufo_handler.generate_projectile(ship))
#                ufo_handler.move_ufo()
#                  
#         #increase of score:    
#            for asteroid in hit_list:
#                points = [20, 50, 100]  # points for level 0, 1, 2 asteroids
#
#                score += points[asteroid.level]
#                score_text.set(str(score).zfill(6))
#            
#            for bullet in bullets:
#                bullet.move()
#                bullet.draw(surface)
#                if bullet.hit:
#                    item_exists = any(type(i).__name__ in item_names for i in ac_items)
#                    if random.randint(1,5) == 5 and not item_exists:
#                        random_item = random.choice(item_classes)
#                        current_item = random_item(bullet.pos, bullet.direction, speed= 2)
#                        ac_items.append(current_item)
#
#            # only keep the items for their spawn time
#            ac_items = [active_item for active_item in ac_items if pygame.time.get_ticks() - active_item.spawn_time < active_item.duration
#                         and not active_item.hit]
#            
#            for active_item in ac_items:
#                active_item.draw(surface)
#                active_item.move()           
#            
#            # remove those bullets that have hit something or left the game window
#            bullets = [bullet for bullet in bullets if not bullet.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT) and not bullet.hit]
        
#        if not ship.alive and not end_screen:
#            if game_over_start is None:
#                game_over_start = pygame.time.get_ticks()
#            game_over.draw(surface)      #transiotioning to the endscreen when spaceship dies
#            
#            if pygame.time.get_ticks() - game_over_start < 6000:
#                end_screen = True
        if game != None:
            game.update_game(surface, rotate_right, rotate_left, move_up, shoot)
            if game.gameover and not end_screen:
                if game_over_start is None:
                    game_over_start = pygame.time.get_ticks()
                game_over.draw(surface)      #transiotioning to the endscreen when spaceship dies

                if pygame.time.get_ticks() - game_over_start > 6000:
                    end_screen = True                
       

        # Normal game behavior
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.