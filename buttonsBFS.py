from collections import deque


class State:
    def __init__(self, grid, shapes, colours, unpressable):
        self.grid = grid
        self.shapes = shapes
        self.colours = colours
        self.unpressable = unpressable

    def __hash__(self):
        return hash((tuple(map(tuple, self.grid)), tuple(map(tuple, self.shapes)),
                     tuple(map(tuple, self.colours)), tuple(map(tuple, self.unpressable))))


class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class ButtonsSolver:
    def __init__(self, max_depth=1000):
        self.visited_states = set()
        self.max_depth = max_depth
        self.pressed_buttons = set()

    def solve(self, startingState):
        queue = deque([(startingState, 0, [])])

        while queue:
            state, depth, moves = queue.popleft()

            if depth > self.max_depth:
                return None

            if self.isPuzzleComplete(state):
                button_count = len(moves)  # Number of buttons pressed
                button_presses = []
                for move in moves:
                    button_presses.append((move.col, move.row))

                return "\nSolution: " + "\nNumber of moves: " + str(
                    button_count) + "\nButtons pressed will be presented as (column, row) with index's starting at zero\nand zero, zero being the top left tile of the game." + "\nButtons Pressed: " + str(button_presses)

            self.visited_states.add(hash(state))
            for move in self.findNewMoves(state):
                resulting_state = self.makeMove(state, move)

                if hash(resulting_state) not in self.visited_states:
                    queue.append((resulting_state, depth + 1, moves + [move]))

        return None

    def isPuzzleComplete(self, state):
        for row in state.grid:
            for button in row:
                if button:
                    return False
        return True

    def findNewMoves(self, state):
        possible_moves = set()

        for row in range(len(state.grid)):
            for col in range(len(state.grid[row])):
                if state.grid[row][col] and not state.unpressable[row][col]:
                    possible_moves.add(Move(row, col))

        return possible_moves

    def makeMove(self, state, move):
        row = move.row
        col = move.col

        new_grid = [list(row) for row in state.grid]
        new_grid[row][col] = not new_grid[row][col]

        if not state.unpressable[row][col]:
            shape = state.shapes[row][col]
            color = state.colours[row][col]

            for j in range(len(state.grid[row])):
                if not state.unpressable[row][j]:
                    if state.shapes[row][j] == shape or state.colours[row][j] == color:
                        new_grid[row][j] = not new_grid[row][j]

            for i in range(len(state.grid)):
                if not state.unpressable[i][col]:
                    if state.shapes[i][col] == shape or state.colours[i][col] == color:
                        new_grid[i][col] = not new_grid[i][col]

        new_state = State(new_grid, state.shapes,
                          state.colours, state.unpressable)
        return new_state


def startingState(levelNo):
    if levelNo == 8:
        grid = [
            [False, False, False, False, False],
            [False, False, False, True, False],
            [False, False, False, False, False],
            [False, True, False, False, False],
            [False, False, False, False, False]
        ]

        colours = [
            ['A', 'A', 'A', 'A', 'A'],
            ['B', 'B', 'B', 'B', 'B'],
            ['C', 'C', 'C', 'C', 'C'],
            ['D', 'D', 'D', 'D', 'D'],
            ['E', 'E', 'E', 'E', 'E']
        ]

        shapes = [
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P']
        ]
        unpressable = [
            [True, True, True, True, True],
            [True, False, False, False, True],
            [True, False, True, False, True],
            [True, False, False, False, True],
            [True, True, True, True, True]
        ]

    elif levelNo == 17:
        grid = [
            [False, False, False, False, False],
            [True, False, False, False, True],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, True, False, False]
        ]

        colours = [
            ['Z', 'Z', 'Z', 'Z', 'Z'],
            ['A', 'Z', 'Z', 'Z', 'F'],
            ['B', 'B', 'Z', 'E', 'E'],
            ['Z', 'C', 'C', 'C', 'Z'],
            ['Z', 'Z', 'D', 'Z', 'Z']
        ]

        shapes = [
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P']
        ]

        unpressable = [
            [True, True, True, True, True],
            [False, True, True, True, False],
            [False, False, True, False, False],
            [True, False, False, False, True],
            [True, True, False, True, True]
        ]

    elif levelNo == 24:
        grid = [
            [False, True, True, True, False],
            [False, False, True, True, False],
            [False, False, False, True, True],
            [False, False, False, False, True],
            [False, False, False, False, False]
        ]

        colours = [
            ['A', 'A', 'A', 'A', 'A'],
            ['B', 'B', 'B', 'B', 'B'],
            ['C', 'C', 'C', 'C', 'C'],
            ['D', 'D', 'D', 'D', 'D'],
            ['E', 'E', 'E', 'E', 'E']
        ]

        shapes = [
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P']
        ]
        unpressable = [
            [True, False, False, False, True],
            [True, True, False, False, True],
            [True, True, True, False, False],
            [True, True, True, True, False],
            [True, True, True, True, True]
        ]

    return State(grid, shapes, colours, unpressable)


def printSol(level):
    solver = ButtonsSolver()
    startState = startingState(level)
    solution = solver.solve(startState)

    if solution:
        print(solution)
    else:
        print("No solution found.")


printSol(17)
