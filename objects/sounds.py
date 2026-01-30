from pathlib import Path
import pygame

BASE = Path(__file__).resolve().parent.parent
SOUNDS_DIR = BASE / "soundeffects"

class Sounds:

    def __init__(self):
        self.dmg_sound = pygame.mixer.Sound(SOUNDS_DIR/"damage_sound.mp3")
        self.shooting_sound = pygame.mixer.Sound(SOUNDS_DIR/"shoot.wav")