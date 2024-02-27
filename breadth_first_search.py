graph = {}
graph["dan"] = ["beni", "chris", "gab"]
graph["beni"] = ["martha", "ant", "alex"]
graph["chris"] = ["renan", "denny"]
graph["gab"] = ["renan"]
graph["renan"] = ["gab", "chris"]

from collections import deque

def search_friend(friend):
	search_queue = list(graph["dan"])
	verified = []

	while search_queue:
		person = search_queue.pop(0)
		if person in verified:
			continue
		if person == friend:
			print(friend + " found")
			return True
		else:
			if person in graph:
				search_queue.extend(graph[person])
				verified.append(person)
	print(f"{friend} Not found")
	return False

search_friend("beni")
search_friend("denny")
search_friend("outsider")
