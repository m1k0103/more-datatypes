import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Queue:
    def __init__(self,max_length):
        self.max_length = max_length
        self.queue = [None] * max_length
        self.front = 0
        self.back = 0
    
    def enqueue(self,data):
        if self.back == self.front and self.back == 0: # if empty
            if self.back == self.max_length+1: # if the back pointer has reached the max length
                self.back = 0
                self.queue[self.back] = data
                return True
            else:
                self.queue[self.back] = data
                self.back += 1
                return True

        elif self.back == self.front and self.queue[0] != None: # if full
            logging.info("queue is full. can't enqueue.")
            return False
        else: # everything else
            self.queue[self.back] = data
            self.back += 1
            return True
            

    def dequeue(self):
        if self.back == self.front and self.queue[0] == None:
            logging.info("queue is empty. cant dequeue.")
            return False
        else:
            if self.front == self.max_length:
                self.queue[self.front] = None
                self.front = 0
                return True
            else:
                self.queue[self.front] = None
                self.front += 1
                return True
