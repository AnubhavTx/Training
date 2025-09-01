import math 


expr = input("Enter the expression:")


def tokenize(expr):
    tokens = []
    number_buffer = ''
    operations = set(["+","-","%","*"])

    for ch in expr:
        if ch.isdigit() or ch == '.':
            number_buffer += ch
        
        elif ch in operations:
            if number_buffer :
                tokens.append(number_buffer)
                number_buffer = ''
            tokens.append(ch)

        elif ch == " ":
            if number_buffer :
                tokens.append(number_buffer)
                number_buffer = ''

        else :
            pass

    if number_buffer:
        tokens.append(number_buffer)

    return tokens

def combine_operators(op1, op2):
    if op1 == '-' and op2 == '-':
        return '+'
    elif op1 == '+' and op2 == '+':
        return '+'
    elif op1 == '+' and op2 == '-':
        return '-'
    elif op1 == '-' and op2 == '+':
        return '-'
    else:
        return None
    
def combine_operators_tokens(tokens):
    combined_tokens = []
    i = 0 
    while i<len(tokens):
        token = tokens[i]
        if token in ["+","-"]:
            if i+1<len(tokens) and tokens[i+1] in ["+","-"]:
                new_op = combine_operators(tokens[i],tokens[i+1])
                if new_op is not None:
                    combined_tokens.append(new_op)
                    i+=2
                    continue
                else:
                    combined_tokens.append(token)
            else:
                combined_tokens.append(token)
        else:
            combined_tokens.append(token)

        i += 1
    return combined_tokens

def calculate(tokens):
    result = float(tokens[0])
    i = 1

    while i < len(tokens):
        op = tokens[i]
        num = float(tokens[i + 1])

        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if num == 0:
                raise ValueError("Division by zero!")
            result /= num
        else:
            raise ValueError(f"Unknown operator: {op}")

        i += 2  

    return result


tokens = tokenize(expr)
tokens = combine_operators_tokens(tokens)

print("Tokens:", tokens)

result = calculate(tokens)
print("Result:", result)