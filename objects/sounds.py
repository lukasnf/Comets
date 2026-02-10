from pathlib import Path
import pygame

BASE = Path(__file__).resolve().parent.parent
SOUNDS_DIR = BASE / "soundeffects"

class Sounds:
    """
    Manager class for loading and storing all ingame sounds.
    It requires audio files placed in the soundeffects folder.
    """
    def __init__(self):
        """
        Initializes sounds by loading the audio files.
        It requies the initialization of pygame.mixer.

         Attributes:
            dmg_sound: sound played, if player takes damage.
            shooting_sound: sound played, if player shoots projectiles.
            item_pickup: sound played, if an ingame item is obtained.
        """
        self.dmg_sound = pygame.mixer.Sound(SOUNDS_DIR/"damage_sound.mp3")
        self.shooting_sound = pygame.mixer.Sound(SOUNDS_DIR/"shoot.wav")
        self.item_pickup = pygame.mixer.Sound(SOUNDS_DIR/"item_pickup.mp3")