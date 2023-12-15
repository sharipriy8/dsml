import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

text = "This is a sample sentence for generating n-grams."

tokenized_text = word_tokenize(text)

print(tokenized_text)


from nltk import ngrams
def generate_ngrams(tokens, n):
 return list(ngrams(tokens, n))

n_value = 3 


ngrams_list = generate_ngrams(tokenized_text, n_value)


print(f"{n_value}-grams:", ngrams_list)



