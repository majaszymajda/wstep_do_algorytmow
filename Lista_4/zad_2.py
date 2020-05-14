class Node:
    # wezel binarny

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


# class BinTree:
#     def __init___(self, root):
#         self.root = root


def traverse_preorder(top):
    if top is None:
        return
    print(top)
    traverse_preorder(top.left)
    traverse_preorder(top.right)


def traverse_postorder(top):
    if top is None:
        return
    traverse_postorder(top.left)
    traverse_postorder(top.right)
    print(top)


def wybieranie_liscia():
    print("wybierz z ktorego z lisci chcesz stworzyc nowe drzewo")
    lisc = int(input())
    return lisc


def search_for_node(data, root):
    if root is None:
        return None
    if root.data == data:
        return root
    else:
        node = search_for_node(data, root.left)
        if node is not None:
            return node
        else:
            return search_for_node(data, root.right)


def search_for_father(node, root):
    # nie jes optymalne, ale struktura zbudowana z lewego
    # i prawego nie wskazuje na ojca
    if root is None:
        return None
    if root is node:
        return None
    else:
        if (root.left is node) or (root.right is node):
            return root
        else:
            father = search_for_father(node, root.left)
            if father is not None:
                return father
            else:
                return search_for_father(node, root.right)


def build_tree_from_leaf(node, root):
    if (node.left is not None) or (node.right is not None):
        print("zadany wieszcholek nie jest lisciem") 
        return None
    else:
        father = search_for_father(node, root)
        grand_father = search_for_father(father, root)
        if father.left is node:
            if grand_father.left is father:
                grand_father.left = None
                # father.left = None
                node.left = father  # nie ma znaczenia czy lewa czy prawa
                father.left = grand_father
            else:
                grand_father.right = None
                # father.left = None
                node.left = father  # nie ma znaczenia czy lewa czy prawa
                father.left = grand_father
        else:
            if grand_father.left is father:
                grand_father.left = None
                # father.right = None
                node.left = father  # nie ma znaczenia czy lewa czy prawa
                father.right = grand_father
            else:
                grand_father.right = None
                # father.rigth = None
                node.left = father  # nie ma znaczenia czy lewa czy prawa
                father.right = grand_father




if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    x = int(input("podaj liscia (od 4-7)"))
    # for i in range(1, 8):
    #     x = (search_for_node(i, root))
    #     print(search_for_father(x, root))
    node = search_for_node(x, root)
    build_tree_from_leaf(node, root)
    root = node
    print(root)
    traverse_preorder(root)  # sprawdzenie drzewa
    print("-------")
    traverse_postorder(root)
