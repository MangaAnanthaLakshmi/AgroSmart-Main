class RLAgent:
    def __init__(self):
        self.q_table = {}

    def choose_action(self, state):
        if state is None:
            raise ValueError(
                "RL Error: State(Environment) is missing. "
                "Reinforcement Learning requires a state to choose an action."
            )

        return "Fertilizer A"

    def update(self, state, action, reward, next_state):
        if reward is None:
            raise ValueError(
                "RL Error: Reward is missing. "
                "Reinforcement Learning cannot learn without a reward."
            )

        return "Q-table Updated"