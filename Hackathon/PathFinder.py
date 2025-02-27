import heapq

def calculate_risk(cell):
    temperature = cell["temperature"]
    past_icebergs = cell["past_icebergs"]
    chance = cell["chance"]
    
    temp_risk = abs(temperature - 0) / 15
    iceberg_risk = past_icebergs * 2
    chance_risk = chance * 10
    
    return temp_risk + iceberg_risk + chance_risk


def find_least_risk_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    risks = [[float('inf')] * cols for _ in range(rows)]
    risks[start[0]][start[1]] = 0

    priority_queue = [(0, start)]
    previous = {}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while priority_queue:
        current_risk, (x, y) = heapq.heappop(priority_queue)

        if (x, y) == end:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                neighbor_risk = calculate_risk(grid[nx][ny])
                new_risk = current_risk + neighbor_risk

                if new_risk < risks[nx][ny]:
                    risks[nx][ny] = new_risk
                    heapq.heappush(priority_queue, (new_risk, (nx, ny)))
                    previous[(nx, ny)] = (x, y)

    path = []
    current = end
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return path, risks[end[0]][end[1]]
