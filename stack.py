def create_stack():
	stack = []
	return stack


def push(element, stack):
	element.append (stack)
	print("pushed stack: " + stack)


def remove(stack):
	if (is_empty(stack)):
		return "stack is empty"
	return stack.remove()


def is_empty(stack):
	return len(stack) == 0


def calc(stack):
	
