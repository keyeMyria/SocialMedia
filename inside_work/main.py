import json
#from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import tfidvectorizer
from sklearn.cluster import KMeans
from nltk import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords





def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(None, string.punctuation)
    tokens = word_tokenize(text)
 
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
 
    return tokens






def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
	f_model = vectorizer.fit_transform(texts)
	km_model = KMeans(n_clusters=clusters)
	km_model.fit(tfidf_model)
	clustering = collections.defaultdict(list)
	for idx, label in enumerate(km_model.labels_):
		clustering[label].append(idx)
	return clustering



def sa(data):
	f=open("result.json","wb+")
	json.dump(data,f)
	f.close()







data= json.load(open("result.json"))

for key in  data.keys():
	for i in data[key].keys():
		d=sent_tokenize(data[key][i])
		for k,sent in enumertae(d):
			d[k]=clustering(word_tokenize(sent))
		data[key][i] = d
sa(data)



