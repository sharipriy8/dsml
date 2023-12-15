import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

text = "This is a sample sentence for POS tagging."


tokenized_text = word_tokenize(text)
tokenized_text 


pos_tags = pos_tag(tokenized_text)


print("POS Tags:", pos_tags)

