import spacy
import os
from nltk.corpus import stopwords

class ProcessadorLN:

    nlp = None

    def __init__(self) -> None:
        os.system("python -m spacy download pt_core_news_sm")
        self.nlp = spacy.load("pt_core_news_sm")

    def limpar_conectivos(self, texto: str):
        stopwords_pt = set(stopwords.words('portuguese'))

        doc = self.nlp(texto)
        tokens = []
        for token in doc:
            if token.text not in stopwords_pt and len(token.text) > 2:
                tokens.append(token.lemma_)