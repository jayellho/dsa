from generate_tree import generate_trees
import collections

# implement bfs iteratively ================================================================
def bfs(root):
    q = collections.deque()
    root.visited = True
    q.append(root)
    while q:
        r = q.popleft()

        # do some visiting here.
        print(r.val)

        if r.left and not r.left.visited:
            r.left.visited = True
            q.append(r.left)
        if r. right and not r.right.visited:
            r.right.visited = True
            q.append(r.right)




## generate test tree
vals = [1,2,3,4,5,6,7]
my_tree = generate_trees(vals)

# traverse generated tree ===================================================================
bfs(my_tree)
    
