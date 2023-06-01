from collections import deque

"""
This script calculates the minimum number of moves that a game in pushingButtons.jar will take to complete using breadth first search. 
The script will also print the moves that you can follow to validate this result. Currently the code is only set up for 
levels 8, 17, 19 and 24, however if you want to check another level this can be done by adding to the startingState method. 
"""


class State:
    """ 
    Constructor method
    Method creates a state object
    """

    def __init__(self, grid, shapes, colours, unpressable):
        self.grid = grid
        self.shapes = shapes
        self.colours = colours
        self.unpressable = unpressable


class Move:
    """ 
    Constructor method
    Method creates a move object
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col


class ButtonsSolver:
    def __init__(self):
        self.visitedStates = set()

    """
    solve
    Method which will use breadth first search to explore different combinations of button presses. Once a combination of button presses
    is found which ends with a grid state of all false, output is returned.

    @params: self, startingState
    @return: result, the number of moves made, and the position of each button pressed
    """

    def solve(self, startingState):
        # Create a queue filled with 3 value tuples.
        queue = deque([(startingState, 0, [])])

        while len(queue) > 0:
            # The three values in the queue are state, depth, and moves
            # state being the current state of the game game, depth being the number of moves made so far,
            # and moves being the list of col and row values of the buttons which have been pressed so far, stored as a Move object.
            state, depth, moves = queue.popleft()

            # If every button in the game is pushed down, return the number of moves and the list of moves taken.
            if self.isGameComplete(state):
                buttonCount = len(moves)
                buttonPressesList = []
                for move in moves:
                    buttonPressesList.append((move.col, move.row))

                arrayDescription = "\nButtons pressed will be presented as (column, row) with index's starting at zero.\nzero, zero being the top left tile of the game."
                result = arrayDescription + "\nSolution:\n" + "Buttons Pressed: " + \
                    str(buttonPressesList) + \
                    "\nNumber of moves: " + str(buttonCount)
                return result

            # Add current state to visited states
            self.visitedStates.add(state)

            # Press another button
            for move in self.findNewMoves(state):
                stateAfterMove = self.makeMove(state, move)

                if stateAfterMove not in self.visitedStates:
                    queue.append((stateAfterMove, depth + 1, moves + [move]))

        return None

    """
    isGameComplete
    Method which checks if the game is finished. Checks if every tile is set to false. 

    @params: self, state
    @return: True if game is complete, false if not
    """

    def isGameComplete(self, state):
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
        possibleMoves = set()

        for row in range(len(state.grid)):
            for col in range(len(state.grid[row])):
                # If button unpressed and if it is a tile that is part of the game
                if state.grid[row][col] and not state.unpressable[row][col]:
                    possibleMoves.add(Move(row, col))

        return possibleMoves

    """
    makeMove
    Method which will set the current button to its opposite state, will then check buttons in the same row and column.
    If there is any buttons in the same row or column with the same colour or shape, it will reverse the state of these buttons as well.

    @params: self, state, move
    @return: newState, the buttons grid once the move has been made.

    """

    def makeMove(self, state, move):
        row = move.row
        col = move.col

        new_grid = [list(row) for row in state.grid]
        new_grid[row][col] = not new_grid[row][col]

        shape = state.shapes[row][col]
        color = state.colours[row][col]

        # checks buttons which are the same shape or colour in the same column.
        # If there is any, will reverse the state of that button.
        for i in range(len(state.grid)):
            if not state.unpressable[i][col]:
                if state.shapes[i][col] == shape or state.colours[i][col] == color:
                    new_grid[i][col] = not new_grid[i][col]

        # checks buttons which are the same shape or colour in the same row.
        # If there is any, will reverse the state of that button.
        for j in range(len(state.grid[row])):
            if not state.unpressable[row][j]:
                if state.shapes[row][j] == shape or state.colours[row][j] == color:
                    new_grid[row][j] = not new_grid[row][j]

        new_state = State(new_grid, state.shapes,
                          state.colours, state.unpressable)
        return new_state


"""
startingState
Method used to set up each level of the pushing buttons game. This method will set four things, grid is will have true wherever
there is a button which is unpressed. For colours, every matching letter will have the same colour, and same with shape. For 
unpressable, anything that is set to true will be a tile which is not included in the game.

@params: levelNo, the level number to be selected
@return: a starting state
"""


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
        # Gets rid of unwanted tiles in the grid, True if the button is unpressable, or is a tile that is not in use in this game
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


"""
printSolution
Method which will call othere methods in order and then print the solution or no solution found.

@Args: level, the level to be tested
"""


def printSolution(level):
    solver = ButtonsSolver()
    startState = startingState(level)
    solution = solver.solve(startState)

    if solution:
        print(solution)
    else:
        print("No solution found.")


""" 
Enter level number in printSolution(). Currently the levels initialised are 8, 17, 19, 24
"""
printSolution(8)
