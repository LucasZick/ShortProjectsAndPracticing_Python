
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

    def listPrint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insertAsFirst(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insertAtMid(self, lastNode, newData):
        assert lastNode, "Nodo anterior precisa existir na lista."

        newNode = Node(newData)
        newNode.next = lastNode.next
        lastNode.next = newNode

    def search(self, valor):
        actual = self.head
        while actual and actual.data != valor:
            actual = actual.next
        return actual

    def remove(self, valor):
        assert self.head, "Impossível remover valor de lista vazia."

        if self.head.data == valor:
            self.head = self.head.next
        else:
            last = None
            actual = self.head
            while actual and actual.data != valor:
                last = actual
                actual = actual.next
            if actual:
                last.next = actual.next
            else:
                last.next = None


if __name__ == '__main__':
    lista = LinkedList()

    # TESTING INSERT

    for i in range(10):
        lista.insertAsFirst(i)
    lista.listPrint()

    # TESTING REMOVE

    # lista.listPrint()
    # print('_________________________________')
    # lista.remove(9)
    # lista.listPrint()

    # TESTING SEARCH

    # for i in range(22, -4, -2):
    #    elemento = lista.search(i)
    #    if elemento:
    #        print("Elemento {0} presente na lista!".format(i))
    #    else:
    #        print("Elemento {0} não encontrado.".format(i))
