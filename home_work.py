

class Node:
    """Класс Node используется для создания элемента дерева

    Methods
    -------
    __init__()
        инициализация класса Node

    __str__()
        преобразование в строку  
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:

    """BinaryTree используется для создания бинарного дерева

    Methods
    -------
    __init__()
        Инициализация дерева

    add()
        Добавление элемента в дерево 

    search()
        Поиск элемента в дереве
    
    printTree()
        Вывод в консоль всего дерева начиная с корня (Обход двоичного дерева сверху вниз)

    countNode()
        Подсчет количества узлов дерева
    
    deleteElement()
        Удаление узла дерева (с учетом, что у узла будет не более двух потомков, один справа другой слева)
        (В противном случае нужно где-то хранить всех потомков удаляемого узла или делать рекурсию, пока не знаю как...)

    
    """

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node, value, parent=None):
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)
        
    def printTree(self, node):
        if node:
            print(node.value)
            self.printTree(node.left)
            self.printTree(node.right)

     # подсчет количества узлов дерева
    def countNode(self, node):
        if node == None:
            return 0
        return self.countNode(node.left) + self.countNode(node.right) + 1   

    def deleteElement(self, value):
        res = self.search(self.root, value)
        childLeft = res[0].left
        childRight = res[0].right
        parent = res[1].value
        if res[0] is None:
            print("нет такого узла")
        else:
            # если у узла нет потомков
            if childLeft == None and childRight == None:
                if value > parent:
                    res[1].right = None
                else: 
                    res[1].left = None
            # у узла есть один потомок слева
            if childLeft != None and childRight == None:
                if value > parent:
                    res[1].right = childLeft
                else: 
                    res[1].left = childLeft
            # если у узла есть один потомок справа
            if childLeft == None and childRight != None:
                if value > parent:
                    res[1].right = childRight
                else: 
                    res[1].left = childRight
            # если у узла есть по одному потомку справа и слева 
            if childLeft != None and childRight != None:
                if value > parent:
                    res[1].right = childLeft
                else: 
                    res[1].left = childLeft
                res = self.search(self.root, res[0].value)
                res[1].right = childRight
               
            print(f'узел {value} удален')




bt = BinaryTree(5)
bt.add(3)
bt.add(7)
bt.add(2)
bt.add(4)
bt.add(6)
bt.add(8)

print(bt.search(bt.root, 3)[0])
print(bt.search(bt.root, 3)[1])
bt.deleteElement(3)
print(bt.search(bt.root, 2)[0])
print(bt.search(bt.root, 2)[1])

# print(bt.root)
# print(bt.search(bt.root, 9)[0])
# print(bt.root.left)
# print(bt.root.right)


# bt.printTree(bt.root)

# print(bt.countNode(bt.root))