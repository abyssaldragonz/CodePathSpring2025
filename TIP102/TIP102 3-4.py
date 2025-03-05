# PROBLEM FIVE
def clean_post(post):
    stack = []

    # for i in range(len(post)-1):
    #     if post[i].islower and post[i+1].isupper and post[i].upper==post[i+1]: # is a pair of upper and lower
            # remove it by popping off stack

    # add each letter to stack
    # if letter to add can make a pair with the stack's top, 
    #   pop previous letter off

    for ch in post:
        if stack: # stack has something
            if (ch.isupper() and stack[-1].islower() and ch.lower()==stack[-1]):
                stack.pop()
                continue # is a pair so dont append anything at all after popping
            if (ch.islower() and stack[-1].isupper() and ch.upper()==stack[-1]):
                stack.pop()
                continue
        
        stack.append(ch)

        # aA
        # Aa
        # aa <- not a pair
    return "".join(stack)

# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s")) 


# PROBLEM SIX
def edit_post(post):
# start with empty string
# pop every element in queue and add to empty string
    retStr = ""
    queue = post.split()

    for word in queue:
        # retStr += queue.pop(0)
        # retStr = queue.pop(0) + retStr
        retStr += word[::-1] + " " # without a queue
    return retStr
      
# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 

# PROBLEM SEVEN
def post_compare(draft1, draft2):
    stack1 = []
    stack2 = []

    for ch in draft1:
        if ch != '#':
            stack1.append(ch)
        else: 
            stack1.pop()

    for ch in draft2:
        if ch != '#':
            stack2.append(ch)
        else: 
            stack2.pop()
            
    return stack1 == stack2

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 