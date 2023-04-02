from typing import Optional

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)
        return

    def reverse(self) -> Optional[Node]:
        pre, head = None, self.head
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr
        self.head = pre

    def show(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        return None

if __name__ == '__main__':
    linkList = LinkedList()
    linkList.insert(1)
    linkList.insert(2)
    linkList.reverse()
    linkList.show()
