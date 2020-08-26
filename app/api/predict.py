import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

log = logging.getLogger(__name__)
router = APIRouter()

df = pd.read_csv('toking.csv')


def search_func(user_input):

    user_input = [user_input]
    nlp=English()
    tokenizer = Tokenizer(nlp.vocab)
    tf = TfidfVectorizer(stop_words='english')
    dtm = tf.fit_transform(df['search'])
    dtm = pd.DataFrame(dtm.todense(), columns=tf.get_feature_names())

    nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
    nn.fit(dtm)
    dtf = tf.transform(user_input)
    _, output = nn.kneighbors(dtf.todense())


    recommendations = []
    for n in output:
        for row in n:
            recommendations.append(row)

    result=[]
    for i in recommendations:
        data=(df.loc[i,:])
        result.append(data)
    return {'strain_recommendations': result}


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    symptom1: str = Field(..., example='insomnia')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(item: Item):
    """
    Make a baseline strain recommendation.

    ### Request Body
    - `symptom1`: string
    - `symptom2`: string
    - `symptom3`: string

    ### Response
    - `strain_recommendation`: list of strain names
    """
    X_new = item.to_df()
    log.info(X_new)
    return {'recommendations': search_func(item.symptom1)}
