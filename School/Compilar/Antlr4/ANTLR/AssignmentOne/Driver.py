import sys

from antlr4 import *

from XMLLexer import XMLLexer


def makeTokens():
    input_data = sys.stdin.read()
    input_stream = InputStream(input_data)
    lexer = XMLLexer(input_stream)
    return lexer.getAllTokens()


def identify(token):
    text = token.text
    if token.type == XMLLexer.OPEN:
        return text[1:-1]
    if token.type == XMLLexer.CLOSE:
        return text[2:-1]
    return ""


def unmatched(stack):
    while stack:
        tag = stack.pop()
        print(f"ERROR: UNMATCHED-OPEN <{tag}>")


def run():
    tokens = makeTokens()
    stack = []

    for token in tokens:
        if token.type == Token.EOF:
            break

        match token.type:
            case XMLLexer.OPEN:
                name = identify(token)
                stack.append(name)

            case XMLLexer.CLOSE:
                name = identify(token)
                if not stack or stack[-1] != name:
                    error_msg = f"ERROR: UNMATCHED-CLOSE </{name}>"
                    if stack:
                        error_msg += f". Expecting </{stack[-1]}>"
                    print(error_msg)
                    return
                stack.pop()

            case XMLLexer.SELF | XMLLexer.TEXT:
                continue
    if stack:
        unmatched(stack)
    else:
        print("OK")


if __name__ == "__main__":
    run()
