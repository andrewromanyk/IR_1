import sortedcontainers as sc

def tokenize_expression(expression):
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    tokens = expression.split()

    final_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i] not in ['AND', 'OR', 'NOT', '(', ')']:
            final_tokens.append(tokens[i])
        else:
            final_tokens.append(tokens[i])
        i += 1
    return final_tokens


def boolean_to_rpn(expression):
    # Define operator precedence (higher value means higher precedence)
    precedence = {
        'OR': 1,
        'AND': 2,
        'NOT': 3,
        '(': 0  # Lowest precedence for processing
    }

    # Initialize output queue and operator stack
    output = []
    operators = []

    # Tokenize the input expression
    tokens = tokenize_expression(expression)

    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            # Process operators according to precedence
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence.get(token, 0)):
                output.append(operators.pop())
            operators.append(token)

        elif token == '(':
            operators.append(token)

        elif token == ')':
            # Pop operators until matching left parenthesis
            while operators and operators[-1] != '(':
                output.append(operators.pop())

            # Remove the left parenthesis
            if operators and operators[-1] == '(':
                operators.pop()

        else:
            # Token is an operand (search term)
            output.append(token)

    # Pop any remaining operators to the output
    while operators:
        output.append(operators.pop())

    return output


def bool_search(expression, method, files=sc.SortedSet([i for i in range(10)])):
    rpn = boolean_to_rpn(expression)

    stack = []

    for token in rpn:
        print(f"token: {token}")
        print(f"stack: {stack}")
        if token == "AND":
            first = stack.pop()
            second = stack.pop()
            stack.append(first.intersection(second))
        elif token == "OR":
            first = stack.pop()
            second = stack.pop()
            stack.append(first.union(second))
        elif token == "NOT":
            first = stack.pop()
            top = files
            stack.append(top.difference(first))
        else:
            stack.append(sc.SortedSet(method(token)))

    return stack.pop()