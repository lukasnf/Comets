import pygame

# Import the game objects
import objects.spaceship as spaceship
import objects.asteroids as asteroids


if __name__ == "__main__":
    pygame.init()

    # window size in pixels: this game uses x-y coordinates like computer screens, not like math!
    # x=0, y=0 is top left corner, positive y is down, positive x is right
    DISPLAY_WIDTH = 1000
    DISPLAY_HEIGHT = 1000

    # frame per second
    FPS = 50

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

    # Create game objects before entering the loop

    # Initialize spaceship
    ship = spaceship.Spaceship(
        coordinates= [(440,470),(455,465),(470,470),(455,430)],direction= (0,-1), color= "white", speed= 10, width= 1
    )

    # Initialize asteroid
    asteroid = asteroids.Asteroid(
        radius=30, x=200, y=200, dx=1, dy=0, speed=2, color="green"
    )

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


        # Clear the screen by filling it with black color
        surface.fill(pygame.Color("black"))

        # Draw game objects
        ship.draw(surface)
        asteroid.draw(surface)

        # Spaceship control
        if move_up:
            ship.move()
            ship.rotate()
        

        # Move asteroid
        asteroid.move()

        # Simple boundary check to reset asteroid position
        if asteroid.x > DISPLAY_WIDTH:
            asteroid = asteroids.Asteroid(
                radius=30, x=0, y=200, dx=1, dy=0, speed=2, color="red"
            )
        

        # Normal game behavior
        pygame.time.wait(1)  # slow things down by waiting 1 millisecond
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Call the quit() method outside the while loop to end the application.
