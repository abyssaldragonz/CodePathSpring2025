# Week 7 Session 1 Standard Problem Set Version 1

#PROBLEM ONE
def count_suits_iterative(suits):
    count = 0
    for s in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    # base case
    if not suits: # empty list
        return 0
    return 1 + count_suits_recursive(suits[1:]) # recursive call

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))


#PROBLEM TWO
def sum_stones(stones): # follow same structure as problem one
    # base case
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))


#PROBLEM THREE
def count_suits_iterative(suits): # find unique values - no dupes
    uniqueSuits = set() # set is the best DS for this
    for s in suits:
        uniqueSuits.add(s)
    return len(uniqueSuits)

def count_suits_recursive(suits):
    # base case - if empty
    if not suits:
        return 0
    # base case - if duplicate encountered somewhere else in list
    if suits[0] in suits[1:]:
        return count_suits_recursive(suits[1:]) # dont add 1

    # recursive call - only if we need to add to count aka no dupes
    return 1 + count_suits_recursive(suits[1:]) # add 1


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark III", "Mark II"]))
