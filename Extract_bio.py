import pandas as pd
import twint
import nest_asyncio

nest_asyncio.apply()


def return_bio(df):
    bio = []
    for i, users in enumerate(df['username']):
        try:
            c = twint.Config()
            c.Username = users
            c.Store_object = True
            twint.run.Lookup(c)
            user = twint.output.users_list[-1]
            bio.append(user.bio)
            print(bio[-1])
        except:
            print("the Error arise from index -> {}".format(i))
            continue
        print("In progress...\nindex number : {}".format(i))
    return bio


df = pd.read_excel('User_job.xlsx', sheet_name='Sheet_1')
df['bio'] = pd.Series(return_bio(df))
df.to_excel('User_FInfo.xlsx', sheet_name='sheet_1', index=False)
