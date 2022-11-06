def create_stack():                 # Creating a stack
    stack = []
    return stack
def check_empty(stack):             # Creating empty stack
    return len(stack) == 0
def push(stack, item):              # Adding items into the stack
    stack.append(item)
    print("pushed item in the list : ",item)
def pop(stack):                     # Remov the element from the stack
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
print("popped item List In array : " + pop(stack))
print("stack after popping element: " + str(stack))
print("popped item List In Array : " + pop(stack))
print("stack after popping element: " + str(stack))