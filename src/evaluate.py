# -*- coding: utf-8 -*-

from __future__ import print_function

from scipy import spatial
import numpy as np
from DB import Database
import pandas as pd

def distance(v1, v2, d_type='d1'):
  assert v1.shape == v2.shape, "shape of two vectors need to be same!"

  if d_type == 'd1':
    return np.sum(np.absolute(v1 - v2))
  elif d_type == 'd2':
    return np.sum((v1 - v2) ** 2)
  elif d_type == 'd2-norm':
    return 2 - 2 * np.dot(v1, v2)
  elif d_type == 'd3':
    pass
  elif d_type == 'd4':
    pass
  elif d_type == 'd5':
    pass
  elif d_type == 'd6':
    pass
  elif d_type == 'd7':
    return 2 - 2 * np.dot(v1, v2)
  elif d_type == 'd8':
    return 2 - 2 * np.dot(v1, v2)
  elif d_type == 'cosine':
    return spatial.distance.cosine(v1, v2)
  elif d_type == 'square':
    return np.sum((v1 - v2) ** 2)

def infer(query, depth=None, d_type='square'):
  data = pd.read_pickle('database/data-small.pkl')
  # print(data[:3])
  results = []
  for i, row in data.iterrows():
    s_hist = data.loc[i,'hist']
    results.append({
                    'dis': distance(query, s_hist, d_type=d_type),
                    'img': data.loc[i,'path'],
                    'link': data.loc[i,'link'],
                    'site': data.loc[i,'site'],
                    'product_link': data.loc[i,'product_link'],
                    'logo': data.loc[i,'logo'],
                    'price': data.loc[i,'price']
                  })
  results = sorted(results, key=lambda x: x['dis'])
  if depth and depth <= len(results):
    results = results[:depth]
  return results

