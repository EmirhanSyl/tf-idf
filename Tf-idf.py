import math
import pandas as pd

col_list = ["Pageurl", "Title"]
dataframe = pd.read_csv("marketing_sample_for_ebay_com-ebay_com_product__20210101_20210331__30k_data.csv", usecols=col_list)
word = input("Serch...: ")

def tfidfCalculate(wd, df):
    tfidf_dict = {}

    D_sum = 0
    D = 0

    for index in df.index:
        title = str(df.loc[index, 'Title'])
        pageURL = str(df.loc[index, 'Pageurl'])

        word_list = title.split()

        t = word_list.count(wd)
        d = len(word_list)

        tfidf_dict[pageURL] = t / d

        D_sum += 1
        if t > 0:
            D += 1

    else:
        idf_result = math.log2(D / D_sum)

        for index in df.index:
            pageURL = str(df.loc[index, 'Pageurl'])
            tfidf_dict[pageURL] = tfidf_dict[pageURL] * idf_result

    for w in sorted(tfidf_dict, key=tfidf_dict.get, reverse=True):
        print(w, tfidf_dict[w])


if not word == "":
    tfidfCalculate(word, dataframe)
else:
    print("Please enter a word!")