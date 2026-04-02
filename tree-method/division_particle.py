import numpy as np
import matplotlib.pyplot as plt
from division_cell_func import division_cell

particle_num = 100
particle_position = np.random.uniform(-1,1,size = (particle_num,2))
max_level = 4

field_diameter = 2

cell_diameter = 2 / 2 ** max_level

division = division_cell(max_level)

particles_position =particle_position

particles_level = []

divide_particles = [[[] for  _ in range(2 ** max_level)] for _ in range(2 ** max_level)]

particle = [0.345 , -0.393]

level_array = division.division(particle)
for particle_position in particles_position :
    found = False
    for i in range(0 , 2 ** max_level):
        if found : break
        if particle_position[0] >= cell_diameter * i - field_diameter / 2 and particle_position[0] < cell_diameter*(i + 1) - field_diameter / 2 :
            for j in range(0, 2 ** max_level):
                if particle_position[1] <=  field_diameter / 2 - cell_diameter * j and particle_position[1] > field_diameter / 2 - cell_diameter *( j + 1) :
                    particles_level.append(level_array[j][i])
                    divide_particles[j][i].append(particle_position)
                    found = True
                    break

# plt.scatter(particles_position[:particle_num,0],particles_position[:particle_num,1] ,c=particles_level ,cmap = 'vanimo')
# plt.imshow(level_array, cmap='Blues', extent=[-1, 1, -1, 1])
# plt.colorbar()
# plt.show()