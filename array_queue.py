class LLQueue:
    def__init__(self):
        self.storage = []

    # adds a value to the back of the queue
    def enqueue(self, value):
        self.storage.append(value)  # 0(1) run time
    # removes a value from the front of the queue

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(0)
