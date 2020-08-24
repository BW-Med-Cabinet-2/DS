# -*- coding: utf-8 -*-
"""BW_U4_N1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KEU9voTuKDxFzOPfhgVfIUuQtMQ5NZDp
"""

import pandas as pd
import numpy as np

#df = pd.read_csv('/content/cannabis.csv')

#df.head()

df2 = pd.read_csv('https://raw.githubusercontent.com/kushyapp/cannabis-dataset/master/Dataset/Strains/strains-kushy_api.2017-11-14.csv')
df2.head()

#print(df.shape,df2.shape)

df2['ailment'].isnull().value_counts()

df2['ailment'].unique()

df2['thc'] = df2['thc'].replace(0, np.nan)

df2['effects'].isnull()

med = df2[df2['ailment'].isnull()==False]
med = med.reset_index().drop(['index','id'],axis=1)
med.head()

from sklearn.feature_extraction.text import TfidfVectorizer
#from nltk.corpus import stopwords
from sklearn.neighbors import NearestNeighbors

def strain_finder(request,outputs=10): 
  input = [request]
  tfidf = TfidfVectorizer(stop_words='english')

  ttm = tfidf.fit_transform(med['ailment'])

  ttm = pd.DataFrame(ttm.todense(), columns=tfidf.get_feature_names())

  nn = NearestNeighbors(n_neighbors=outputs, algorithm='kd_tree')
  nn.fit(ttm)
  encoded = tfidf.transform(input)
  for item in nn.kneighbors(encoded.todense())[1][0]:
    print(med['name'][item]," ",med['ailment'][item], '\n')

strain_finder('I need something for pain and stress', 50)