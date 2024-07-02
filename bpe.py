def train(self, text, vocab_size, verbose=False):
    assert vocab_size>=256
    num_merges = vocab_size-256

    #input text processing
    text_bytes = text.encode("utf-8")
    ids = list(text_bytes) 

    #merging most common pairs
    merges = {} #(int, int)->(int)


# def encode(self, text):
# def decode(self, ids):