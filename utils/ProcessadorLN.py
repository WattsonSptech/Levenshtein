from transformers import pipeline
from transformers.pipelines.base import Pipeline
from nltk.corpus import stopwords
from spacy.language import Language
from typing import Any
import spacy
import os
import nltk
import re

class ProcessadorLN:

    nlp: Language
    stopwords: set
    modelo: Pipeline

    def __init__(self) -> None:
        nltk.download('stopwords')

        try:
            nlp = spacy.load("pt_core_news_sm")
        except OSError:
            os.system("python -m spacy download pt_core_news_sm")
            nlp = spacy.load("pt_core_news_sm")
        
        self.nlp = nlp
        self.stopwords = set(stopwords.words('portuguese'))
        self.modelo = pipeline(
            task="sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment"
        )

    def tokenizar(self, texto: str):
        texto = re.sub(r"http\S+|www\S+", "", texto.lower().strip())
        texto = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto)

        doc = self.nlp(texto)
        tokens = []
        for token in doc:
            if token.text not in self.stopwords and len(token.text) > 2:
                tokens.append(token.lemma_)
        return tokens
    
    def avaliar_sentenca(self, texto_tokenizado: list[str]) -> list | Any:
        avals: list = self.modelo(texto_tokenizado)
        aval_mais_precisa = avals[0]["label"]
        return re.search(r"\d+", aval_mais_precisa).group()
