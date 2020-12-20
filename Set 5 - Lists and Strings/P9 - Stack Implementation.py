print('Stack Implementation')

stack_list = [2,'beamer', 23, True, 0.9, 'seven', 'big', 1337]

def push(stack, value):
	stack.append(value)
    
def pop(stack):
    if len(stack) > 0:
        val_to_return = stack[len(stack) - 1]
        del stack[len(stack) - 1]
        return val_to_return
    else:
        return

def isempty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    
def peak(stack):
    if len(stack) == 0:
        return
    else:
        return stack[len(stack) - 1]
   