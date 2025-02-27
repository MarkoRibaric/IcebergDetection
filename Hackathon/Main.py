from Grid import generate_grid
from Visualization import visualize_grid, visualize_grid_with_path
from PathFinder import find_least_risk_path

def main():

    grid_size = 10
    grid = generate_grid(grid_size)

    start = (grid_size - 1, 0)
    end =  (0, grid_size - 1)

    path, total_risk = find_least_risk_path(grid, start, end)
    print(f"Least Risk Path: {path}")
    print(f"Total Risk: {total_risk:.2f}")

    #visualize_grid(grid)
    visualize_grid_with_path(grid, path, animate=True, save_animation=True)


if __name__ == "__main__":
    main()
