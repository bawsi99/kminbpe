

#returns count of each consecutive pairs of token 
def get_stats(ids, counts=None):
    counts={}  # initialization if counts = None
    for pair in zip(ids,ids[1:]):
        if pair not in counts:
            counts[pair]=1
        else:
            counts[pair]+=1
    return counts

def merge(ids, pair, idx):
    new_tokens=[]
    i=0
    while i<len(ids):
        if i<len(ids)-1 and (ids[i], ids[i+1]) == pair:
            new_tokens.append(idx)
            i+=1
        else:
            new_tokens.append(ids[i])
        i+=1
    return new_tokens


    
    