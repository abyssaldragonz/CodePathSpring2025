# Week 1 Session 1 Standard Problem Set Version 1

#PROBLEM TWO
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
    pass

#PROBLEM THREE
def print_catchphrase(character):
    if (character == "Pooh"):
        print("Oh bother!")
    elif (character == "Tigger"):
        print("TTFN: Ta-ta for now!")
    elif (character == "Eeyore"):
        print("Thanks for noticing me.")
    elif (character == "Christopher Robin"):
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
    pass

#PROBLEM FOUR
def get_item(items, x):
    if (x < 0 or x >= len(items)):
        return None
    return items[x]
    pass

#PROBLEM FIVE
def sum_honey(hunny_jars):
    sum = 0
    for jar in hunny_jars:
        sum += jar
    return sum
    pass

#PROBLEM SIX
def doubled(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2
    return hunny_jars
    pass

#PROBLEM SEVEN
def count_less_than(race_times, threshold):
    count = 0
    for race in race_times:
        if (race < threshold):
            count += 1
    return count
    pass

#PROBLEM EIGHT
def print_todo_list(task):
    print("Pooh's To Dos:")
    for i in range(len(task)):
        print(f"{i+1}. {task[i]}")
    pass

#PROBLEM NINE
def can_pair(item_quantities):
    for num in item_quantities:
        if (num % 2 != 0): # one number is odd
            return False
    return True # every number in lsit is even
    pass

#PROBLEM TEN
def split_haycorns(quantity):
    arr = []

    for i in range(quantity):
        if (quantity % (i+1) == 0):
            arr.append(i+1)
    return arr
    pass

#PROBLEM ELEVEN
def tiggerfy(s):
    newStr = ""
    tigger = ['t', 'i', 'g', 'e', 'r']
    for ch in s:
        if (ch not in tigger):
            newStr += ch
    return newStr
    pass

#PROBLEM TWELVE
def locate_thistles(items):
    arr = []
    for i in range(len(items)):
        if "thistle" == items[i]:
            arr.append(i)
    return arr
    pass


#STANDARD PROBLEM SET ONE

#PROBLEM ONE
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
    pass

#PROBLEM TWO
def final_value_after_operations(operations):
    tigger = 1
    for elem in operations:
        if (elem == "bouncy" or elem == "flouncy"):
            tigger += 1
        elif (elem == "trouncy" or elem == "pouncy"):
            tigger -= 1
    return tigger
    pass 

#PROBLEM THREE
def tiggerfyAdvanced(word):
    word = word.lower()
    word = word.replace('t', "")
    word = word.replace('i', "")
    word = word.replace('gg', "")
    word = word.replace('er', "")
    return word
    pass

def non_decreasing(nums):
    pass

#MAIN
# greeting("Michael")
# print_catchphrase("Pooh")
# print_catchphrase("Foo")
# print( get_item( ["piglet", "pooh", "roo", "rabbit"], 2) )
# print( get_item( ["piglet", "pooh", "roo", "rabbit"], -1) )
# print( sum_honey([2,3,4,5]) )
# print( doubled([1,2,3]) )
# print( count_less_than([1,2,3,4,5,6], 4) )
# print_todo_list( ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"] )
# print( can_pair([1,2,3,4,5,6,7]) )
# print( can_pair([0,2,4,6,8]) )
# print( split_haycorns(6) )
# print( tiggerfy("suspicerous") )
# print( locate_thistles(["thistle", "stick", "carrot", "thistle", "eeyore's tail"]) )

print( linear_search(['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn'], "hunny") )
print( linear_search(['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn'], "foo") )
print( final_value_after_operations(["trouncy", "bouncy", "flouncy"]) )
print( tiggerfyAdvanced("eggplant") )