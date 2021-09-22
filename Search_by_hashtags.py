import pandas as pd
import emot
import twint
import nest_asyncio

Hashtags = pd.read_excel('Hashtags.xlsx', sheet_name='sheet1')[0].tolist()

def return_tweet(Hashtag_lst):
    data = []
    for i, emo in enumerate(Hashtag_lst):
        try:
            tweets = []
            c = twint.Config()
            c.Images = True
            # c.Popular_tweets=True
            c.Search = emo
            c.Limit = 20
            c.Store_object = True
            c.Store_object_tweets_list = tweets
            twint.run.Search(c)
            data.extend(tweets)
        except:
            print('The Error arise from index :{}\nRun the code again by changing return_tweet(search[{}:]) '.format(i,
                                                                                                                     i))
            break
        print("in progress...\nindex number -> {}".format(i))
    return data


Tweets = return_tweet(Hashtags)
# creating a dataframe
df = pd.concat(
    [pd.Series(Tweets).apply(lambda x: x.username), pd.Series(Tweets).apply(lambda x: x.name),
     pd.Series(Tweets).apply(lambda x: x.tweet)],
    axis=1)
df.columns = ['username', 'name', 'tweet']
# English only
df = df[pd.Series(Tweets).apply(lambda x: x.lang) == 'en'].reset_index()
df = df.drop('index', axis=1)
df = df.sample(frac=1).reset_index()
df = df.drop('index', axis=1)
# writing to an excel file
df.to_excel('twitter_Hashtags.xlsx', sheet_name='sheet_1', index=False)
