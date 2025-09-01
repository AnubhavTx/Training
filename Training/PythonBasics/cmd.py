import argparse
import operator
import sys

# Mapping from operation names or symbols to actual Python functions
OPERATION_MAP = {
    'plus': operator.add,
    '+': operator.add,
    '++': operator.add,
    'add': operator.add,

    'minus': operator.sub,
    '-': operator.sub,
    '--': operator.sub,
    '+-': operator.sub,
    '-+': operator.sub,
    'subtract': operator.sub,

    'multiply': operator.mul,
    '*': operator.mul,
    'x': operator.mul,

    'divide': operator.truediv,
    '/': operator.truediv
}

def main():
    parser = argparse.ArgumentParser(description='Perform an operation on a list of numbers.')
    parser.add_argument('--operation', type=str, required=True, help='Operation to perform (e.g., plus, --, multiply)')
    parser.add_argument('--list', type=float, nargs='+', required=True, help='List of numbers to process')

    args = parser.parse_args()
    print(f"Raw input for operation: {args.operation!r}")

    # Strip quotes and whitespace, then convert to lowercase
    op_str = args.operation.strip('"').strip("'").strip().lower()

    numbers = args.list

    # Get the function for the given operation
    op_func = OPERATION_MAP.get(op_str)

    if not op_func:
        print(f"Unknown operation: {op_str}")
        sys.exit(1)

    # Apply operation cumulatively
    result = numbers[0]
    for num in numbers[1:]:
        result = op_func(result, num)

    print(f"Result: {result}")

if __name__ == '__main__':
    main()