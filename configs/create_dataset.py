import pandas as pd
import os
import shutil
import tqdm


def file_count(path):
    print(len(os.listdir(path)))

def limmit_data(path, limit):
    df1 = pd.read_csv(path)[:limit]
    df1.to_csv(path, index=False)

def def_cols(path, cols):
    df1 = pd.read_csv(path, usecols=cols)
    df1.to_csv(path, index=False)

def small_db(source, dest, limit):
    """
    This creates small dataset of 1000 records in csv file
    :return: none
    """
    #cols to use
    cols = ['id','gender','subCategory','productDisplayName']
    df = pd.read_csv(source, usecols=cols)
    new_df = df[:limit].copy()
    new_df.to_csv(dest, index=False)
    print("success")

def copy_img(source, dest, csv_file):
    """
    make small copy of original dataset images
    :return: none
    """
    df = pd.read_csv(csv_file)
    new_df = df['id'].copy()
    files_to_find = []
    for i in new_df:
        files_to_find.append(str(i) + '.jpg')

    print("Total files : ", len(files_to_find))

    for root, dirs, files in os.walk(source):
        print(root)
        for filename in files:
            print(filename)
            if filename in files_to_find:
                shutil.copy(os.path.join(root, filename), dest)
    print("success")

def add_cols(main_csv):
    df1 = pd.read_csv(main_csv)[:1000]
    df2 = pd.read_csv("database/test_data.csv")
    df3 = pd.concat([df1,df2], axis=1)
    # df3.info()
    path=[]
    for i,row in df3.iterrows():
        temp = "database/images/"+str(df3.loc[i,"filename"][1])
        path.append(temp)
    df3["path"] = path
    df3.to_csv("database/test_data.csv", index=False)
    print("success")

def reindex(csv_file, cols):
    df1 = pd.read_csv(csv_file)
    df1.reindex(columns=cols)
    df1.to_csv(csv_file, index=False)
    print("success")

def add_sites(csv_file):
    df = pd.read_csv(csv_file)
    site = []
    link = []
    logo = []
    price = []
    for i in range(400):
        site.append('flipkart')
        site.append('amazon')
        site.append('myntra')
        link.append('https://www.flipkart.com/')
        link.append('https://www.amazon.in/')
        link.append('https://www.myntra.com/')
        logo.append('images/logos/flipkart.png')
        logo.append('images/logos/amazon.png')
        logo.append('images/logos/myntra.png')
        price.append(449)
        price.append(399)
        price.append(589)
        price.append(699)

    price = price[:1000].copy()
    site = site[:1000].copy()
    link = link[:1000].copy()
    logo = logo[:1000].copy()

    # # print('site ', len(site), site[:10])
    # # print('link ',len(link), link[:10])
    # # print('logo ',len(logo), logo[:10])

    df['site'] = site
    df['product_link'] = link
    df['logo'] = logo
    df['price'] = price
    # df.info()
    df.to_csv(csv_file, index=False)
    print(df[:10])
    print("success")


if __name__ == '__main__':
    pass
    # file_count('/Users/mrnk/Documents/Workspace/Experiments/FindX/database/images')
    # small_db(source='database/styles.csv',dest='database/test_data.csv',limit=1000)
    # copy_img(source='/Users/mrnk/Documents/Workspace/Experiments/FindX/database/images-original', dest='/Users/mrnk/Documents/Workspace/Experiments/FindX/database/images', csv_file='database/test_data.csv')
    #
    # reindex("database/test_data.csv", columns)
    # add_cols("database/images.csv")
    # limmit_data("database/test_data.csv",1000)
    # cols = ["id", "filename", 'gender', "subCategory", "productDisplayName", "link"]
    # def_cols("database/test_data.csv", cols)
    # add_sites("database/test_data.csv")
