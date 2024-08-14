internal_path = 0
depth=0

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree(root, level=0, prefix="Root: "):

    global internal_path
    global depth

    if root is not None:
        print(" " * (level * 4) + prefix + root.val)
        if root.left or root.right:
            if root.left:
                internal_path += (level+1)
                print_tree(root.left, level + 1, "{}".format(level+1)+" 左 --- ")
            else:
                print(" " * ((level + 1) * 4) +   "{}".format(level+1)+" 左 --- None")
            if root.right:
                internal_path += (level+1)
                print_tree(root.right, level + 1,"{}".format(level+1)+" 右 --- ")
            else:
                print(" " * ((level + 1) * 4) +  "{}".format(level+1)+" 右 --- None")
            
            if depth < level+1:
                depth = level+1
            

def external_path_length(root, depth=0):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return depth
    return external_path_length(root.left, depth + 1) + external_path_length(root.right, depth + 1)


def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=' ') 
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# 测试代码
if __name__ == "__main__":
    
    str = "CORONAVIRUS"

    root  = TreeNode(str[0])
    str1  = str[1:]
    for c in str1:
        root = insert(root, c)

    # 层次打印树
    external_path = external_path_length(root,0)
    print_tree(root,0)
    print("[",str, "]:  depth of tree: ", depth, " internal path: " , internal_path,"external path:",external_path)
    print("preorder traversal: ", end=' ') 
    preorder_traversal(root)