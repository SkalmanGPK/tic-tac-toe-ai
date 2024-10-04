import random
class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=1.0, decay=0.999):
        self.q_table = {}
        self.alpha = alpha # Learning rate
        self.gamme = gamma # Discount factor
        self.epsilon = epsilon # Exploration rate
        self.decay = decay # Epsilon decay
    
    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)
    
    def choose_action(self, state, possible_actions):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(possible_actions)
        else:
            q_values = [self.get_q_value(state, action) for action in possible_actions]
            max_q = max(q_values)
            return possible_actions[q_values.index(max_q)]
    
    def update_q_table(self, state, action, reward, next_state, possible_next_actions):
        future_q_values = [self.get_q_value(next_state, a) for a in possible_next_actions]
        max_future_q = max(future_q_values) if future_q_values else 0
        old_q = self.get_q_value(state, action)
        new_q = old_q + self.alpha * (reward + self.gamme * max_future_q - old_q)
        self.q_table[(state, action)] = new_q
    
    def decay_epsilon(self):
        self.epsilon *= self.decay