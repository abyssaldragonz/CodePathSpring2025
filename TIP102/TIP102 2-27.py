# Problem Three
# Visit booths which have a specific number of points available
# Use a stack
# Return total points collected after visiting all booths

def collect_festival_points(points):
    stack = [];
    for booth in points:
        stack.append(booth);

    return sum(stack)

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 


# Problem Four
# visit booths in specific a order
# red herrings with "back"
# use stack
def booth_navigation(clues):
    journey = [];

    for clue in clues:
        if clue == "back" and journey:
            journey.pop()
        elif clue != "back":
            journey.append(clue);

    return journey;

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 