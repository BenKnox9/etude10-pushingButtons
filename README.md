# Etude 10 - Pushing Buttons

## Authors
Ben Knox, Daniel Bohinc

## Description
ButtonsBFS.py is a python script which uses breadth first traversal to find the minimum number of moves to complete the pushingButtons.jar game. It will also print out the column and row number of the buttons pressed in order. 


To initialise the game state, we have used 4 nested lists, grid, colours, shapes, and unpressable.

These 4 nested lists assumed that the game as a whole was made up of 5 tiles by 5 tiles, however we could ignore tiles which weren't being used for buttons with the unpressable grid.

To set up the initial game state this is what we did:
grid will have true wherever there is a button which is unpressed. For colours, every matching character will have the same colour, and same with shape. For unpressable, anything that is set to true will be a tile which is not included in the game. 

From here we pass the starting state of the game into the solve method. The solve method is where the BFS will take place. The solve method will check if the game is complete (all buttons are pressed down) and if so return the solution. If not it will add itself to visitedStates and then press another button. This process will repeat until a solution is found.

The reason that BFS is used in this solution is that it loops through all possiblities at depth one, and then all new possibilities at depth two and so on. This means that any solution found will in theory be the optimum solution (the solution with the minimum depth). 

More in depth descriptions on methods is included as comments in buttonsBFS.py

## Running the code
Before you run the code you need to specify the level you want to find the solution for. This is done in line 323 of the script, enter the level as the paramter for the call to printSolution(). 
e.g. for level 8:
```python
printSolution(8)
```

If you want to test a level that is not initialised yet you will need to add the relevant nested lists in the starting state method. the elements of each list are as follows:
- grid will have true wherever there is a button which is unpressed.
- For colours, every matching character will have the same colour. 
- For shapes, every matching character will have the same shape. 
- For unpressable, anything that is set to true will be a tile which is not included in the game. 

To run the code after you have the desired level enter the following in the terminal:

```bash
python3 buttonsBFS.py
```

## Testing
Firstly prior to this submission we had submitted a manual approach to solving these levels, so were already aware of the optimum solutions. 

Given buttonsBFS.py prints out the buttons pressed in order, we could use these buttons in the game and verify that the buttons pressed would in fact complete the game. As well as this, the optimum number of buttons pressed for each level matched the result we found when using a manual approach to this task. 

The example solutions below are expressed in the form (column, row). 
We are assuming that the game is made up of 5 tiles by 5 tiles, with the top left tile of the game being at column 0 and row 0. 

The final number of buttons pressed for each level was as follows: 
- Level 8:  3 
    - Example solution: [(1, 3), (1, 1), (2, 3)]

- Level 17:  10 
    - Example solution: [(2, 4), (0, 1), (0, 2), (4, 1), (2, 3), (3, 3), (0, 1), (3, 2), (2, 3), (1, 2)]

- Level 24:  6
    - Example solution: [(3, 0), (4, 3), (2, 1), (2, 0), (2, 1), (1, 0)]

Extra level:
- Level 19:  8
    - Example solution: [(0, 3), (1, 3), (2, 3), (3, 3), (0, 3), (4, 3), (4, 2), (3, 3)]

#### Example solutions
These example solutions aren't the only solutions which will work, many others will achieve the same result in the same number of moves. As well as this our program will not generate the same example solution every time, it will generate the first solution it finds in the shortest number of moves, so, if the code was to be run again these example solutions may not be the solutions generated yet the total number of buttons pressed will be the same.