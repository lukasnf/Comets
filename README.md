# Comets

A remake of the arcade classic *Asteroids*, written in Python with Pygame.

![Gameplay](docs/gameplay.gif)
<img width="470" height="305" alt="comets" src="https://github.com/user-attachments/assets/63bd777e-b201-4a3b-b4e1-555fbefe43eb" />


## Features

- **Vector-based physics:** the ship accelerates, drifts and slows down through friction
- **Progressive levels:** asteroids split into smaller pieces when hit; later levels spawn more asteroids and UFOs that shoot back
- **Power-ups that spawn during play:**

| Item | Effect |
| :--- | :--- |
| Heart | Restores full health |
| Shield | Temporary invincibility |
| Rapid Fire | Shorter shooting cooldown |
| Extra Point | Bonus score |
| Feather | Slows down time |
| Speed *(debuff)* | Makes enemies faster |

- **Leaderboard** that saves high scores between sessions

## Technical Highlights

- Object-oriented structure with separate classes for ship, asteroids, UFOs, bullets and items
- 2D vector math for movement, rotation and friction
- Collision detection between all game objects
- Fixed-timestep game loop with level and state management (title screen, game, leaderboard)

<!-- Only keep the points that are actually true for your code, and add your own. -->

## Getting Started

```bash
git clone https://github.com/lukasnf/Comets.git
cd Comets
pip install -r requirements.txt
python main.py
```

Requires Python 3.10 or newer.

## Controls

| Action | Key |
| :--- | :--- |
| Accelerate | `W` / `↑` |
| Rotate left | `A` / `←` |
| Rotate right | `D` / `→` |
| Shoot | `Space` |
| Skip level (cheat) | `N` |
| Quit | `Esc` |

On the title screen, press `Enter` to start or `Space` to open the leaderboard.

## Fonts

The arcade font is not included for licensing reasons. The game falls back to a default font; for the original look, place a font file at `fonts/Arcade.ttf`.

## Project Structure

```
Comets/
├── main.py          # Entry point and game loop
├── ...              # Fill in your actual modules
├── docs/            # Screenshots and GIFs for this README
└── requirements.txt
```

## What I Learned
Comets was a three-person team project in my first semester at KIT, developed together with Oliver and Benjamin. I was mainly responsible for [z. B. the physics and collision system / the item system / the level logic].

Working as a team taught me to coordinate tasks and use Git collaboratively, with branches, merges and resolving conflicts. I also learned to structure a larger Python codebase into classes and modules so that three people could work on it in parallel.
## License

MIT, see [LICENSE](LICENSE).
