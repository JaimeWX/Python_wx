from collections import deque

graph = {}
graph["o"] = ["a","b","c"]
graph["a"] = ["m","n"]
graph["b"] = ["x"]
graph["c"] = ["i","j"]
graph["m"] = []
graph["n"] = []
graph["x"] = []
graph["i"] = []
graph["j"] = []

def bf_search(name):
    search_queue = deque()
    search_queue += graph[name]
    # search array is used to record the person searched.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mongo seller!")
                return True
            else:
                search_queue += graph[person]
                #print(search_queue)
                searched.append(person)
    return False
def person_is_seller(name):
    return name[-1] == "x"

bf_search("o")

