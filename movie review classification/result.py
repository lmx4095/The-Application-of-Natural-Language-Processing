import nltk
import random
from nltk.corpus import PlaintextCorpusReader
root_all=r"E:\SILS Course\INLS 613\hw1\train"
file_all=r"train_all\.txt"
p_all=PlaintextCorpusReader(root_all, file_all)
print(p_all.words())

corpus_root = r"E:\SILS Course\INLS 613\hw1\train\data cleaning\pos"
corpus_root_neg= r"E:\SILS Course\INLS 613\hw1\train\data cleaning\neg"
file_pattern = r".*/.*\.txt"
p_pos = PlaintextCorpusReader(corpus_root, file_pattern)
p_neg = PlaintextCorpusReader(corpus_root_neg, file_pattern)
documents = [(list(p_pos.words('1.txt')), "positive")]
for num in range(2,1001):
    s = str(num) + '.txt'
    documents = documents+[(list(p_pos.words(s)), "positive")]
for num in range(1001,2001):
    s = str(num) + '.txt'
    documents = documents + [(list(p_neg.words(s)), "negative")]
random.shuffle(documents)
print(documents[:1])

all_words = nltk.FreqDist(w.lower() for w in p_all.words())
word_features = list(all_words.keys())[:3000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
print(featuresets)
train_set, test_set = featuresets[:], featuresets[:50]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(1000))


