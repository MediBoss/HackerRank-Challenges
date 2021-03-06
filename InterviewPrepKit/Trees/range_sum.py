'''
Given the root node of a binary search tree, return the sum of values
of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Level  : Medium
Time Allocated : 20 minutes
Time Used : 32 minutes
Time Complexity : O(n)
Space Complexity : O(n)
'''

def rangeSumBST(self, root, L, R):
    '''Using DFS to find all values in range'''

    sum = 0
    list_of_queues = deque([root])

    while len(list_of_queues) > 0:
        curr_node = list_of_queues.popleft()
        if curr_node.val >= L and curr_node.val <= R:
            sum += curr_node.val
        if curr_node.left:
            list_of_queues.append(curr_node.left)
        if curr_node.right:
            list_of_queues.append(curr_node.right)


    return(sum)
