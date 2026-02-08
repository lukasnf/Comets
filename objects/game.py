import objects.spaceship as spaceship
import objects.asteroids as asteroids
import objects.ufo as ufo
import objects.projectile as projectile
import objects.items as item
import objects.sounds as sound
from objects.text import Text
import random
import time
import pygame

# angle rotation speed
THETA = 6
# scales how fast the spaceship accelerates
THRUST = .3
# Cooldown which allows to take damage
DMG_COOLDOWN = .5 # in s
# initiate maximum speed
MAX_SPEED = 10
# Bullet speed
B_SPEED = MAX_SPEED + 5
# Maximum spaceship hp
MAX_HP = 210
# obtained damage
DAMAGE = MAX_HP//3
# Cooldown between the shots
SHOT_COOLDOWN = .2 # in s

class Game:

    def __init__(self, display_height, display_width):
        self.display_height = display_height
        self.display_width = display_width
        self.level_label = Text("Level 1", 30, "white", self.display_width - 75, self.display_height*.1)
        self.score_text = Text('0'.zfill(6), 35, "white", display_width*0.1, display_height*0.1)
        # Initialize Healthbar 
        self.health_bar = spaceship.Healthbar(pos= (self.score_text.text_x, self.score_text.text_y + self.score_text.text_size), height= 20, max_hp= MAX_HP) 
        self.level = 1
        self.config_Level()
        self.ship = spaceship.Spaceship(color="hotpink", width=0)
        self.ufo_handler = ufo.Ufo_Handler(display_width, display_height, 1)
        self.bullets = []
        self.ac_items = []
        # List of all item names
        self.item_names = ["Heart_Item", "Rapid_Fire_Item"]
        # List of all item classes
        self.item_classes = [item.Heart_Item, item.Rapid_Fire_Item]
        # Initialize Healthbar 
        self.health_bar = spaceship.Healthbar(pos= (self.score_text.text_x, self.score_text.text_y + self.score_text.text_size), height= 20, max_hp= MAX_HP) 
        # initiate sounds
        self.sounds = sound.Sounds()
        self.current_shot = 0
        self.current_dmg = 0
        self.score = 0
        self.gameover = False
        


    def config_Level(self):
        self.score = 0
        self.health_bar.hp = self.health_bar.max_hp
        match self.level:
            case 1:
                self.flying_asteroids = asteroids.Asteroids(max_number= 2,min_number= 2, window_height= self.display_height, 
                                           window_width= self.display_width, max_speed=2)
            case 2:
                self.flying_asteroids = asteroids.Asteroids(max_number= 4,min_number= 3, window_height= self.display_height, 
                                           window_width= self.display_width, max_speed=4)
                self.item_names.extend(["Extra_Point_Item", "Speed_Item"])
                self.item_classes.extend([item.Extra_Point_Item, item.Speed_Item])
            case 3:
                self.flying_asteroids = asteroids.Asteroids(max_number= 6,min_number= 5, window_height= self.display_height, 
                                           window_width= self.display_width, max_speed=4)
                self.item_names.extend(["Feather_Item", "Shield_Item"])
                self.item_classes.extend([item.Feather_Item, item.Shield_Item])

    def next_level(self):
        self.level += 1
        self.level_label.set(f"Level {self.level}")
        self.config_Level()

    def update_game(self, surface, rotate_right, rotate_left, move_up, shoot, cheat):
        #* Spaceship Control
            # Damage control
            if self.ship.check_collision(self.flying_asteroids.collection, self.bullets) and self.ship.alive:
                init_dmg = time.time()
                if abs(self.current_dmg - init_dmg) >= DMG_COOLDOWN:
                    self.sounds.dmg_sound.play()
                    self.health_bar.hp -= DAMAGE
                    self.ship.check_health(self.health_bar.hp)
                    self.current_dmg = time.time()
            else:
                self.ship.draw(surface)
                # Spaceship rotation logic
            if rotate_right:
                self.ship.rotate(THETA)
            elif rotate_left:
                self.ship.rotate(-THETA)
                # Spaceship acceleration    
            if move_up:
                self.ship.velocity += self.ship.direction * THRUST 
                if self.ship.velocity.length() > MAX_SPEED:
                    self.ship.velocity = self.ship.velocity.normalize() * MAX_SPEED
            else:
                self.ship.decelerate()

            self.ship.move()
            self.ship.check_window(self.display_width, self.display_height)
            # Shooting control, with shoot cooldown
            if shoot and self.ship.alive:
                init_shot = time.time()
                if abs(self.current_shot - init_shot) >= SHOT_COOLDOWN:
                    self.sounds.shooting_sound.play()
                    projectiles = projectile.Projectile(self.ship.coordinates[-1], self.ship.direction, 
                                                        B_SPEED, "ship" ,radius= 2, color= "cyan")
                    self.bullets.append(projectiles)
                    self.current_shot = time.time()
            
            if not self.ship.alive:
                self.gameover = True

        #* Asteroids Control
            self.flying_asteroids.cyclic_boundary_condition()
            self.flying_asteroids.collision_detection()
            hit_list = self.flying_asteroids.hit_detection(self.bullets)
            for aster in self.flying_asteroids.collection:
                aster.move()
                aster.draw(surface)

            if len(self.flying_asteroids.collection) == 0 or cheat:
                self.next_level()
                return
            
         #* Bullet & Item control
         #* Ufo control
            self.ufo_handler.check_period()
            if self.ufo_handler.ufo != None:      
                self.ufo_handler.draw_ufo(surface)
                if self.ufo_handler.ufo.shoot():
                    self.bullets.append(self.ufo_handler.generate_projectile(self.ship))
                self.ufo_handler.move_ufo()
                  
         #increase of score:    
            for asteroid in hit_list:
                points = [20, 50, 100]  # points for level 0, 1, 2 asteroids

                self.score += points[asteroid.level]
                self.score_text.set(str(self.score).zfill(6))
            
            for bullet in self.bullets:
                bullet.move()
                bullet.draw(surface)
                if bullet.hit:
                    item_exists = any(type(i).__name__ in self.item_names for i in self.ac_items)
                    if random.randint(1,5) == 5 and not item_exists:
                        random_item = random.choice(self.item_classes)
                        current_item = random_item(bullet.pos, bullet.direction, speed= 2)
                        self.ac_items.append(current_item)

            for active_item in self.ac_items:
                active_item.draw(surface)
                active_item.move()           
                if active_item.check_collision(self.ship.coordinates):
                    self.sounds.dmg_sound.play()

            # only keep the items for their spawn time
            self.ac_items = [active_item for active_item in self.ac_items if pygame.time.get_ticks() - active_item.spawn_time < active_item.duration
                         and not active_item.hit]
            
            # remove those bullets that have hit something or left the game window
            self.bullets = [bullet for bullet in self.bullets if not bullet.check_window(self.display_width, self.display_height) and not bullet.hit]

            # draw score and health bar
            self.score_text.draw(surface) #draws score on surface
            self.health_bar.draw(surface) #draws healthbar on surface
            self.level_label.draw(surface)


        