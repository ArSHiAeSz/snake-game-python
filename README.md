# Snake Game (Python & Pygame)

🎮 A classic Snake Game implemented in Python using the Pygame library.

## Video Demo
▶️ https://youtu.be/20xWnYtRagw?si=bAfhn7BSTjxR2TDG

---

## Description
This project is a complete implementation of the classic Snake Game developed in Python with Pygame.
The player controls a snake using the keyboard, navigating it around the screen to eat food and grow longer.
Each time the snake eats food, the score increases and the game gradually becomes more challenging as the snake's speed increases.

The game ends when the snake collides with the wall or with its own body.
Additional features include pause and restart functionality, as well as persistent high score saving using a local file.

This project was originally developed as the final project for **CS50P (Harvard University)** and later refined as a polished, standalone Python game project.

---

## Features
- Keyboard-controlled snake movement
- Dynamic difficulty with increasing speed
- Persistent high score saving
- Pause and restart functionality
- Modular and readable code structure
- Unit testing using pytest

---

## Technologies Used
- Python 3
- Pygame
- Pytest
- File handling for persistent storage

---

## Project Structure

snake-game-pygame/
---
├── project.py # Main game logic
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── tests/
└── test_project.py # Unit tests (pytest)
---
## Team contributions 
This project was developed collaboratively:

👤 Arshia Eisazadeh
Implemented the main game logic and core SnakeGame class

Managed movement, collision detection, scoring, and speed scaling

Handled the main game loop and event-driven logic

👤 Amirali Nasiraii
Implemented helper functions (food spawning, high score handling)

Wrote unit tests using pytest

Prepared documentation and dependency files

---

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt

Run the game:

bash
Copy code
python project.py

 **Author
Arshia Eisazadeh
Python Developer | CS50P (Harvard)
