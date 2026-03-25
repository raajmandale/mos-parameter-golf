class Tokenizer:
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}

    def fit(self, text):
        words = text.split()
        vocab = sorted(set(words))
        self.word2idx = {w: i for i, w in enumerate(vocab)}
        self.idx2word = {i: w for w, i in self.word2idx.items()}

    def encode(self, text):
        return [self.word2idx[w] for w in text.split() if w in self.word2idx]

    def decode(self, tokens):
        return " ".join(self.idx2word[t] for t in tokens)
