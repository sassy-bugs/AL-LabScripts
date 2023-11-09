from collections import deque

class MonkeyBananaProblem:
    def __init__(self, monkey_position, chair_position, banana_position, path=None):
        self.monkey_position = monkey_position
        self.chair_position = chair_position
        self.banana_position = banana_position
        self.path = path if path is not None else []

    def is_goal_state(self):
        return self.monkey_position == self.banana_position

    def move_monkey(self, new_position):
        self.monkey_position = new_position
        self.path.append(f"Take {'right' if new_position > self.monkey_position else 'left'}")

    def move_chair(self, new_position):
        self.chair_position = new_position
        self.path.append(f"Move chair {'right' if new_position > self.chair_position else 'left'}")

    def climb_chair(self):
        self.monkey_position = self.chair_position
        self.path.append("Climb chair")

    def actions(self):
        possible_actions = []
        if self.monkey_position < self.banana_position:
            possible_actions.append("Take right")
        if self.monkey_position > self.chair_position:
            possible_actions.append("Take left")
        if self.monkey_position == self.chair_position and self.chair_position < self.banana_position:
            possible_actions.append("Climb chair")
            possible_actions.append("Move chair right")
        return possible_actions

def solve_monkey_banana_problem(initial_state):
    frontier = deque([initial_state])
    explored = set()

    while frontier:
        current_state = frontier.popleft()

        if current_state.is_goal_state():
            return current_state.path

        explored.add((current_state.monkey_position, current_state.chair_position, current_state.banana_position))

        for action in current_state.actions():
            new_state = MonkeyBananaProblem(
                current_state.monkey_position,
                current_state.chair_position,
                current_state.banana_position,
                list(current_state.path)
            )

            if action == "Take right":
                new_state.move_monkey(current_state.monkey_position + 1)
            elif action == "Take left":
                new_state.move_monkey(current_state.monkey_position - 1)
            elif action == "Climb chair":
                new_state.climb_chair()
            elif action == "Move chair right":
                new_state.move_chair(current_state.chair_position + 1)

            if (new_state.monkey_position, new_state.chair_position, new_state.banana_position) not in explored:
                frontier.append(new_state)

    return None

if __name__ == "__main__":
    initial_state = MonkeyBananaProblem(monkey_position=1, chair_position=4, banana_position=3)
    
    result = solve_monkey_banana_problem(initial_state)

    if result is not None:
        print("Steps to reach the banana:")
        for step in result:
            print(step)
    else:
        print("The monkey could not reach the banana.")
