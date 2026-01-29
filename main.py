import pygame
# Import the game objects
import objects.spaceship as spaceship
import objects.asteroids as asteroids
import objects.ufo as ufo
import objects.projectile as projectile
import objects.items as item
import time

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
    DMG_COOLDOWN = 1 # in s
    # Maximum spaceship hp
    MAX_HP = 200

    current_shot = 0
    current_dmg = 0
    
    # create the main screen
    surface = pygame.display.set_mode(size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # get the shooting sound from soundeffects folder
    shooting_sound = pygame.mixer.Sound("soundeffects/shoot.wav")

    # damage sound from soundeffects folder
    dmg_sound = pygame.mixer.Sound("soundeffects/damage_sound.mp3")

    #Mainscreen mit Start, muss beginnen, wenn Spieler Start drückt
    #Game: Highscore, 20 pkt für groß, 50 pkt für mittel, 100 pkt für klein. Oben links angezeigt, darunter Leben


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
    flying_asteroids = asteroids.Asteroids(max_number= 4,min_number= 2, window_height= DISPLAY_HEIGHT, 
                                           window_width=DISPLAY_WIDTH, max_speed=5)

    # Initialize ufo Handler
    ufo_handler = ufo.Ufo_Handler(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)

    #Initialize Items:
    heart_item = item.Item(png= "heart pixel art 254x254.png")

    # Initialize Healthbar 
    health_bar = spaceship.Healthbar(height= 20, max_hp= MAX_HP) 

    # Projectile list
    bullets = []

    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game when the window is closed
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

        health_bar.draw(surface)
        # Draw and move game objects

        #* Spaceship Control
            # Damage control
        if ship.check_collision(flying_asteroids.collection):
            init_dmg = time.time()
            if abs(current_dmg - init_dmg) >= DMG_COOLDOWN :
                dmg_sound.play()
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
        
            # Shooting control, with shoot cooldown
        if shoot:
            init_shot = time.time()
            if abs(current_shot - init_shot) >= SHOT_COOLDOWN:
                shooting_sound.play()
                projectiles = projectile.Projectile(pos= ship.coordinates[-1], direction= ship.direction, 
                                                    speed= B_SPEED ,radius= 2, color= "cyan")
                bullets.append(projectiles)
                current_shot = time.time()

        ship.move()
        ship.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT)

        #* Asteroids Control
        flying_asteroids.cyclic_boundary_condition()
        flying_asteroids.collision_detection()
        flying_asteroids.hit_detection(bullets)
        for aster in flying_asteroids.collection:
            aster.move()
            aster.draw(surface)

        
        if any(bullet.hit for bullet in bullets):
            heart_item.draw(surface, bullet.pos)

        # remove those bullets that have hit something or left the game window
        bullets = [bullet for bullet in bullets if not bullet.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT) and not bullet.hit]
        
        for bullet in bullets:
            bullet.move()
            bullet.draw(surface)

        #* Ufo control
        ufo_handler.check_period()
        ufo_handler.move_ufo()
        ufo_handler.draw_ufo(surface)
        
        # Normal game behavior
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.