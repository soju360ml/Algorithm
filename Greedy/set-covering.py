stations = {'a': {1, 2}, 'b': {1}, 'c': {2, 3}}
states_needed = {1, 2, 3}
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)