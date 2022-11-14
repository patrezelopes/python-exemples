############

#
# Cheap Crowdfunding Problem
#

# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#

# You would like to get the reward, while spending the least amount > 0.
#

# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.

#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.
#

############


def find_min_pledge(pledge_list):
    pledge_list = list(filter(lambda x: x > 0, pledge_list))
    try:
        min_pledged = min(pledge_list)
        max_pledged = max(pledge_list)
        pledge_possibles = list(range(min_pledged, max_pledged+1, 1))
        pledged_available = set(pledge_possibles).difference(set(pledge_list))
    except ValueError:
        return 1
    try:
        pledge = min(pledged_available)
    except ValueError:
        pledge = max(pledge_list) + 1 if max(pledge_list) < 1000 else None
    return pledge


assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1
assert find_min_pledge(list(range(1, 100000 + 1, 1))) is None

