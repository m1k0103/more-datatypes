import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Stack:
    def __init__(self,max_size):
        self.stack = [] 
        self.max_size = max_size

    def push(self,value):
        if len(self.stack) == self.max_size:
            logging.info(f"Push of value {value} failed.")
            return False
        else:
            logger.info(f"Pushing value: {value}")
            self.stack.append(value)
            return True

    def pop(self):
        if len(self.stack) == 0:
            logger.info(f"Popping failed.")
            return False
        else:
            logger.info(f"Popping value {self.stack[-1:]}")
            del self.stack[-1:]
            return True

    def display(self):
        print(self.stack)
        return
