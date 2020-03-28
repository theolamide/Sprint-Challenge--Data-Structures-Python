from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check length

        # If length less than capacity
        if self.storage.length < self.capacity:
            # add item to tail and set tail to current
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        # If length equal to capacity
        elif self.storage.length == self.capacity:
            if not self.current.next:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head

            else:
                self.current.next.delete()
                self.current.insert_after(item)
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        oldest = self.storage.head

        while oldest:
            list_buffer_contents.append(oldest.value)
            oldest = oldest.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
