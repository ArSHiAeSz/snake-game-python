import pygame
import os
import tempfile
from project import spawn_food, load_highscore, save_highscore, SnakeGame

pygame.init()

def test_spawn_food_not_on_snake():
    snake = [(5,5), (5,6), (5,7)]
    food = spawn_food(snake)

    assert food not in snake
    assert isinstance(food, tuple)
    assert len(food) == 2

def test_save_and_load_highscore():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name

    save_highscore(15, path)
    score = load_highscore(path)

    assert score == 15

    os.remove(path)

def test_load_highscore_file_not_exists():
    score = load_highscore("file_does_not_exist.txt")
    assert score == 0

def test_game_reset():
    game = SnakeGame(None, None, None)

    game.score = 10
    game.game_over = True
    game.snake = [(1,1)]

    game.reset()

    assert game.score == 0
    assert game.game_over is False
    assert len(game.snake) == 3
