import time


def travelling_salesperson_solver(adj_matrice):
    visited = init_visited(adj_matrice)
    visited[0] = True
    curr_solution = {"path": [], "cost": 0}
    curr_solution["path"].append(0)
    best_solution = None

    best_solution = branch_and_bound(adj_matrice, 0, visited, curr_solution, best_solution)
    print(str(best_solution))


def branch_and_bound(adj_matrice, curr_node, visited, curr_solution, best_solution):
    all_visited = True

    if bound(curr_solution, best_solution, visited, adj_matrice):
        return best_solution

    for node_id, cost in enumerate(adj_matrice[curr_node]):
        all_visited &= visited[node_id]

        if not visited[node_id] and node_id != curr_node:
            curr_solution["path"].append(node_id)
            curr_solution["cost"] += cost
            visited[node_id] = True
            best_solution = branch_and_bound(adj_matrice, node_id, visited, curr_solution, best_solution)
            curr_solution["path"].pop()
            curr_solution["cost"] -= cost
            visited[node_id] = False

    if all_visited:
        last_neighbor = curr_solution["path"][-1]
        curr_solution["path"].append(0)
        curr_solution["cost"] += adj_matrice[last_neighbor][0]

        if not best_solution or curr_solution["cost"] < best_solution["cost"]:
            best_solution = {
                "path": curr_solution["path"][:],
                "cost": curr_solution["cost"]
            }

        curr_solution["path"].pop()
        curr_solution["cost"] -= adj_matrice[last_neighbor][0]

    return best_solution


def bound(curr_solution, best_solution, visited, adj_matrice):
    cost = curr_solution["cost"]
    #for node_id, value in enumerate(visited):
    #    if not value:
    #        cost += min([costs[node_id] for costs in adj_matrice])
    return best_solution and best_solution["cost"] < cost


def init_visited(adj_matrice):
    return [False for _ in adj_matrice];


if __name__ == "__main__":
    adj_matrice = [
        [0   , 29  , 20  , 21  , 16  , 31  , 100 , 12  , 4   , 31  , 18  ],
        [29  , 0   , 15  , 29  , 28  , 40  , 72  , 21  , 29  , 41  , 12  ],
        [20  , 15  , 0   , 15  , 14  , 25  , 81  , 9   , 23  , 27  , 13  ],
        [21  , 29  , 15  , 0   , 4   , 12  , 92  , 12  , 25  , 13  , 25  ],
        [16  , 28  , 14  , 4   , 0   , 16  , 94  , 9   , 20  , 16  , 22  ],
        [31  , 40  , 25  , 12  , 16  , 0   , 95  , 24  , 36  , 3   , 37  ],
        [100 , 72  , 81  , 92  , 94  , 95  , 0   , 90  , 101 , 99  , 84  ],
        [12  , 21  , 9   , 12  , 9   , 24  , 90  , 0   , 15  , 25  , 13  ],
        [4   , 29  , 23  , 25  , 20  , 36  , 101 , 15  , 0   , 35  , 18  ],
        [31  , 41  , 27  , 13  , 16  , 3   , 99  , 25  , 35  , 0   , 38  ],
        [18  , 12  , 13  , 25  , 22  , 37  , 84  , 13  , 18  , 38  , 0   ]
    ]
    start_time = time.time()
    travelling_salesperson_solver(adj_matrice)
    end_time = time.time()

    print("{} seconds".format(end_time - start_time))
