# -*- coding: utf-8 -*-

from __future__ import print_function

import pandas as pd
import os

# DB_dir = 'database'
DB_csv = 'database/data-small.csv'


class Database(object):

  def __init__(self):
    self.data = pd.read_csv(DB_csv)
    

  def __len__(self):
    return len(self.data)

  def get_data(self):
    return self.data


if __name__ == "__main__":
  db = Database()
  data = db.get_data()
  print("DB length:", len(db))
  
