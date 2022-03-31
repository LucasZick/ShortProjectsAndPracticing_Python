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
    
    def removeRepeated(self, nonRepeatedList):
        assert self.head, "Impossível checar lista vazia."

        actual = self.head

        while actual and actual.data != None:
            nextOne = actual.next
            if actual.data in nonRepeatedList:
                self.remove(actual.data)
            else:
                nonRepeatedList.append(actual.data)
            actual = nextOne

if __name__ == '__main__':
    entryList = [8,90,12,312,2,14,8,17,21,90,2,2,2,2,31,12]
    nonRepeatedList = []

    lista = LinkedList()

    for i in entryList:
        lista.insertAsFirst(i)

    lista.removeRepeated(nonRepeatedList)
    lista.listPrint()
    
    

