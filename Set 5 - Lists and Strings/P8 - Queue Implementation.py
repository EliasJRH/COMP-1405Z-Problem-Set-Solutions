('Queue Implementation')
max_size = 10
queue_list = [2,'beamer', 23, True, 0.9, 'seven', 'big', 1337]


def enqueue(queue, val_to_add):
    if len(queue) < max_size:
        queue.append(val_to_add)
        return True
    else:
        return False
    
def dequeue(queue):
    if len(queue) >= 1:
        val_to_return = queue[0]
        del queue[0]
        return val_to_return
    else:
        return
    
def peek(queue):
    if len(queue) > 1:
        return queue[0]
    else:
        return
    
def isempty(queue):
    if len(queue) > 0:
        return False
    else:
        return True
    
def multienqueue(queue, items):
    succesful_enqueues = 0
    for x in range(len(items)):
        if enqueue(queue,items[x]) == False:
            return succesful_enqueues
        else:
            succesful_enqueues += 1
    
def multidequeue(queue, number):
    queue_to_return = []
    for x in range(number):
        val_returned = dequeue(queue)
        if val_returned == None:
            break
        else:
            queue_to_return.append(val_returned)
    return queue_to_return