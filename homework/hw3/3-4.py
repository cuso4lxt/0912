##实现一个链表，能够完成增删改查的操作

# Node类代表节点
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None # 头节点，默认为None

    def insert(self, data):  # 插入
        new_node = Node(data)
        new_node.next = self.head  # 新节点的next指向头节点
        self.head = new_node  # 将新节点设置为头节点

    def delete(self, key):
        temp = self.head  # 遍历链表的指针

        if temp != None:
            if temp.data == key:  # 删除的节点是头节点
                self.head = self.head.next
                temp = None
                return

        prev = None  #  保留上一个节点
        while temp != None:
            if temp.data == key:  # 找到了要删除的节点
                break
            prev, temp = temp, temp.next

        if temp == None:  # 没有找到要删除的（链表里没有）
            return

        prev.next = temp.next  # 挂链
        temp = None  # 删除要删的节点

    def update(self, old_key, new_key):
        temp = self.head  #遍历链表的指针
        while temp != None:
            if temp.data == old_key:
                temp.data = new_key  #改
                return
            temp = temp.next

    def find(self, key):
        temp = self.head
        while temp != None:
            if temp.data == key:
                return temp
            temp = temp.next

        return None
def run_linklist():
    llist = LinkList()

    while True:
        user_input = input("请输入操作和数据（insert/update/delete/find/quit），用空格分隔\n")
        command = user_input.split(" ")  # 提取用户操作

        operation = command[0].lower()  # 提取操作名，转换为小写

        if operation == 'quit':
            break

        if operation == 'insert':
            data = int(command[1])
            llist.insert(data)

        elif operation == 'update':
            old_key = int(command[1])
            new_key = int(command[2])
            llist.update(old_key,new_key)

        elif operation == 'delete':
            key = int(command[1])
            llist.delete(key)

        elif operation == 'find':
            key = int(command[1])
            node = llist.find(key)
            if node:
                print(f"找到了数据为{node.data}的节点。")
            else:
                print("没有找到该节点")

run_linklist()





