from game.game_state_manager import GameStateManager

game_manager = GameStateManager()

while game_manager.running:
    game_manager.manager_loop()
