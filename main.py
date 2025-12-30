import pygame

# Import the game objects
import objects.spaceship as spaceship
import objects.asteroids as asteroids
import objects.ufo as ufo
import objects.projectile as projectile
import time


if __name__ == "__main__":
    pygame.init()

    # window size in pixels: this game uses x-y coordinates like computer screens, not like math!
    # x=0, y=0 is top left corner, positive y is down, positive x is right
    DISPLAY_WIDTH = 1000
    DISPLAY_HEIGHT = 1000

    # frame per second
    FPS = 50
    THETA = 7
    THRUST = 0.4
    MAX_SPEED = 10
    B_SPEED = MAX_SPEED + 5
    SHOT_COOLDOWN = 0.4 # in s
    current_shot = 0
    
    # create the main screen
    surface = pygame.display.set_mode(size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))

    #Mainscreen mit Start, muss beginnen wenn Spieler Start drückt
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
    ship = spaceship.Spaceship(coordinates= [(440,770),(455,765),(470,770),(455,730)], color= "hotpink", width= 0)

    # Initialize asteroids
    flying_asteroids = asteroids.Asteroids(4, 2, DISPLAY_HEIGHT, DISPLAY_WIDTH, 5)

    # Initialize ufo Handler
    ufo_handler = ufo.Ufo_Handler(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)
    
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

        # Draw and move game objects
        ship.draw(surface)
        ship.center()


        flying_asteroids.cyclic_boundary_condition()
        flying_asteroids.collision_detection()
        flying_asteroids.hit_detection(bullets)
        for aster in flying_asteroids.collection:
            aster.move()
            aster.draw(surface)


        # Spaceship control
        if rotate_right:
            ship.rotate(THETA)
        elif rotate_left:
            ship.rotate(-THETA)
            
        if move_up:
            ship.velocity += ship.direction * THRUST 
            if ship.velocity.length() > MAX_SPEED:
                ship.velocity = ship.velocity.normalize() * MAX_SPEED
        else:
            ship.deaccelerate()
        
        if shoot:
            init_shot = time.time()
            if abs(init_shot - current_shot) >= SHOT_COOLDOWN:
                projectiles = projectile.Projectile(pos= ship.coordinates[-1], direction= ship.direction, speed= B_SPEED ,radius= 2, color= "blue")
                bullets.append(projectiles)
                current_shot = time.time()

        # remove those bullets that has hit something or left the game window
        bullets = [bullet for bullet in bullets if not bullet.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT) and not bullet.hit]
        for bullet in bullets:
            bullet.move()
            bullet.draw(surface)
    
        ship.move()
        ship.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT)

        ufo_handler.check_period()
        ufo_handler.move_ufo()
        ufo_handler.draw_ufo(surface)
        
        # Normal game behavior
        pygame.time.wait(1)  # slow things down by waiting 1 millisecond
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.