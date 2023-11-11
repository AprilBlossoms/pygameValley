from pygame import Vector2

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (245, 186, 218)

FARM_LAYERS = {
    'ground': 0,
    'paths/hills/fence': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'plants and rocks': 5,
    'buildings': 6,
    'ground plant': 7,
    'main': 8,
    'house top': 9,
    'rain drops': 10
}
FARMHOUSE_LAYERS = {
    'ground': 0,
    'furniture floor': 1,
    'furniture': 2,
    'main': 3
}
PLAYER_TOOL_OFFSET = {
    'left': Vector2(-50, 10),
    'right': Vector2(50, 10),
    'up': Vector2(0, -15),
    'down': Vector2(0, 30)
}

GROW_SPEED = {
    'carrot': 1,
    'strawberry': 0.8
}