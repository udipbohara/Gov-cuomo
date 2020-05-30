import json
import pandas as pd
import warnings
import matplotlib.pyplot as plt 
import re 
import unicodedata
import glob
from flair.models import TextClassifier
from flair.data import Sentence

warnings.filterwarnings('ignore')


#get all the files from folders #do same for each month
files = glob.glob('../data/march/*.json')
dfs = [pd.read_json(f) for f in files]
df_march = pd.concat(dfs,ignore_index=True)


df_march.user_id = df_march.user_id.astype(str)
df_march.tweet_id = df_march.tweet_id.astype(str)

#drop duplicates
df_march.drop_duplicates('tweet_id', inplace=True)
#Filtering tweets of Gov Cuomo by his user ID.
march_cuomo = df_march.loc[df_march.user_id ==  '232268199']

#remove all tweets from Gov Cuomo and drop duplicates for tweets.
march_all = df_march.loc[df_march.user_id !='232268199']

contraction_map = {
"ain't": "is not","aren't": "are not","can't": "cannot","can't've": "cannot have","'cause": "because",
"could've": "could have","couldn't": "could not","couldn't've": "could not have","didn't": "did not",
"doesn't": "does not","don't": "do not","hadn't": "had not","hadn't've": "had not have","hasn't": "has not",
"haven't": "have not","he'd": "he would","he'd've": "he would have","he'll": "he will","he'll've": "he he will have","he's": "he is",
"how'd": "how did","how'd'y": "how do you","how'll": "how will","how's": "how is","I'd": "I would","I'd've": "I would have",
"I'll": "I will","I'll've": "I will have","I'm": "I am","I've": "I have","i'd": "i would","i'd've": "i would have","i'll": "i will",
"i'll've": "i will have","i'm": "i am","i've": "i have","isn't": "is not","it'd": "it would","it'd've": "it would have","it'll": "it will",
"it'll've": "it will have","it's": "it is","let's": "let us","ma'am": "madam","mayn't": "may not",
"might've": "might have","mightn't": "might not","mightn't've": "might not have","must've": "must have","mustn't": "must not",
"mustn't've": "must not have","needn't": "need not","needn't've": "need not have","o'clock": "of the clock",
"oughtn't": "ought not","oughtn't've": "ought not have","shan't": "shall not","sha'n't": "shall not","shan't've": "shall not have",
"she'd": "she would","she'd've": "she would have","she'll": "she will","she'll've": "she will have",
"she's": "she is","should've": "should have","shouldn't": "should not","shouldn't've": "should not have","so've": "so have",
"so's": "so as","that'd": "that would","that'd've": "that would have","that's": "that is",
"there'd": "there would","there'd've": "there would have","there's": "there is","they'd": "they would","they'd've": "they would have","they'll": "they will","they'll've": "they will have",
"they're": "they are","they've": "they have","to've": "to have","wasn't": "was not",
"we'd": "we would","we'd've": "we would have","we'll": "we will","we'll've": "we will have","we're": "we are","we've": "we have",
"weren't": "were not","what'll": "what will","what'll've": "what will have","what're": "what are",
"what's": "what is","what've": "what have","when's": "when is","when've": "when have","where'd": "where did","where's": "where is",
"where've": "where have","who'll": "who will","who'll've": "who will have","who's": "who is","who've": "who have",
"why's": "why is","why've": "why have","will've": "will have","won't": "will not","won't've": "will not have","would've": "would have",
"wouldn't": "would not","wouldn't've": "would not have","y'all": "you all","y'all'd": "you all would","y'all'd've": "you all would have",
"y'all're": "you all are","y'all've": "you all have","you'd": "you would","you'd've": "you would have","you'll": "you will",
"you'll've": "you will have","you're": "you are","you've": "you have"
}

def remove_special_chars(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text

def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def remove_url_chars(text):
    text = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", text)
    return text 

def expand_contractions(text, contraction_mapping=contraction_map):

    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())                       
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

#create dictionary of the functions to be applied
funcdict = {"1": expand_contractions,"2": remove_special_chars, "3": remove_accented_chars,}

march_all['processed_text'] = march_all.text
march_cuomo['processed_text'] = march_cuomo.text

for k,v in funcdict.items():
    march_all.processed_text = march_all.processed_text.apply(lambda x: v(x))
    march_cuomo.processed_text = march_cuomo.processed_text.apply(lambda x: v(x))

#remove new line chars and lowercase the letters.
march_all.processed_text = march_all.processed_text.replace('\n','', regex=True).str.lower()

df = march_all.copy() 

#sentiment training
tagger = TextClassifier.load('sentiment')


value = []
score = []
sentiments = []
for texts in df.processed_text:
    sentence = Sentence(texts)
    tagger.predict(sentence)
    value.append(sentence.labels[0].value)
    score.append(sentence.labels[0].score)
    sentiments.append(sentence.labels)

df['sentiment_value'] = value
df['score'] = score 
df['sentiments'] = sentiments

df.to_csv('../data/march_trained.csv')
march_cuomo.to_csv('../data/march_cuomo.csv')

"""
#converting all the negative sentiments to '-'ve 
df.loc[df.sentiment_value == 'NEGATIVE', 'score'] = -1 * df.score 

#for above 0.8 threshold for negativity
df.loc[df.score <= -0.8, 'polarity'] = -1 

#for positive polarity threshold
df.loc[df.score >= 0.8, 'polarity'] = 1 

#rest are neutral, polarity = 0 
df['polarity'] = df['polarity'].fillna(0)
"""