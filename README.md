# 🚀 Asteroids (Meteroids)

A modern, object-oriented Python remake of the classic arcade game "Asteroids", built with Pygame. 

Survive as long as possible by shooting asteroids, dodging UFOs, and collecting powerful items! The game features a complete state machine including a title screen, progressive difficulty levels, and a persistent leaderboard to track your high scores.

## ✨ Features
* **Physics-based Movement:** Realistic spaceship acceleration and friction using vector math.
* **Progressive Levels:** Asteroids split into smaller pieces when hit. Higher levels spawn more asteroids and introduce UFOs that shoot back.
* **Item System:** Collect dynamically spawning power-ups:
  * ❤️ **Heart:** Restores health to maximum.
  * 🛡️ **Shield:** Grants temporary invincibility.
  * 🔫 **Rapid Fire:** Significantly reduces shoot cooldown.
  * 🪙 **Extra Point:** Grants bonus score points.
  * 🪶 **Feather:** Slows down time (enemies move slower).
  * ⚡ **Speed:** Increases enemy speed (watch out!).
* **Leaderboard:** Persistent high score tracking using `pandas`, saved locally in a `.csv` file.

---

## ⚠️ Important Note on Assets (Sounds & Fonts)
To comply with licensing and keep the repository clean, **custom fonts and sound effects are not included** in this repository (they are excluded via `.gitignore`). 

**The game is fully playable without them!** It includes a built-in safety fallback:
* If the custom font is missing, the game automatically switches to the Pygame default system font.
* If sound files are missing, the game utilizes a `DummySound` class and runs completely silently without crashing.

**Want the full experience?**
If you want to play with the original assets, create the following folders in the root directory and add your own files:
* `fonts/Arcade.ttf`
* `soundeffects/damage_sound.mp3`
* `soundeffects/shoot.wav`
* `soundeffects/item_pickup.mp3`
* `soundeffects/weltall_musik.mp3`

---

## 🎮 Controls

| Action | Key(s) |
| :--- | :--- |
| **Accelerate** | `W` or `UP Arrow` |
| **Rotate Left** | `A` or `LEFT Arrow` |
| **Rotate Right** | `D` or `RIGHT Arrow` |
| **Shoot** | `SPACE` |
| **Skip Level (Cheat)**| `N` |
| **Quit Game** | `ESC` |

*On the Title Screen:* Press `ENTER` to start the game or `SPACE` to view the Leaderboard.

---

## 🛠️ Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Meteroids.git](https://github.com/YOUR_USERNAME/Meteroids.git)
   cd Meteroids
