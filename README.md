# 🚀 Comets

A Python remake of the classic arcade game "Asteroids", built with Pygame. 

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
To comply with licensing and keep the repository clean, **custom fonts are not included** in this repository (they are excluded via `.gitignore`). 

**Want the full experience?**
If you want to play with the original assets, create the following folders in the root directory and add your own files:
* `fonts/Arcade.ttf`
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

README made with Gemini.
