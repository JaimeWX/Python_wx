from available_stations import available_stations
from required_states import required_states

def select_stations():
    selected_stations =set()
    rs = required_states
    while rs:
        best_station = None
        states_covered = set()
        for station, states in available_stations.items():
            # | sum ; & intersection ; - difference set
            covered = rs & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        rs -= states_covered
        selected_stations.add(best_station)
    print(selected_stations)

select_stations()




