import matplotlib.pyplot as plt
from PathFinder import calculate_risk

def visualize_grid(grid):
    grid_size = len(grid)
    fig, ax = plt.subplots(figsize=(12, 12))
    
    for i in range(grid_size):
        for j in range(grid_size):
            cell = grid[i][j]
            temperature = cell['temperature']
            past_icebergs = cell['past_icebergs']
            chance = cell['chance']
            
            ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color='lightblue', zorder=0))
            
            ax.text(
                j, i,
                f"T: {temperature:.1f}\nP: {past_icebergs:.2f}\nC: {chance:.2f}",
                ha='center', va='center', fontsize=6, fontweight='bold'
            )
    
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    ax.set_xticks([x - 0.5 for x in range(1, grid_size)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, grid_size)], minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
    ax.set_xlim(-0.5, grid_size - 0.5)
    ax.set_ylim(-0.5, grid_size - 0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(left=False, bottom=False)

    ax.set_title("Grid Visualization: Temperature, Past Icebergs, Chance Of Icebergs Based On Currents And Winds", fontsize=16)
    plt.show()
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PathFinder import calculate_risk
def visualize_grid_with_path(grid, path, animate=False):
    grid_size = len(grid)
    fig, ax = plt.subplots(figsize=(12, 12))

    max_risk = 0
    for i in range(grid_size):
        for j in range(grid_size):
            max_risk = max(max_risk, calculate_risk(grid[i][j]))

    visited_cells = set()

    # Load the image of the ship
    ship_image = mpimg.imread('titanicimage.png')  # Ensure this path is correct
    plt.pause(10)
    for step, (x, y) in enumerate(path):
        if animate:
            ax.clear()
        for i in range(grid_size):
            for j in range(grid_size):
                cell = grid[i][j]

                risk = calculate_risk(cell)
                risk_normalized = risk / max_risk

                color = (0, 0, risk_normalized)
                
                # If the current cell is the ship's position, make the background light blue
                if (i, j) == (x, y):
                    color = 'lightblue'  # Change the background of the current cell to light blue
                    # Place the ship image on top of the light blue background
                    ax.imshow(ship_image, extent=[j - 0.5, j + 0.5, i - 0.5, i + 0.5], zorder=2)
                elif (i, j) in visited_cells:
                    color = 'lightblue'  # The ship's trail will be light blue

                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color=color, zorder=0))

        visited_cells.add((x, y))

        ax.set_xticks(range(grid_size))
        ax.set_yticks(range(grid_size))
        ax.set_xticks([x - 0.5 for x in range(1, grid_size)], minor=True)
        ax.set_yticks([y - 0.5 for y in range(1, grid_size)], minor=True)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
        ax.set_xlim(-0.5, grid_size - 0.5)
        ax.set_ylim(-0.5, grid_size - 0.5)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(left=False, bottom=False)

        ax.set_title("Grid Visualization with Ship Path", fontsize=16)

        plt.pause(0.3 if animate else 0)

        if not animate:
            break

    plt.show()