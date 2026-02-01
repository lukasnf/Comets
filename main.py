import pygame
# Import the game objects
import objects.spaceship as spaceship
import objects.asteroids as asteroids
import objects.ufo as ufo
import objects.projectile as projectile
import objects.items as item
import objects.sounds as sound
from objects.text import text
import time
import random

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    # window size in pixels: this game uses x-y coordinates like computer screens, not like math!
    # x=0, y=0 is top left corner, positive y is down, positive x is right
    DISPLAY_WIDTH = 700
    DISPLAY_HEIGHT = 700
    
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
    title = text("ASTEROIDS", 80, "bad robots", "white", DISPLAY_WIDTH*0.253, DISPLAY_HEIGHT*0.35)
    press_key = text("Press ENTER to start game", 40, "Arial", "white", 150, 450)

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
    flying_asteroids = asteroids.Asteroids(max_number= 5,min_number= 2, window_height= DISPLAY_HEIGHT, 
                                           window_width=DISPLAY_WIDTH, max_speed=5)

    # Initialize ufo Handler
    ufo_handler = ufo.Ufo_Handler(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)

    # Initialize Healthbar 
    health_bar = spaceship.Healthbar(height= 20, max_hp= MAX_HP) 

    # Projectile list
    bullets = []

    # List of active items
    ac_items = []



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
                continue
                

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

        if title_screen:
            title.draw(surface)
            press_key.draw(surface)
        else:
            health_bar.draw(surface)
            # Draw and move game objects
            #* Spaceship Control
                # Damage control
            if ship.check_collision(flying_asteroids.collection, bullets):
                init_dmg = time.time()
                if abs(current_dmg - init_dmg) >= DMG_COOLDOWN :
                    sounds.dmg_sound.play()
                    health_bar.hp -= 25
                    current_dmg = time.time()
            else:
                ship.draw(surface)
                # Spaceship rotation logic
            if rotate_right:
                ship.rotate(THETA)
            elif rotate_left:
                ship.rotate(-THETA)
                # Spaceship acceleration    
            if move_up:
                ship.velocity += ship.direction * THRUST 
                if ship.velocity.length() > MAX_SPEED:
                    ship.velocity = ship.velocity.normalize() * MAX_SPEED
            else:
                ship.decelerate()
            ship.move()
            ship.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT)
                # Shooting control, with shoot cooldown
            if shoot:
                init_shot = time.time()
                if abs(current_shot - init_shot) >= SHOT_COOLDOWN:
                    sounds.shooting_sound.play()
                    projectiles = projectile.Projectile(ship.coordinates[-1], ship.direction, 
                                                        B_SPEED, "ship" ,radius= 2, color= "cyan")
                    bullets.append(projectiles)
                    current_shot = time.time()
            #* Asteroids Control
            flying_asteroids.cyclic_boundary_condition()
            flying_asteroids.collision_detection()
            flying_asteroids.hit_detection(bullets)
            for aster in flying_asteroids.collection:
                aster.move()
                aster.draw(surface)
            #* Bullet & Item control
            #* Ufo control
            ufo_handler.check_period()
            if ufo_handler.ufo != None:      
                ufo_handler.draw_ufo(surface)
                if ufo_handler.ufo.shoot():
                    bullets.append(ufo_handler.generate_projectile(ship))
                ufo_handler.move_ufo()
            for bullet in bullets:
                bullet.move()
                bullet.draw(surface)
                if bullet.hit:
                    if random.randint(0,5) == 5 and len(ac_items) != 1:
                        heart_item = item.Heart_Item(bullet.pos, bullet.direction, speed= 2)
                        spawn_time = pygame.time.get_ticks()
                        ac_items.append(heart_item)
                # only keep the items for ITEM_SPAWN_TIME
            ac_items = [active_item for active_item in ac_items if pygame.time.get_ticks() - spawn_time < active_item.spawn_time and 
                        not active_item.hit]
            for active_item in ac_items:
                active_item.draw(surface)
                active_item.move()
                # remove those bullets that have hit something or left the game window
            bullets = [bullet for bullet in bullets if not bullet.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT) and not bullet.hit]



        # Normal game behavior
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.