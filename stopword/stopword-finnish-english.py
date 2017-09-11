def features(word):
	return {'last_letter': word[-1]}

from nltk.corpus import stopwords
import random, nltk
words = ([(word, 'english') for word in stopwords.words('english')]+[(word, 'finnish') for word in stopwords.words('finnish')])
random.shuffle(words)
featuresets = [(features(n), g) for (n,g) in words]
train_set, test_set = featuresets[20:], featuresets[:20]
classifier =nltk.NaiveBayesClassifier.train(train_set)

def main():
    print(classifier.show_most_informative_features(3))

main()