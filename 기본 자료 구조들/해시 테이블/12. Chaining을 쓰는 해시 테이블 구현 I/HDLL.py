class Node:
    """��ũ�� ����Ʈ�� ��� Ŭ����"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # ���� ��忡 ���� ���۷���
        self.prev = None  # �� ��忡 ���� ���۷���


class LinkedList:
    """��ũ�� ����Ʈ Ŭ����"""
    def __init__(self):
        self.head = None  # ��ũ�� ����Ʈ�� ���� �� ���
        self.tail = None  # ��ũ�� ����Ʈ�� ���� �� ���
        

    def find_node_with_key(self, key):
        """��ũ�� ����Ʈ���� �־��� �����͸� �����ִ� ��带 �����Ѵ�. ��, �ش� ��尡 ������ None�� �����Ѵ�"""
        iterator = self.head   # ��ũ�� ����Ʈ�� ���� ���� �ʿ��� ��� ����

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None


    def append(self, key, value):
        """��ũ�� ����Ʈ �߰� ���� �޼ҵ�"""
        new_node = Node(key, value)

        # �� ��ũ�� ����Ʈ��� head�� tail�� ���� ���� ���� ����
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # �̹� ��尡 ������
        else:
            self.tail.next = new_node  # ������ ����� ���� ���� �߰�
            new_node.prev = self.tail
            self.tail = new_node  # ������ ��� ������


    def delete(self, node_to_delete):
        """���� ��ũ�� ����Ʈ ���� ���� �޼ҵ�"""

        # ��ũ�� ����Ʈ���� ������ ���� �����͸� ������ ��
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # ��ũ�� ����Ʈ ���� �� ������ ������ ��
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # ��ũ�� ����Ʈ ���� �� ������ ������ ��
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # �� ��� ���̿� �ִ� ������ ������ ��
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.value


    def __str__(self):
        """��ũ�� ����Ʈ�� ���ڿ��� ǥ���ؼ� �����ϴ� �޼ҵ�"""
        res_str = ""

        # ��ũ�� ����Ʈ �ȿ� ��� ��带 ���� ���� ����. �ϴ� ���� �� ���� �����Ѵ�.
        iterator = self.head

        # ��ũ�� ����Ʈ ������ ����
        while iterator is not None:
            # �� ����� �����͸� �����ϴ� ���ڿ��� �����ش�
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next  # ���� ���� �Ѿ��

        return res_str
    
    