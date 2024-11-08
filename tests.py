from more_datatypes import Stack, Queue

# check stack length
assert Stack(5).max_size == 5

# check stack functions
s = Stack(2)
assert s.push("value") == True # if pushed correctly
assert s.pop() == True # if pops correctly
assert s.pop() == False # if pop fails when empty
s.push("a")
s.push("b")
assert s.push("c") == False # if push fails when full

# tests stack values
assert Stack(4).push(None) == True # if None tries to get pushed, should still work


### Queue

# check queue length
assert Queue(5).max_length == 5

#check stack funcs
q = Queue(2)
assert q.enqueue("a") == True
assert q.dequeue() == True

q.enqueue("a")
q.enqueue("b")
assert q.enqueue("c") == False # if queue is full
assert Queue(5).dequeue() == False # if queue is empty