class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f'Node({self.value})'


def parse(tokens):
    parse_tree = Node('program')
    current_node = parse_tree

    for token_type, token_value in tokens:
        if token_type == 'KEYWORD':
            current_node.add_child(Node(token_value))
        elif token_type == 'OPERATOR':
            current_node.add_child(Node(token_value))
        elif token_type == 'IDENTIFIER':
            current_node.add_child(Node(token_value))
        elif token_type == 'PUNCTUATION':
            current_node.add_child(Node(token_value))
        elif token_type == 'NUMBER_LITERAL':
            current_node.add_child(Node(token_value))
        elif token_type == 'STRING_LITERAL':
            current_node.add_child(Node(token_value))
        elif token_type == 'NEWLINE':
            # Start a new statement
            current_node = Node('statement')
            parse_tree.add_child(current_node)
        elif token_type == 'WHITESPACE':
            pass  # Ignore whitespace
        else:
            raise ValueError(f'Unknown token type: {token_type}')

    return parse_tree


def print_tree(node, depth=0, output_file=None):
    if output_file is None:
        print('  ' * depth + str(node))
    else:
        output_file.write('  ' * depth + str(node) + '\n')
    for child in node.children:
        print_tree(child, depth + 1, output_file)


def main():
    with open('tokenstream.txt', 'r') as f:
        token_stream = [line.strip().split(': ') for line in f]

    parse_tree = parse(token_stream)
    with open('parsetree.txt', 'w') as output_file:
        print_tree(parse_tree, output_file=output_file)


if __name__ == '__main__':
    main()
