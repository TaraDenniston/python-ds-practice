def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # First attempt--couldn't understand why in example 3 (4,3) would come
    # before (5,2), so I had to look at the solution. I had not been able to
    # figure out a way to do it while only iterating through the list once.

    # for x in range(len(nums)):
    #     for y in range((x + 1), len(nums)):
    #         if nums[x] + nums[y] == goal:
    #             return (nums[x], nums[y])

    # return ()


    # Solution provided--stores the difference, which it looks for in the list
    # (which is why (4,3) comes before (5,2), because it checks 3 against 4 
    # before it checks 2 against 5). I admit this one had me stumped.

    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()



