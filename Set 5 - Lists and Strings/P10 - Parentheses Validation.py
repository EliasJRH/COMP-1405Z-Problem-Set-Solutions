print('Parantheses Validation')

def isvalid(string):
    open_round = 0
    open_curly = 0
    open_square = 0
    bracket_stack = []
    for x in string:
        if x == '(':
            open_round += 1
            bracket_stack.append('O')
        elif x == ')':
            open_round -= 1
            if bracket_stack.pop(len(bracket_stack) - 1) != 'O':
                return False
        elif x == '{':
            open_curly += 1
            bracket_stack.append('C')
        elif x == '}':
            open_curly -= 1
            if bracket_stack.pop(len(bracket_stack) - 1) != 'C':
                return False
        elif x == '[':
            open_square += 1
            bracket_stack.append('S')
        elif x == ']':
            open_square -= 1
            if bracket_stack.pop(len(bracket_stack) - 1) != 'S':
                return False
        if open_round < 0 or open_curly < 0 or open_square < 0:
            return False
    if open_round != 0 or open_curly != 0 or open_square != 0:
            return False
    else:
        return True
        
print(isvalid('()[]'))