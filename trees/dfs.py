from generate_tree import generate_trees
# implement dfs recursively ================================================================
def dfs(root):
    if not root:
        return
    
    # do some visiting here.
    print(root.val)

    root.visited = True
    if root.left and not root.left.visited:
        dfs(root.left)
    if root.right and not root.right.visited:
        dfs(root.right)




## generate test tree
vals = [1,2,3,4,5,6,7]
my_tree = generate_trees(vals)

# traverse generated tree ===================================================================
dfs(my_tree)
    
    