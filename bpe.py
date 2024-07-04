from base import get_stats,merge


class BasicTokenizer():
    def __init__(self):
        super().__init__()

    def train(self, text, vocab_size, verbose=False):
        assert vocab_size>=256
        num_merges = vocab_size-256

        #input text processing
        text_bytes = text.encode("utf-8")
        ids = list(text_bytes) #converting text into a list of integers in the range 0-255, that is from unicode to utf-8 , characters which cannot be represented in a byte , consume multiple bytes 

        #merging most common pairs
        merges = {} #(int, int)->(int)
        vocab = {idx: bytes([idx]) for idx in range(256)} #creating an initial vocab of 256 tokens and storing their bytes 

        for i in range(num_merges):
            stats = get_stats(ids)
            if not stats:
                break 
            pair=max(stats, key = stats.get)
            idx = len(vocab)
            ids = merge(ids, pair, idx)
            merges[pair]=idx
            vocab[idx] = vocab[pair[0]] + vocab[pair[1]]
    
            if verbose:
                print(f'merge {i+1}/{num_merges}: {pair} -> {idx} ({vocab[idx]}) had {stats[pair]} occurences')
        
        self.merges = merges # used in encode
        self.vocab = vocab # used in decode
    def encode(self, text):

        mergecopy = sorted(self.merges, key=self.merges.get)
        ids = list(text.encode("utf-8"))
        for i in mergecopy:       
            ids = merge(ids, i, self.merges[i])
        return ids
        
    def decode(self, ids):

        str = b"".join(self.vocab[i] for i in ids)
        return str.decode("utf-8",errors="replace")




text='Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. AHAHDBAHBaasm sadvcaaajh jsaccccccccbh hhhhhhhhhhcbsjah gascgjasbhjasbja jhbashbhj bhasbhjasbxhjas hbashbhb jhabhjabhjx ab'
# ids = list(text.encode("utf-8"))
# print(len(ids))
# print(get_stats(ids))
BT = BasicTokenizer()
print(BT.train(text=text, vocab_size=260, verbose=True))
k=BT.encode('Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄')
m = BT.decode(k)
print(m == 'Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄')