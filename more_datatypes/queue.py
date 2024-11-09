class Queue:
    def __init__(self,max_length):
        self.max_length = max_length
        self.queue = [None * max_length]
        self.front = 0
        self.back = 0
    
    def enqueue(self,data):
        if self.back == self.front and self.back == 0: # if empty
            if self.back == self.max_length:
                self.back = 0
                self.queue[self.back] = data

            else:
                self.queue[self.back] = data
                self.back += 1
        elif self.back == self.front and #uhhhhhh too late for this
        pass

    def dequeue(self):
        if self.back == self.front and  # bla bla bla logic 
        pass

    def display(self):
        print(self.queue)
        return