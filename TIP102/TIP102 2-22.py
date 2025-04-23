# Week 10 Session 1 Standard Problem Set Version 1

# PROBLEM ONE
flights = {"JFK": ["LAX", "DFW"], "LAX": ["JFK"], "DFW": ["ATL", "JFK"], "ATL": ["DFW"]}

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])


# PROBLEM TWO
def bidirectional_flights(flights):
    # True if undirected
    # False if directed
    for i in range(len(flights)): # an airport
        for j in flights[i]: # airport's connected flights
            if i not in flights[j]: # airport flight is not round-trip
                return False
    return True # every flight is round-trip


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))


# PROBLEM THREE
def get_direct_flights(flights, source):
    dq = []
    visited = []
    dq.append(source)

    while dq: # BFS
        popped = dq.pop(0)
        if popped != source:
            visited.append(popped)

        for i in range(len(flights[popped])):
            if flights[popped][i] == 1 and i not in visited:
                dq.append(i)
    return list(set(visited))

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2)) # [0, 1, 3]
print(get_direct_flights(flights, 3)) # []


# PROBLEM FOUR
def get_adj_dict(flights):
    adj_dict = {}

    for connection in flights: # connection is now a list of [a,b]
        if connection[0] not in adj_dict:
            adj_dict[connection[0]] = [connection[1]]
        else:
            adj_dict[connection[0]].append(connection[1])
        
        if connection[1] not in adj_dict:
            adj_dict[connection[1]] = [connection[0]]
        else:
            adj_dict[connection[1]].append(connection[0])

    return adj_dict

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
"""
{
    'Cape Town': ['Addis Ababa', 'Cairo'],
    'Addis Ababa': ['Cape Town', 'Lagos'],
    'Lagos': ['Cairo', 'Addis Ababa'],
    'Cairo': ['Cape Town', 'Lagos', 'Nairobi'],
    'Nairobi': ['Cairo']
}
"""