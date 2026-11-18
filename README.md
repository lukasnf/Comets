# Comets

A remake of the arcade classic *Asteroids*, written in Python with Pygame.

![Gameplay](docs/gameplay.gif)
<!-- Record a 5–10 s clip of the game and save it as docs/gameplay.gif -->

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

<!-- 2–3 sentences in your own words, e.g. what was hardest and how you solved it. -->

## License

MIT, see [LICENSE](LICENSE).
