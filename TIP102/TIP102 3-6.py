# Week 3 Session 2 Advanced Problem Set Version 2

# PROBLEM THREE
def match_buyers_and_sellers(buyers, sellers):
    # max num of sales
    # each buyer can only buy from one person
    # each seller can only sell from one person

    # two pointers to loop through two lists
    # sort lists before looping

    maxSales = 0

    buyers.sort()
    sellers.sort()
    buyers=buyers[::-1]
    sellers=sellers[::-1]

    buyPoint, sellPoint = 0, 0

    while (buyers and sellers and buyPoint<len(buyers)):
        # if a sale is made, pop the ones who were involved in sale
        if buyers[buyPoint] >= sellers[sellPoint]:
            # can make sale
            buyers.pop(buyPoint)
            sellers.pop(sellPoint)
            maxSales += 1
        else:
            # no sale can be made
            buyPoint += 1


    return maxSales



buyers1 = [4, 7, 9]
sellers1 = [8, 2, 5, 8]
print(match_buyers_and_sellers(buyers1, sellers1)) 

buyers2 = [1, 1, 1]
sellers2 = [10]
print(match_buyers_and_sellers(buyers2, sellers2))