iterateble_data = dataframe.rdd.toLocalIterator()

# data cleaning
for index in iterateble_data:
    index['name'] = index['name'].lower()
    index['name'] = index['name'].translate(string.maketrans("!#$%&\()*+,/:;<=>?@[\\]^_`{|}~]", ' '))
    
    
vocabulary = set()

for index in iterateble_data:
    vocabulary.update(index['name'].split(' '))
    
vocabulary = list(vocabulary)
tfidf = TfidfVectorizer(vocabulary=vocabulary, dtype=np.float32)
tfidf.fit(dataframe['name'])
tfidf_tran = tfidf.transform(dataframe['name'])
