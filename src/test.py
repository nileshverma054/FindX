# import torch
# print(torch.__version__)

import os
import tqdm
import pandas as pd
import shutil
import feather

# cols = ['id','gender','subCategory','productDisplayName']
# df = pd.read_csv('database/test_data.csv', usecols=cols)
# new_df = df[:1000].copy()
#print(new_df)
# df.to_csv('database/test_data.csv', index=False)


source = r"C:\Users\dhass\OneDrive\Documents\VST\Dataset\fashion-product-images-small\images"
dest = r"C:\Users\dhass\OneDrive\Documents\VST\CBIR\CBIR-CODE - Copy\database\images"


'''
df = pd.read_csv('database/test_data.csv')
new_df = df['id'][:2000].copy()
#print(new_df)
files_to_find = []
for i in new_df:
    files_to_find.append(str(i)+'.jpg')

print(files_to_find)

for root,dirs,files in os.walk(source):
    for filename in files:
        if filename in files_to_find:
            shutil.copy(os.path.join(root,filename),dest)
        
print("done")
'''
# df = pd.read_csv('database/test_data.csv')

# df.to_feather('database/data.ftr')

# data = pd.read_feather('database/data.ftr')
# ret = data.query('gender == "Men"',inplace=False)
# print(ret['id'][:10])
#print(len(ret),"\n",ret)

#============

# cols = ['gender','subCategory','productDisplayName']
# db_csv = 'database/styles.csv'
# df1 = pd.read_csv(db_csv, usecols=cols)
# df2 = pd.read_csv('database/images.csv', usecols=["id"])
# df4 = pd.read_csv('database/images.csv', usecols=["link"])
# df3 = pd.concat([df2,df1,df4], axis=1)
# df3.info()

# df1.info()
# df2.info()
# # print(df3[:5])
# new_data = []
# for i,row in df3.iterrows():
#     new_name = 'database/images/'+str(df3.loc[i,"id"])
#     # df.loc[i,"id"] = new_name
#     new_data.append(new_name)
# df3["path"] =new_data
# # print(df3[:5])
# df3.to_csv('database/data.csv', index=False)
# print("done")

#================

# df = pd.read_csv('database/data-small.csv')
# df.info()

# site = []
# link = []
# logo = [] 
# for i in range(400):
#     site.append('flipkart')
#     site.append('amazon')
#     site.append('myntra')
#     link.append('https://www.flipkart.com/')
#     link.append('https://www.amazon.in/')
#     link.append('https://www.myntra.com/')
#     logo.append('images/logos/flipkart.png')
#     logo.append('images/logos/amazon.png')
#     logo.append('images/logos/myntra.png')

# site = site[:1000].copy()
# link = link[:1000].copy()
# logo = logo[:1000].copy()

# # print('site ', len(site), site[:10])
# # print('link ',len(link), link[:10])
# # print('logo ',len(logo), logo[:10])

# df['site'] = site
# df['product_link'] = link
# df['logo'] = logo
# df.info()
# df.to_csv("database/data-small.csv", index=False)

# ======================


df = pd.read_csv('database/data-small.csv')
df.info()

price = [] 
for i in range(300):
    price.append(449)
    price.append(399)
    price.append(589)
    price.append(699)
    

price = price[:1000].copy()

df['price'] = price
df.info()
df.to_csv("database/data-small.csv", index=False)
