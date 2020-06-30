class lexer:
    def __init__(self, data):
        self.numbers = ["0",'1','2','3','4','5','6','7','8','9']
        self.data     = data
        self.tokens   = []
        self.keywords = [
            'add',
            'rem',
            'sub',
            'mul',
            'div',
            'display',
            '#',
            'fact',
            'fib',
            'go'
        ]
    def tokenizer(self):
        for loc in self.data:
            tmp = []
            tid = ''
            for l in loc:
                if l == '"' and tid == '':
                    tid = 'char'
                    tmp = []
                elif l == '"' and tid == 'char':
                    self.tokens.append({'id': tid, 'value': ''.join(tmp)})
                    tid = '' 
                    tmp = []
                elif l == ':':
                    self.tokens.append({'id': 'label', 'value': ''.join(tmp)})
                    tmp = []
                elif ''.join(tmp) in self.keywords:
                    self.tokens.append({'id': 'keyword', 'value': ''.join(tmp)})
                    tmp = []
                elif l == '\n':
                    if len(tmp) > 0:
                        self.tokens.append({'id':'atom','value':''.join(tmp)})
                elif l == ' ' and tid != 'char':
                    continue
                else:
                    tmp.append(l)
