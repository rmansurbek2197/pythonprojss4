class HTMLTokenizer:
    def __init__(self, html):
        self.html = html
        self.index = 0
        self.tokens = []

    def tokenize(self):
        while self.index < len(self.html):
            if self.html[self.index].isspace():
                self.index += 1
            elif self.html[self.index] == '<':
                self.parse_tag()
            elif self.html[self.index] == '>':
                self.index += 1
            else:
                self.parse_text()
        return self.tokens

    def parse_tag(self):
        tag = ''
        self.index += 1
        while self.html[self.index] != '>' and self.index < len(self.html):
            if self.html[self.index] == ' ':
                self.tokens.append(('tag', tag))
                self.parse_attributes()
                return
            tag += self.html[self.index]
            self.index += 1
        self.tokens.append(('tag', tag))
        self.index += 1

    def parse_attributes(self):
        while self.index < len(self.html) and self.html[self.index] != '>':
            attribute = ''
            self.index += 1
            while self.html[self.index] != '=' and self.html[self.index] != '>' and self.index < len(self.html):
                attribute += self.html[self.index]
                self.index += 1
            if self.html[self.index] == '=':
                self.index += 1
                value = ''
                if self.html[self.index] == '"':
                    self.index += 1
                    while self.html[self.index] != '"' and self.index < len(self.html):
                        value += self.html[self.index]
                        self.index += 1
                    self.index += 1
                self.tokens.append(('attribute', attribute, value))
        self.index += 1

    def parse_text(self):
        text = ''
        while self.html[self.index] != '<' and self.index < len(self.html):
            text += self.html[self.index]
            self.index += 1
        self.tokens.append(('text', text))

    def print_tokens(self):
        for token in self.tokens:
            print(token)

tokenizer = HTMLTokenizer('<html><body><h1>Hello World</h1></body></html>')
tokenizer.tokenize()
tokenizer.print_tokens()