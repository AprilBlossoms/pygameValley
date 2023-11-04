class State:
    def __init__(self, game_manager, name):
        self.game_manager = game_manager
        self.name = name
        self.prev_state = None

    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game_manager.state_stack) > 1:
            self.prev_state = self.game_manager.state_stack[-1]
        self.game_manager.state_stack.append(self)

    def exit_state(self):
        self.game_manager.state_stack.pop()