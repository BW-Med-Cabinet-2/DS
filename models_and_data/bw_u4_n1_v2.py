# -*- coding: utf-8 -*-
"""BW_U4_N1_V2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KEU9voTuKDxFzOPfhgVfIUuQtMQ5NZDp
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors




df2 = pd.read_csv('''
 https://raw.githubusercontent.com/calebmckay1/Unit-1-Build/master/toking.csv
                  ''')

med = df2[df2['ailment'].isnull()==False]
med = med.reset_index()
med = med[['name','type','flavors','positive_effects','ailment','search']]



def strain_finder(request, outputs=10, category='ailment'):
  """Accepts input string and integer for number of outputs
  requires a string input of either name, type, flavors, positive_effects, or 
  ailment. 
  Returns a list of tuples of strings"""
  input = [request]
  tfidf = TfidfVectorizer(stop_words='english')

  ttm = tfidf.fit_transform(med[category])

  ttm = pd.DataFrame(ttm.todense(), columns=tfidf.get_feature_names())

  nn = NearestNeighbors(n_neighbors=outputs, algorithm='kd_tree')
  nn.fit(ttm)
  encoded = tfidf.transform(input)
  result =[]
  for item in nn.kneighbors(encoded.todense())[1][0]:
    info = (('name', med['name'][item]), ('type', med['type'][item]), 
            ('positive_effects',(med['effects'][item])),
            ('ailments', (med['ailment'][item])),
            ('flavors',med['flavors'][item])
            )
    result.append(info)
  return result



def search_name(name):
  """Name is case sensitive, most are title case.
  example **Cure for Scurvy** 
  and not **cure for scurvy**"""
  result = med[med['name']==name]
  if len(result)==0:
    return "Name not found"
  return result

search_name('A-1')

def search_type(strain):
  """ Types available are Indica, Stavia, and Hybrid"""
  strain = strain.title()
  output = med[med['type']==strain]
  if len(output)==0:
    return "Type not found"
  return output

search_type('Indica')