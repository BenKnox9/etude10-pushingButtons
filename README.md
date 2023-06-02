# etude10-pushingButtons

## Authors
Ben Knox, Daniel Bohinc

## Description
ButtonsBFS.py is a python script which uses breadth first traversal to find the minimum number of moves to complete the pushingButtons.jar game. It will also print out the column and row number of the buttons pressed in order. 

To initialise the game state, we have used 4 nested lists, grid, colours, shapes, and unpressable.
grid is will have true wherever there is a button which is unpressed. For colours, every matching letter will have the same colour, and same with shape. For unpressable, anything that is set to true will be a tile which is not included in the game. 

From here we pass the starting state of the game into the solve method. The solve method is where the BFS will take place. 

