class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def print(self):
        print(self.val)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()

def insert_node(node: Node, val):
    if val < node.val:
        node.left = val
    else:
        node.right = val
    return node

def evaluate_node(tree: Node, remaining_list):
    # [1,2,3,4,5] or [1,2,3,4,5,6] then median = 3
    if not remaining_list:
        return tree
    median = remaining_list[round(len(remaining_list) / 2)]
    left_list = remaining_list[0:median-1]
    right_list = remaining_list[median:len(remaining_list)]
    # find middle and split list by center
    if tree is None:
        tree = Node(median, None, None)
    tree.left = evaluate_node(tree, left_list)
    tree.right = evaluate_node(tree, right_list)
    return tree

evaluate_node(None, [1,2,3,4,5,6])

def main():
    n = Node(5, Node(3,Node(6, None, None), None), Node(4, None, None))
    n.print()

    #nums = [-1,0,3,5,9,12]


#main()