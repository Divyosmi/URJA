class Evaluator:
    def __init__(self, AST):
        print("Hi, from urja , wish you all the best")
        self.AST = AST
    def run(self, node):
        if isinstance(node, list):
            for n in node:
                for k, v in n.items():
                    self.execute([k, v])
        elif isinstance(node, dict):
            for k, v in node.items():
                self.execute([k, v])
    def execute(self, loc):
        if isinstance(loc[1], list):
            self.run(loc[1])
        elif loc[0] == 'display':
            self.display(loc[1])
        elif loc[0] == 'go':
            self.go(loc[1])
        elif loc[0] == 'add':
            self.add(loc[1])
        elif loc[0] == 'sub':
            self.sub(loc[1])
        elif loc[0] == 'mul':
            self.mul(loc[1])
        elif loc[0] == 'div':
            self.div(loc[1])
        elif loc[0] == 'rem':
            self.rem(loc[1])
        elif loc[0] == '#':
            self.comm(loc[1])
        elif loc[0] == 'fact':
            self.fact(loc[1])
        elif loc[0] == 'fib':
            self.fib(loc[1])
    def go(self, v):
        self.run(v)
    def comm(self, v):
        pass
    def fact(self, v):
        a = 1 
        for i in range(1,int(v) + 1):
            a *= i
        print(a)
    def fib(self, v):
        v = int(v)
        a = 0
        b = 1
        if v == 0:
            pass
        elif v == 1:
            print(v - 1)
        else:
            l = []
            l.append(a)
            l.append(b)
            for i in range(2, v + 1):
                c = a + b
                a = b
                b = c
                l.append(b)
            print(l)
    def add(self, v):
        w = float(input())
        print(float(v) + w)
    def rem(self, v):
        w = float(input())
        print(float(int(v) % int(w)))
    def mul(self, v):
        w = float(input())
        print(float(v) * w)
    def div(self, v):
        w = float(input())
        print(float(v) / w)
    def sub(self, v):
        w = float(input())
        print(float(v) - w)         
    def display(self, v):
        print(v)
