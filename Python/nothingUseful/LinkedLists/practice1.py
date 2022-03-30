
class Node:
    def __init__(self, data=0, nextData=None):
        self.data = data
        self.next = nextData

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
         print (printval.data)
         printval = printval.nextData
    
    def insertAsFirst(list, newData):
        newNode = Node(newData)
        newNode.nextData = list.head
        list.head = newNode
    
    def insertAtMid(lista, lastNode, newData):
        assert lastNode, "Nodo anterior precisa existir na lista."

        newNode = Node(newData)
        newNode.nextData = lastNode.nextData
        lastNode.nextData = newNode

lista = LinkedList()
lista.insertAsFirst(5)
lista.insertAsFirst(10)
#lista.insertAsFirst(20)
#lista.insertAsFirst(10)
#lista.insertAsFirst(40)
#lista.insertAsFirst(10)

lista.listPrint()

lastNode = lista.head
lista.insertAtMid(lastNode,3)

lastNode = lista.head
lista.insertAtMid(lastNode,20)

print("Inserindo um novo elemento depois de um outro:", lista)

lista.listPrint()