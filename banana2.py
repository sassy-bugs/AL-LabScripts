from queue import Queue

def monkey_and_bananas():
    # Initialize the room and objects
    room = [['.' for _ in range(10)] for _ in range(10)]
    monkey_pos = (0, 0)
    chair_pos = (3, 3)
    banana_pos = (5, 5)
    x,y = monkey_pos
    room[x][y] = 'M'

    x,y = chair_pos
    room[x][y] = 'C'

    x,y = banana_pos
    room[x][y] = 'B'

    print("Initial state: ")
    for row in room:
        print(' '.join(row))

    # Define the sequence of moves (up, down, right, left)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    move_names = ['Down', 'Up', 'Right', 'Left']

    # Helper function to check if a move is valid
    def is_valid_move(x, y):
        return 0 <= x < 10 and 0 <= y < 10

    # Function to find a path from start to goal using BFS
    def find_path(start, goal):
        visited = set()
        queue = Queue()
        queue.put((start, []))  # Start node and its path

        while not queue.empty():
            node, path = queue.get()
            x, y = node

            if node == goal:
                return path  # Found a path

            visited.add(node)

            for ((dx, dy), move_name) in zip(moves, move_names):
                new_x, new_y = x + dx, y + dy
                new_node = (new_x, new_y)

                if is_valid_move(new_x, new_y) and new_node not in visited:
                    queue.put((new_node, path + [move_name]))

        return None  # No path found

    # Find the path for the monkey to reach the chair
    monkey_to_chair_path = find_path(monkey_pos, chair_pos)
    # print(monkey_to_chair_path)
    if monkey_to_chair_path is None:
        print("No path for monkey to reach the chair.")
        return

    # Move the monkey to the chair along the path
    for move_name in monkey_to_chair_path:
        print(f'Monkey moves {move_name} to reach the chair.')

    x,y = monkey_pos
    room[x][y] = '.'
    monkey_pos = chair_pos
    
    # # Move the chair to an adjacent cell of the banana
    monkey_to_banana_path = find_path(monkey_pos, banana_pos)

    if monkey_to_banana_path is None:
        print("No path for monkey to reach the banana.")
        return
    x,y = chair_pos
    room[x][y] = '.'
    monkey_pos=banana_pos
    chair_pos=banana_pos

    for move_name in monkey_to_banana_path:
        print(f'Monkey moves the chair {move_name} to reach the banana.')
    # Climb the chair
    print('Monkey climbs the chair')
    # Use the stick to get the bananas
    print('Monkey uses the stick to knock the bananas down')
    # Get the bananas
    x, y = banana_pos
    room[x][y] = 'X'  # Banana symbol
    print(f'Monkey grabs the bananas at ({x},{y})')
    # Print the room state
    print("Final State: ")
    for row in room:
        print(' '.join(row))
print('AGRIMA GUPTA - 11501012021')
# Run the monkey_and_bananas function
monkey_and_bananas()
