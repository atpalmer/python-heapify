import random
import dataclasses


@dataclasses.dataclass
class Node(object):
    value: int
    left: object
    right: object


def tree_create():
    def tree(h):
        if h > 0:
            left = tree(h - 1)
            right = tree(h - 1)
        else:
            left = None
            right = None
        return Node(random.randint(1, 101), left, right)
    return tree(3)


def tree_heapify(node):
    if node.left:
        tree_heapify(node.left)
        if node.left.value < node.value:
            node.left.value, node.value = node.value, node.left.value
            tree_heapify(node.left)
    if node.right:
        tree_heapify(node.right)
        if node.right.value < node.value:
            node.right.value, node.value = node.value, node.right.value
            tree_heapify(node.right)


def tree_print(tree):
    def impl(tree):
        if tree is None:
            print('-', end='')
            return
        print(tree.value, '(', end='')
        impl(tree.left)
        print(') (', end='')
        impl(tree.right)
        print(')', end='')
    impl(tree)
    print()


def main():
    tree = tree_create()
    tree_print(tree)
    tree_heapify(tree)
    tree_print(tree)


if __name__ == '__main__':
    main()

