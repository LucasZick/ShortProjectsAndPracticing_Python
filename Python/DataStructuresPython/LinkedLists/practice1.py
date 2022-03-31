
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
         print (printval.data)
         printval = printval.next
    
    def insertAsFirst(lista, newData):
        newNode = Node(newData)
        newNode.next = lista.head
        lista.head = newNode
    
    def insertAtMid(list, lastNode, newData):
        assert lastNode, "Nodo anterior precisa existir na lista."

        newNode = Node(newData)
        newNode.next = lastNode.next
        lastNode.next = newNode

    def search(self, valor):
        actual = self.head
        while actual and actual.data != valor:
            actual = actual.next
        return actual

lista = LinkedList()

for i in range(10):
    lista.insertAsFirst(i)

for i in range(21, -4, -2):
    elemento = lista.search(i)
    if elemento:
        print("Elemento {0} presente na lista!".format(i))
    else:
        print("Elemento {0} não encontrado.".format(i))

