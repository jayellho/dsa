import collections

# generate a random tree  ==================================================================
## create node class.
class Node:
    def __init__(self, val = None, left = None, right = None):
        self.visited = False
        self.val = val
        self.left = left
        self.right = right

## define function to generate trees from list of values.       
def generate_trees(vals):
    # empty vals.
    if not vals:
        return None

    root = Node(vals[0])
    queue = collections.deque()
    queue.append(root)
    i = 1
    n = len(vals)

    while i < n:
        current = queue.popleft()

        if i < n:
            current.left = Node(vals[i])
            queue.append(current.left)
            i += 1
        
        if i < n:
            current.right = Node(vals[i])
            queue.append(current.right)
            i += 1
    
    return root