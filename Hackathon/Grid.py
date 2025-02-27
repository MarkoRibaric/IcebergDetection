import numpy as np

def generate_grid(size):
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            wind_factor = np.random.uniform(0, 1)
            current_factor = np.random.uniform(0, 1)
            chance = (wind_factor + current_factor) / 2 
            
            cell = {
                "temperature": np.random.uniform(-5, 15),
                "past_icebergs": np.random.uniform(0, 1),
                "chance": chance
            }
            row.append(cell)
        grid.append(row)
    return grid
