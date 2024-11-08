from more_datatypes import Stack

# tests stack length
assert Stack(5).max_size == 5

# tests stack functions
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

