# Lattice paths

# Starting in the top left corner of a 2 X 2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
# How many such routes are there through a 20 X 20 grid ?

"""
Solution Approach :
===================

* Consider the grid as block of small squares
* calculate the number of lattice paths that reach each level of the bottom corner of mini squares
* for a 3 X 3 grid
* Path(0,0) = 1;
* Path(1,0) = 1; Path(1,1) = 2
* Path(2,0) = 1; Path(2,1) = 3; Path(2,2) = 6
* Path(3,0) = 1; Path(3,1) = 4; Path(3,2) = 10; Path(3,3) = 20

* Now we observed a pattern in total lattice paths covered (for co-ordinates I, J)

* Assume Path(0,J) = 1
* Path = 1, if J = 0
* Path = Path(I,J-1) + Path(I-1, J), if I > J and J > 0
* Path = 2 * Path(I, J-1), if I = J
* Path(n,n) = Gives the total lattice paths covered

"""

def total_lattice_path(grid_size):
    path = [1] * grid_size
    for i in range( grid_size):
        for j in range(i):
            path[j] = path[j] + path[j - 1]
        path[i] = 2 * path[i - 1]
    return path[grid_size - 1]