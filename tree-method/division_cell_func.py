import numpy as np
import matplotlib.pyplot as plt


class division_cell:
    def __init__(self,max_level):

        self.max_level = max_level
        self.sita = np.acos(-1)/6
        self.cell_radius = 2
        self.cell_level = [[0 for _ in range(2**max_level)] for _ in range(2 ** max_level)]

    def division(self,data):
        for level in range(1,self.max_level + 1):
            sub_cell_radius = self.cell_radius / 2**level / 2 
            for line in range(0,2**level):
                for row in range(0,2**level):
                    cell_center_x = sub_cell_radius*(1 + 2 * row) - self.cell_radius / 2
                    cell_center_y = self.cell_radius/2 - sub_cell_radius*(1 + 2 * line)

                    dx = np.fabs(cell_center_x - data[0])
                    dy = np.fabs(cell_center_y - data[1])

                    r_particle_cell_center = np.sqrt(dx * dx + dy * dy)

                    prospect_sita = sub_cell_radius * 2/r_particle_cell_center
                    if(prospect_sita < self.sita):
                        size = 2 ** (self.max_level - level)
                        for i in range(0,size):
                            for j in range(0,size):
                                if(self.cell_level[size * line + i ][size * row + j ] == 0):
                                    self.cell_level[size * line + i ][size * row + j ] = level
    
        return self.cell_level
