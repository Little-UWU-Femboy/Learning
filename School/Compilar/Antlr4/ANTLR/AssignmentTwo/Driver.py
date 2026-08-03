import sys

from antlr4 import *
from logoLexer import logoLexer
from logoParser import logoParser

from SVGEngine import SVGEngine
from Visitor import Visitor


def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 700

    input_text = sys.stdin.read()
    if not input_text:
        return

    input_stream = InputStream(input_text)
    lexer = logoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = logoParser(stream)

    engine = SVGEngine(size, size)
    visitor = Visitor(engine)

    engine.open()

    while parser.getCurrentToken().type != Token.EOF:
        stmt_ctx = parser.stmt()
        if stmt_ctx is not None:
            visitor.visit(stmt_ctx)

    engine.close()


if __name__ == "__main__":
    main()
