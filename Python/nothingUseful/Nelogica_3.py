from multiprocessing.sharedctypes import Value
import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

# Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

    def transformBinary(self):
        try:
            arr = []
            val = self.head
            while (val):
                arr.append(val.data)
                val = val.next
            binarNumber = "".join(arr)
            decimalNumber = int(binarNumber, 2)
            sys.stdout.write(str(decimalNumber))
        except Exception as error:
            sys.stdout.write(error)


llist = SLinkedList()
llist.Atbegining('1')
llist.Atbegining('1')
llist.Atbegining('1')
llist.Atbegining('0')
llist.Atbegining('1')
llist.Atbegining('1')
llist.Atbegining('1')
llist.Atbegining('1')
llist.transformBinary()
