import numpy as np
import matplotlib.pyplot as plt
from create_particle import particle_position 

max_level = 2
sita = np.acos(-1)/8
datas = particle_position

cell_radius = 2

data = [0.7,-0.5]

cell_level = [[0 for _ in range(np.pow(2,max_level))] for _ in range(np.pow(2,max_level))]

for level in range(1,max_level + 1):
    sub_cell_radius = cell_radius / np.pow(2 , level) / 2 
    for line in range(0,np.pow(2,level)):
        for row in range(0,np.pow(2,level)):

            cell_center_x = sub_cell_radius*(1 + 2 * row) - cell_radius / 2
            cell_center_y = cell_radius/2 - sub_cell_radius*(1 + 2 * line)

            dx = np.fabs(cell_center_x - data[0])
            dy = np.fabs(cell_center_y - data[1])

            print(cell_radius/2 - sub_cell_radius*(1 + 2 * line),line)

            if (dx <= sub_cell_radius ) and (dy <= sub_cell_radius) :
                cell_level[line][row] = -1
            else:
                if dx == 0:
                    r_particle_cell = np.fabs(dy - sub_cell_radius)
                if dy == 0:
                    r_particle_cell = np.fabs(dx - sub_cell_radius)
                else :
                    r_particle_cell_center = np.sqrt(dx * dx + dy * dy)

                prospect_sita = sub_cell_radius/r_particle_cell_center
                if(prospect_sita < sita):
                    size = 2 ** (max_level - level)
                    for i in range(0,size):
                        for j in range(0,size):
                            if(cell_level[size * line + i ][size * row + j ] == 0):
                                cell_level[size * line + i ][size * row + j ] = level
                    

plt.imshow(cell_level, cmap='Blues', extent=[-1, 1, -1, 1])

plt.colorbar()

plt.show()