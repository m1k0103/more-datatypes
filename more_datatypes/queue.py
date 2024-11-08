class Queue:
    def __init__(self,max_length):
        self.max_length = max_length
        self.queue = [None * max_length]
        self.front = 0
        self.back = 1
    
    def enqueue(self):
        if self.back == self.front:
            pass
        pass

    def dequeue(self):
        pass