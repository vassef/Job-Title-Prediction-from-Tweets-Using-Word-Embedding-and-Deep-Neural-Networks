import pandas as pd
import wikipedia
import re
from nltk import word_tokenize
import twint
import nest_asyncio

nest_asyncio.apply()

def return_tweet(df):
    data = [0] * len(df)
    hashtags = [0] * len(df)

    for i, user in enumerate(df['username']):
        count = 0
        while count < 4:
            try:
                test = []
                mytw = []
                select = []
                tweets = []
                c = twint.Config()
                c.Username = user
                # c.Limit = 20
                c.Store_object = True
                c.Store_object_tweets_list = tweets
                twint.run.Search(c)
                for item in tweets:
                    if item.lang != 'en':
                        pass
                    else:
                        select.append(item)
                mytw = [item.tweet for item in select]
                test.append(mytw)
                myhashtag = [item.hashtags[0] for item in select if item.hashtags != []]
                myhashtag = ','.join([item for item in myhashtag])
                if len(mytw) > 40:
                    mytw = mytw[0:40]
                    count = 4
                elif len(mytw) < 30:
                    count = count + 1

            except:
                print(
                    'The Error arise from index :{}\nRun the code again by changing return_tweet(search[{}:]) '.format(
                        i, i))
                break

            if count == 3:
                m = max([len(item) for item in test])
                index = [i for i, j in enumerate(test) if len(j) == m][0]
                mytw = test[index]

        data[i] = mytw
        hashtags[i] = myhashtag

        print("in progress...\nindex number -> {}".format(i))

    return data, hashtags


df1 = pd.read_excel('twitter_Emojis.xlsx', sheet_name='sheet_1')
df2 = pd.read_excel('twitter_Hashtags.xlsx', sheet_name='sheet_1')
df = pd.concat([df1, df2])
[data, hashtags] = return_tweet(df)
df['tweet'] = pd.Series(data)
df['hashtags'] = pd.Series(hashtags)
df.to_excel('User_tweet_hashtag.xlsx', sheet_name='sheet_1', index=False)
