# Week 7 Session 2 Standard Problem Set Version 1

# PROBLEM ONE
# def find_cruise_length(cruise_lengths, vacation_length):
#     # print(cruise_lengths)
#     # base case
#     if not cruise_lengths: # empty list
#         return False

#     if len(cruise_lengths) == 1:
#         if cruise_lengths[0] == vacation_length: # vaca_length is in list
#             return True
#         return False # the only element left in list does not equal target

#     # recursive case
#     mid = len(cruise_lengths) // 2
#     # print("THIS IS MID " + str(cruise_lengths[mid]))
#     if vacation_length < cruise_lengths[mid]:
#         return find_cruise_length(cruise_lengths[0:mid], vacation_length)
#     else:
#         return find_cruise_length(cruise_lengths[mid:], vacation_length)
    

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


# PROBLEM TWO
def find_cabin_index(cabins, preferred_deck):
    def helperFunction(left, right):
        # base case

        # recursive case 

        pass
    
    print(cabins)
    # base case
    if not cabins:
        return 0 # index 0 if empty list
    if len(cabins) == 1:
        if preferred_deck < cabins[0]:
            return 0
        else:
            return 1

    # recursive case
    mid = len(cabins) // 2
    if preferred_deck == cabins[mid]: # if equal
        return mid
    elif preferred_deck < cabins[mid]: # left half
        return mid - find_cabin_index(cabins[0:mid], preferred_deck)
    else: # right half
        return mid + find_cabin_index(cabins[mid:], preferred_deck)

# second test case
# passed list # mid       #operation  # return       
# 1 3 5 6     mid = 2     mid - next  return 2
# 1 3         mid = 1     mid - next  return 0
# 1                                     return 1    


print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))