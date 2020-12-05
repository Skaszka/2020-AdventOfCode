def slope_collisions(treemap, height, width, y_change, x_change):

    tree_collisions = 0
    y = 0
    x = 0

    while (y<height):
        if treemap[y][x] == '#':
            tree_collisions += 1
        
        x = (x+x_change)%width
        y = y+y_change
        
    return(tree_collisions)


if __name__ == "__main__":

    input = open("input/day03.txt")

    treemap = []

    for line in input:
        treeline = []
        for char in line:
            if char!='\n':
                treeline.append(char)
        treemap.append(treeline)
        
    height = len(treemap)
    width = len(treemap[0])
    
    slope_checks = []
    slope_checks.append(slope_collisions(treemap, height, width, 1, 3))
    
    print("Solution to part a:", slope_checks[0] )
    
    slope_checks.append(slope_collisions(treemap, height, width, 1, 1))
    slope_checks.append(slope_collisions(treemap, height, width, 1, 5))
    slope_checks.append(slope_collisions(treemap, height, width, 1, 7))
    slope_checks.append(slope_collisions(treemap, height, width, 2, 1))
    
    slope_prod = 1
    for entry in slope_checks:
        slope_prod *= entry
    
    print("Solution to part b:", slope_prod )    