class Tokenizer:
    def __init__(self):
        self.vocabulary = {}
        self.inverse_vocabulary = {}
        self.token_count = 0

    def tokenize(self, text):
        tokens = text.split()
        return tokens

    def build_vocabulary(self, texts):
        for text in texts:
            tokens = self.tokenize(text)
            for token in tokens:
                if token not in self.vocabulary:
                    self.vocabulary[token] = self.token_count
                    self.inverse_vocabulary[self.token_count] = token
                    self.token_count += 1

    def encode(self, text):
        tokens = self.tokenize(text)
        return [self.vocabulary[token] for token in tokens if token in self.vocabulary]

    def decode(self, token_ids):
        return ' '.join(self.inverse_vocabulary[token_id] for token_id in token_ids if token_id in self.inverse_vocabulary)