from linked_list import LinkedList


class LLQueue:
    def__init__(self):
        self.storage = LinkedList()

    # adds a value to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
    # removes a value from the front of the queue

    def dequeue(self):
        return self.storage.remove_head()
