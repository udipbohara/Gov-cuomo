

from flair.models import TextClassifier
from flair.data import Sentence



tagger = TextClassifier.load('sentiment')

sentence = Sentence('Cuomo is doing the best he can!')

tagger.predict(sentence)

print(sentence.labels)