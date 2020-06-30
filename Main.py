from lexer import lexer
from Parser import Parser
from Evaluator import Evaluator
def main():
    a = input()
    filename = a
    file = open(filename, "r")
    Lexer = lexer(file)
    Lexer.tokenizer()
    parser = Parser(Lexer.tokens)
    parser.build_AST()
    evaluator = Evaluator(parser.AST)
    evaluator.run(parser.AST)
    
if __name__ == "__main__":
    main() 
