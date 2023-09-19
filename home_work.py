

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
        Удаление узла дерева 

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
            self.printTree(node.left)
            print(node.value)
            self.printTree(node.right)


    def countNode(self, node):
        if node == None:
            return 0
        return self.countNode(node.left) + self.countNode(node.right) + 1   

    def deleteElement(self, value):
        res = self.search(self.root, value)
        if res[0] is not None:
            # если у узла нет потомков (корень не удалять если нет потомков)
            if res[0].left == None and res[0].right == None:
                # если у выбранного элемента есть родитель
                if res[1] is not None:
                    if value > res[1].value:
                        res[1].right = None
                    else: 
                        res[1].left = None
                else:
                    return print(f'узел {value} является корнем (других элементов нет)')
            
            # у узла есть потомоки слева
            if res[0].left != None and res[0].right == None:
                    resChild = self.search(self.root, res[0].left.value)
                    res[0].value = resChild[0].value
                    res[0].left = resChild[0].left

            # если у узла есть потомоки справа
            if res[0].left == None and res[0].right != None:
                    resChild = self.search(self.root, res[0].right.value)
                    res[0].value = resChild[0].value
                    res[0].right = resChild[0].right

            # если у узла есть потомки справа и слева
            if res[0].left != None and res[0].right != None:
                    resChildLeft = self.search(self.root, res[0].left.value)
                    resChildRight = self.search(self.root, res[0].right.value)
                    res[0].value = resChildLeft[0].value
                    res[0].right = resChildRight[0]
                    res[0].left = resChildLeft[0].left

            print(f'узел {value} удален')
        else:
           print(f'узел {value} не найден') 




bt = BinaryTree(6)
bt.add(3)
bt.add(7)
bt.add(2)
bt.add(1)
bt.add(0)
bt.add(4)
bt.add(5)
bt.add(8)

# bt.printTree(bt.root)

print(bt.search(bt.root, 3)[0])
print(bt.search(bt.root, 3)[1])
bt.deleteElement(3)
print(bt.search(bt.root, 2)[0])
print(bt.search(bt.root, 2)[1])

# print(bt.root)
# print(bt.search(bt.root, 9)[0])
# print(bt.root.left)
# print(bt.root.right)




# print(bt.countNode(bt.root))