# Week 7 Session 1 Standard Problem Set Version 2

# PROBLEM ONE
def get_village_class_iterative(population):
    count = 0
    while population > 0:
        count += 1
        population = population // 10
    return count


def get_village_class_recursive(population):
    # base case
    if population <= 0:
        return 0

    # recursive case
    return 1 + get_village_class_recursive(population // 10)

print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))


# PROBLEM FOUR
def is_palindrome(name):
    # base case - odd number of characters: 
    if len(name) == 1:
        return True

    # base case - even number of characters:
    if len(name) == 2:
        return name[0]==name[1]

    if len(name) == 0:
        return False #?

    # recursive call
    # compare last and first
    if (name[0] == name[-1]):
        return is_palindrome(name[1:-1])
    return False # first and last characters are not the same

print(is_palindrome("eve"))
print(is_palindrome("ling")) # solution says this returns true...
print(is_palindrome(""))
print(is_palindrome("leet"))