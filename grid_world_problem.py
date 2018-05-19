from copy import deepcopy
f = open("input.txt","r")
lines = f.readlines()
rows_cols = lines[0].replace("\n", "").split(",")
walls_line = lines[1].strip("\n")
wall_position = []
walls = int(walls_line)
for i in range(0,walls):
     wall_position.append(lines[i+2].replace("\n", "").split(","))
terminal_states_lines = lines[2+walls].strip("\n")
terminal_states = int(terminal_states_lines)
terminal_states_position = []
for j in range(0,terminal_states):
     terminal_states_position.append(lines[j+3+walls].replace("\n","").split(","))
p = lines[terminal_states+walls+3].replace("\n","").split(",")
r = lines[terminal_states+walls+4].replace("\n","").split(",")
discount_factor = lines[terminal_states+walls+5].strip("\n")
f.close()


rows = int(rows_cols[0])
columns = int(rows_cols[1])

w, h = rows, columns;
grid = [[0.0 for x in range(h)] for y in range(w)]
terminal = [['' for x in range(h)] for y in range(w)]

# Placing walls in grid
for i in range(rows-1,-1,-1):
    for j in range(0,columns,1):
        for k in range(0,walls,1):
            if i==int(wall_position[k][0])-1 and j==int(wall_position[k][1])-1:
                grid[i][j] = float("-inf")


# Placing terminals in grid
for i in range(rows-1,-1,-1):
    for j in range(0,columns,1):
        for k in range(0,terminal_states,1):
            if i==int(terminal_states_position[k][0])-1 and j==int(terminal_states_position[k][1])-1:
                grid[i][j] = float(terminal_states_position[k][2])
                terminal[i][j] = "t"

def grid_world(grid):
    a, b = rows, columns
    new_board =[[0 for m in range(b)] for n in range(a)]
    move=[['' for s in range(b)] for t in range(a)]
    while(new_board!=grid):
        new_board = deepcopy(grid)
        for i in range(0,rows,1):
            for j in range(0,columns,1):
                max_util = float("-inf")

                # Wall or Terminal
                if grid[i][j] == float("-inf") or terminal[i][j] == "t":
                    if grid[i][j] == float("-inf"):
                        move[i][j] = "None"
                    else:
                        move[i][j] = "Exit"

                # Not a wall or a terminal
                else:
                    # Walk Up
                    if i + 1 <= rows-1 and grid[i + 1][j] != float("-inf"):
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 >= 0:
                            if grid[i][j - 1] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j - 1]
                            else:
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        if j + 1 <= columns - 1:
                            if grid[i][j + 1] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j + 1]
                            else:
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util = float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i + 1][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Walk Up"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 >= 0:
                            if grid[i][j - 1] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j - 1]
                            else:
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        if j + 1 <= columns - 1:
                            if grid[i][j + 1] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j + 1]
                            else:
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util = float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Walk Up"
                    # Walk Down
                    if i-1>=0 and grid[i-1][j] != float("-inf"):
                        u1 = 0.0
                        u2 = 0.0

                        if j-1>=0:
                            if grid[i][j-1]!= float("-inf"):
                                u1 = 0.5*(1-float(p[0]))*grid[i][j-1]
                            else:
                                u1 = 0.5*(1-float(p[0]))*grid[i][j]
                        else:
                             u1 = 0.5*(1-float(p[0]))*grid[i][j]
                        if j+1<=columns-1:
                            if grid[i][j+1]!= float("-inf"):
                                u2 = 0.5*(1-float(p[0]))*grid[i][j+1]
                            else:
                                u2 = 0.5*(1-float(p[0]))*grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util=float(r[0]) + (float(discount_factor) * (float(p[0])*grid[i-1][j] +u1+u2))
                        if util>max_util:
                            max_util=util
                            move[i][j] = "Walk Down"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 1 >= 0:
                            if grid[i][j - 1] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j - 1]
                            else:
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        if j + 1 <= columns - 1:
                            if grid[i][j + 1] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j + 1]
                            else:
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util = float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Walk Down"
                    # Walk left
                    if j-1>=0 and grid[i][j-1] != float("-inf"):
                        u1 = 0.0
                        u2 = 0.0

                        if i+1<=rows-1:
                            if grid[i+1][j]!= float("-inf"):
                                u1 = 0.5 * (1 - float(p[0])) * grid[i+1][j]
                            else:
                                u1 = 0.5*(1-float(p[0]))*grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        if i-1>=0:
                            if grid[i-1][j]!= float("-inf"):
                                u2= 0.5 * (1 - float(p[0])) * grid[i-1][j]
                            else:
                                u2 = 0.5*(1-float(p[0]))*grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util=float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i][j-1]+u1+u2))
                        if util>max_util:
                            max_util=util
                            move[i][j]="Walk Left"
                    else:
                            u1 = 0.0
                            u2 = 0.0

                            if i + 1 <= rows - 1:
                                if grid[i + 1][j] != float("-inf"):
                                    u1 = 0.5 * (1 - float(p[0])) * grid[i + 1][j]
                                else:
                                    u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                            else:
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                            if i - 1 >= 0:
                                if grid[i - 1][j] != float("-inf"):
                                    u2 = 0.5 * (1 - float(p[0])) * grid[i - 1][j]
                                else:
                                    u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                            else:
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                            util = float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i][j] + u1 + u2))
                            if util > max_util:
                                max_util = util
                                move[i][j] = "Walk Left"
                    # Walk right
                    if j+1<=columns-1 and grid[i][j+1] != float("-inf"):
                        u1 = 0.0
                        u2 = 0.0

                        if i+1<=rows-1:
                            if grid[i+1][j]!= float("-inf"):
                                u1=0.5 * (1 - float(p[0])) * grid[i+1][j]
                            else:
                                u1=0.5*(1-float(p[0]))*grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        if i-1>=0:
                            if grid[i-1][j]!= float("-inf"):
                                u2= 0.5 * (1 - float(p[0])) * grid[i-1][j]
                            else:
                                u2=0.5*(1-float(p[0]))*grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util=float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i][j+1] +u1+u2))
                        if util>max_util:
                            max_util=util
                            move[i][j]="Walk Right"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if i + 1 <= rows - 1:
                            if grid[i + 1][j] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[0])) * grid[i + 1][j]
                            else:
                                u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        if i - 1 >= 0:
                            if grid[i - 1][j] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[0])) * grid[i - 1][j]
                            else:
                                u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[0])) * grid[i][j]
                        util = float(r[0]) + (float(discount_factor) * (float(p[0]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Walk Right"
                    # Run Up
                    if i+2<=rows-1 and grid[i+2][j] != float("-inf") and grid[i+1][j] != float("-inf"):
                        u1 = 0.0
                        u2 = 0.0
                        if j-2>=0:
                            if grid[i][j-1]!=float("-inf") and grid[i][j-2]!=float("-inf"):
                                u1=0.5*(1-float(p[1]))*grid[i][j-2]
                            else:
                                u1=0.5*(1-float(p[1]))*grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if j+2<=columns-1:
                            if grid[i][j+1]!=float("-inf") and grid[i][j+2]!=float("-inf"):
                                u2=0.5*(1-float(p[1]))*grid[i][j+2]
                            else:
                                u2=0.5*(1-float(p[1]))*grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util=float(r[1]) + (float(discount_factor) * (float(p[1])*grid[i+2][j] +u1+u2))
                        if util>max_util:
                            max_util=util
                            move[i][j]="Run Up"
                    else:
                        u1 = 0.0
                        u2 = 0.0

                        if j - 2 >= 0:
                            if grid[i][j - 1] != float("-inf") and grid[i][j - 2] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j - 2]
                            else:
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if j + 2 <= columns - 1:
                            if grid[i][j + 1] != float("-inf") and grid[i][j + 2] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j + 2]
                            else:
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util = float(r[1]) + (float(discount_factor) * (float(p[1]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Run Up"
                    # Run Down
                    if i - 2 >=0 and grid[i - 2][j] != float("-inf") and grid[i - 1][j] != float("-inf"):
                        u1 = 0.0
                        u2 = 0.0
                        if j - 2 >= 0:
                            if grid[i][j - 1] != float("-inf") and grid[i][j - 2] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j - 2]
                            else:
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if j + 2 <= columns - 1:
                            if grid[i][j + 1] != float("-inf") and grid[i][j + 2] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j + 2]
                            else:
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util = float(r[1]) + (float(discount_factor) * (float(p[1]) * grid[i - 2][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Run Down"
                    else:
                        u1 = 0.0
                        u2 = 0.0
                        if j - 2 >= 0:
                            if grid[i][j - 1] != float("-inf") and grid[i][j - 2] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j - 2]
                            else:
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if j + 2 <= columns - 1:
                            if grid[i][j + 1] != float("-inf") and grid[i][j + 2] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j + 2]
                            else:
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util = float(r[1]) + (float(discount_factor) * (float(p[1]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Run Down"
                    # Run left
                    if j-2>=0 and grid[i][j-2] != float("-inf") and grid[i][j-1] != float("-inf"):
                        u1=0.0
                        u2=0.0
                        if i+2<=rows-1:
                            if grid[i+1][j]!=float("-inf") and grid[i+2][j]!=float("-inf"):
                                u1=0.5*(1-float(p[1]))*grid[i+2][j]
                            else:
                                u1=0.5*(1-float(p[1]))*grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if i-2>=0:
                            if grid[i-1][j]!=float("-inf") and grid[i-2][j]!=float("-inf"):
                                u2=0.5*(1-float(p[1]))*grid[i-2][j]
                            else:
                                u2=0.5*(1-float(p[1]))*grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util=float(r[1]) + (float(discount_factor) * (float(p[1])*grid[i][j-2] +u1+u2))
                        if util>max_util:
                            max_util=util
                            move[i][j]="Run Left"
                    else:
                        u1 = 0.0
                        u2 = 0.0
                        if i + 2 <= rows - 1:
                            if grid[i + 1][j] != float("-inf") and grid[i + 2][j] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[1])) * grid[i + 2][j]
                            else:
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if i - 2 >= 0:
                            if grid[i - 1][j] != float("-inf") and grid[i - 2][j] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[1])) * grid[i - 2][j]
                            else:
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util = float(r[1]) + (float(discount_factor) * (float(p[1]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Run Left"
                    # Run right
                    if j+2<=columns-1 and grid[i][j+2] != float("-inf") and grid[i][j+1] != float("-inf"):
                        u1=0.0
                        u2=0.0
                        if i+2<=rows-1:
                            if grid[i+1][j]!=float("-inf") and grid[i+2][j]!=float("-inf"):
                                u1=0.5*(1-float(p[1]))*grid[i+2][j]
                            else:
                                u1=0.5*(1-float(p[1]))*grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if i-2>=0:
                            if grid[i-1][j]!=float("-inf") and grid[i-2][j]!=float("-inf"):
                                u2=0.5*(1-float(p[1]))*grid[i-2][j]
                            else:
                                u2=0.5*(1-float(p[1]))*grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util=float(r[1]) + (float(discount_factor) * (float(p[1])*grid[i][j+2] +u1+u2))
                        if util>max_util:
                            max_util=util
                            move[i][j]="Run Right"
                    else:
                        u1 = 0.0
                        u2 = 0.0
                        if i + 2 <= rows - 1:
                            if grid[i + 1][j] != float("-inf") and grid[i + 2][j] != float("-inf"):
                                u1 = 0.5 * (1 - float(p[1])) * grid[i + 2][j]
                            else:
                                u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u1 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        if i - 2 >= 0:
                            if grid[i - 1][j] != float("-inf") and grid[i - 2][j] != float("-inf"):
                                u2 = 0.5 * (1 - float(p[1])) * grid[i - 2][j]
                            else:
                                u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        else:
                            u2 = 0.5 * (1 - float(p[1])) * grid[i][j]
                        util = float(r[1]) + (float(discount_factor) * (float(p[1]) * grid[i][j] + u1 + u2))
                        if util > max_util:
                            max_util = util
                            move[i][j] = "Run Right"
                    grid[i][j] = max_util

    return move

solution = grid_world(grid)

with open('output.txt', 'w') as the_file:
    for i in range(rows-1,-1,-1):
        for j in range(0,columns,1):
            the_file.write(solution[i][j])
            if j!=columns-1:
                the_file.write(",")
        if i!=0:
            the_file.write("\n")

the_file.close()
