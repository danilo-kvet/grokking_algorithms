states_set = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


def choose_stations(states_to_include):
	final_stations = set()
	while states_to_include:
		best_station = None
		states_covered = set()

		for station, states in stations.items():
			covered = states_to_include & states

			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered
		
		states_to_include -= states_covered
		final_stations.add(best_station)
	return final_stations
		
print(choose_stations(states_set))

