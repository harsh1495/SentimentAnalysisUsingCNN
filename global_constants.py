with open("english.txt") as f:
    stopwords = [line.rstrip() for line in f]
    
embeddings = {}
with open("glove.twitter.27B.25d.txt", 'r', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = values[1:]
        embeddings[word] = vector