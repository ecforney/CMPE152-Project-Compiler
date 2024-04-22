import re

# Define token types using regular expressions
TOKEN_TYPES = [
    ('KEYWORD', r'\b(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b'),  # valid keywords in Python
    ('OPERATOR', r'(\+\+|\-\-|\=\=|\!\=|\>\=|\<\=|\*|\+|\-|\/|\%|\*\*|\=|\<|\>|\&\&|\|\|)'),  # valid operators in Python
    ('PUNCTUATION', r'(\(|\)|\[|\]|\{|\}|\,|\;|\:)'),  # valid punctuation characters in Python
    ('STRING_LITERAL', r'\".*?\"'),  # string literals
    ('NUMBER_LITERAL', r'\d+'),  # number literals
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # identifiers start with a letter or underscore, followed by letters, digits, or underscores
    ('NEWLINE', r'\n'),  # newline character
    ('WHITESPACE', r'\s+'),  # whitespace
    ('UNKNOWN', r'.'),  # unrecognized characters
]

def tokenize(input_text):
    tokens = []
    while input_text:
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(input_text)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    if token_type == 'NEWLINE':
                        tokens.append(('NEWLINE', f'<\'\\n\'>'))  # Change newline token format
                    else:
                        tokens.append((token_type, f'<\'{value}\'>'))
                break
        if not match:
            raise ValueError('Invalid input: ' + input_text)
        input_text = input_text[match.end():]
    return tokens

def main():
    with open('input.txt', 'r') as f:
        input_text = f.read()
    
    tokens = tokenize(input_text)
    
    # Writing token types and tokens to output.txt in columns
    with open('tokenstream.txt', 'w') as f:
        for token in tokens:
            f.write(f'{token[0]}: {token[1]}\n')

if __name__ == '__main__':
    main()
