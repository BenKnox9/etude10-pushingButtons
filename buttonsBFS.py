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
    def __init__(self):
        self.visited_states = set()
        self.pressed_buttons = set()

    def solve(self, startingState):
        # Create a queue filled with 3 value tuples.
        queue = deque([(startingState, 0, [])])

        while queue:
            # The three values in the queue are state, depth, and moves
            # state being the current state of the puzzle game, depth being the number of moves made so far,
            # and moves being the list of col and row values of the buttons which have been pressed so far, stored as a Move object.
            state, depth, moves = queue.popleft()
            print(moves)

            # If every button in the puzzle is pushed down, return the number of moves and the list of moves taken.
            print("depth: ", depth)
            if self.isPuzzleComplete(state):
                button_count = len(moves)
                button_presses = []
                for move in moves:
                    button_presses.append((move.col, move.row))

                arrayDescription = "\nButtons pressed will be presented as (column, row) with index's starting at zero.\nzero, zero being the top left tile of the game."
                return arrayDescription + "\nSolution:\n" + "Buttons Pressed: " + str(button_presses) + "\nNumber of moves: " + str(button_count)

            # Add current move to visited states
            self.visited_states.add(hash(state))

            # Make another move
            for move in self.findNewMoves(state):
                resulting_state = self.makeMove(state, move)

                if hash(resulting_state) not in self.visited_states:
                    queue.append((resulting_state, depth + 1, moves + [move]))

        return None

    """
    isPuzzleComplete
    Method which checks if the puzzle is finished. Checks if every tile is set to false. 

    @params: self, state
    @return: True if puzzle is complete, false if not
    """

    def isPuzzleComplete(self, state):
        for row in state.grid:
            for button in row:
                if button:
                    return False
        return True

    """
    findNewMoves
    Method which finds potential next moves. Checks the grid for any tiles which are currently set to True
    as these represent unpressed buttons.

    @params: self, state
    @return: a set of possible moves as (row, column)
    """

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

        shape = state.shapes[row][col]
        color = state.colours[row][col]

        # checks buttons which are the same shape or colour in the same column. If there is any, will reverse the state of that button.
        for i in range(len(state.grid)):
            if not state.unpressable[i][col]:
                if state.shapes[i][col] == shape or state.colours[i][col] == color:
                    new_grid[i][col] = not new_grid[i][col]

        # checks buttons which are the same shape or colour in the same row. If there is any, will reverse the state of that button.
        for j in range(len(state.grid[row])):
            if not state.unpressable[row][j]:
                if state.shapes[row][j] == shape or state.colours[row][j] == color:
                    new_grid[row][j] = not new_grid[row][j]

        new_state = State(new_grid, state.shapes,
                          state.colours, state.unpressable)
        return new_state


def startingState(levelNo):
    if levelNo == 8:
        # False if the button is pressed down, True if not
        grid = [
            [False, False, False, False, False],
            [False, False, False, True, False],
            [False, False, False, False, False],
            [False, True, False, False, False],
            [False, False, False, False, False]
        ]
        # each letter that matches is the same colour
        colours = [
            ['A', 'A', 'A', 'A', 'A'],
            ['B', 'B', 'B', 'B', 'B'],
            ['C', 'C', 'C', 'C', 'C'],
            ['D', 'D', 'D', 'D', 'D'],
            ['E', 'E', 'E', 'E', 'E']
        ]
        # each letter that matches is the same shape
        shapes = [
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P'],
            ['X', 'Y', 'Z', 'W', 'P']
        ]
        # Gets rid of unwanted tiles in the grid, True if the button is unpressable, or is a tile that is not in use in this puzzle
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
    elif levelNo == 19:
        grid = [
            [False, False, False, False, False],
            [False, False, False, False, True],
            [False, False, False, False, False],
            [True, False, False, False, False],
            [False, False, False, False, False]
        ]

        colours = [
            ['Z', 'Z', 'Z', 'Z', 'Z'],
            ['A', 'F', 'F', 'E', 'E'],
            ['A', 'Z', 'Z', 'Z', 'D'],
            ['B', 'B', 'C', 'C', 'D'],
            ['Z', 'Z', 'Z', 'Z', 'Z']
        ]

        shapes = [
            ['Q', 'Q', 'Q', 'Q', 'Q'],
            ['X', 'X', 'Y', 'Y', 'Z'],
            ['X', 'Q', 'Q', 'Q', 'Z'],
            ['X', 'S', 'S', 'W', 'W'],
            ['Q', 'Q', 'Q', 'Q', 'Q']
        ]
        unpressable = [
            [True, True, True, True, True],
            [False, False, False, False, False],
            [False, True, True, True, False],
            [False, False, False, False, False],
            [True, True, True, True, True]
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


def printSolution(level):
    solver = ButtonsSolver()
    startState = startingState(level)
    solution = solver.solve(startState)

    if solution:
        print(solution)
    else:
        print("No solution found.")


# Enter level number in printSol(). Currently the levels initialised are 8, 17, 19, 24
printSolution(17)
