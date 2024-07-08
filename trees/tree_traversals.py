from generate_tree import generate_trees

# recursive traversals ========================================================================

## L -> curr -> R
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)

        # do some visiting here.
        print(node.val)

        in_order_traversal(node.right)

## curr -> children (L -> R)
def pre_order_traversal(node):
    if node:
        # do some visiting here.
        print(node.val)

        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


## children (L -> R) -> curr
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)

        print(node.val)


# test out each traversal ======================================================================

## generate tree.
vals = [1,2,3,4,5,6]
my_tree = generate_trees(vals)

# traverse generated tree ===================================================================
print("in_order_traversal:")
in_order_traversal(my_tree)

print("pre_order_traversal:")
pre_order_traversal(my_tree)

print("post_order_traversal:")
post_order_traversal(my_tree)
