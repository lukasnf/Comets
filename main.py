import pygame

# Import the game objects
import objects.spaceship as spaceship
import objects.asteroids as asteroids


if __name__ == "__main__":
    pygame.init()

    # window size in pixels: this game uses x-y coordinates like computer screens, not like math!
    # x=0, y=0 is top left corner, positive y is down, positive x is right
    DISPLAY_WIDTH = 700
    DISPLAY_HEIGHT = 700

    # frame per second
    FPS = 50
    THETA = 7
    
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
    rotate_right =  False

    # Create game objects before entering the loop

    # Initialize spaceship
    ship = spaceship.Spaceship(
        coordinates= [(440,770),(455,765),(470,770),(455,730)],direction= (0,-1), color= "hotpink", speed= 0, width= 0
    )

    # Initialize asteroids
    flying_asteroids = asteroids.Asteroids(4, 2, DISPLAY_HEIGHT, DISPLAY_WIDTH, 10)


    # Game loop
    while running == True:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game when the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move_up = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotate_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rotate_left = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rotate_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rotate_right = False


        # Clear the screen by filling it with black color
        surface.fill(pygame.Color("black"))

        # Draw and move game objects
        ship.draw(surface)
        ship.center()
        flying_asteroids.delete_useless_asteroids()
        flying_asteroids.cyclic_boundary_condition()
        flying_asteroids.collision_detection()
        for aster in flying_asteroids.collection:
            aster.move()
            aster.draw(surface)


        # Spaceship control
        if move_up:
            if ship.speed < 10:
                ship.speed += 0.8
        else:
            ship.deaccelerate()
        if rotate_right:
            ship.rotate(THETA)
        elif rotate_left:
            ship.rotate(-THETA)

        ship.move()
        ship.check_window(DISPLAY_WIDTH,DISPLAY_HEIGHT)
        
        # Normal game behavior
        pygame.time.wait(1)  # slow things down by waiting 1 millisecond
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.
