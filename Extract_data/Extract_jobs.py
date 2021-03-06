import pandas as pd
import wikipedia
import re
from nltk import word_tokenize
import twint
import nest_asyncio

nest_asyncio.apply()

nest_asyncio.apply()

NATIONALITIES_list = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean',
                      'Argentine', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini',
                      'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean',
                      'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'Brazil', 'British', 'Bruneian',
                      'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian',
                      'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Columbia',
                      'Comoran', 'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish',
                      'dangdut', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese',
                      'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian',
                      'English', 'England', 'Fijian', 'Filipino', 'Filipina', 'Finnish', 'French', 'Gabonese',
                      'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan',
                      'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hong Kong',
                      'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish',
                      'Israeli', 'Islamic', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Jewish',
                      'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latin',
                      'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Liswati',
                      'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian',
                      'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan',
                      'Monacan', 'Mon??gasque', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian',
                      'Nauruan', 'Nepalese', 'Netherlander', 'New Zealand', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan',
                      'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani',
                      'Palauan', 'Panamanian', 'Papua New Guinean', 'pagode', 'Paraguayan', 'Peruvian', 'Palestinian',
                      'Polish', 'Portuguese', 'Puerto Rican', 'reggaeton', 'Qatari', 'Romanian', 'Russian', 'Rwandan',
                      'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish',
                      'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian',
                      'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan',
                      'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian',
                      'Thai', 'Togolese', 'Tongan', 'Trinidadian', 'Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan',
                      'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh',
                      'Yemenite', 'Zambian', 'Zimbabwean']
Useless = ['professional', 'former ', 'retired', 'current', 'the ', 'international', 'Member', 'billionaire',
           'University', 'Charismatic', 'Christian', 'country', 'music ', 'Grammy', 'award', 'winning', 'winner',
           'Olympic', 'gold', 'medal', 'playback', 'entertainment', 'best', 'mother', 'nominated', 'electronic',
           'famous', 'reality', 'retail', 'stage', 'event', 'popular', 'South', 'living', 'primarily', 'conservative',
           'competitive ', 'track', 'field', 'freelance', 'female', 'male', 'public ', 'most', 'national ', 'evening',
           'first', 'lady', 'National Party', 'online', 'independent', 'Emmy', 'Award', 'multitalented', 'R & B',
           'wildlife', 'better']
key_lst = ['from ', 'who', 'whose ', 'known ', 'one of', 'of ', 'for ', 'currently ', 'consisting', 'based', 'notable',
           'multiple time', 'that', 'heir', 'mostly', 'noted ', 'was ', 'managed by', ' in ', 'widely', 'about ',
           'since ', 'formed', 'serving', 'with ', ' during', 'founded', 'notably', 'at ', 'represented',
           'specializing', 'focusing', 'as well as', 'possibly', 'signed to', 'referred to']


def clean_txt(text, key_lst, NATIONALITIES_list, Useless):
    text = re.sub(r"\([^()]*\)", "", text)
    text = re.sub('U.S.', "", text)
    if ' is a ' in text and ' is an ' in text:
        if len(re.search('(.*?) is an ', text).group(1)) < len(re.search('(.*?) is a ', text).group(1)):
            if len(text.split(' is an ')[1].split('.')[0]) < len(text.split(' is an ')[1].split('. ')[0]):
                job = text.split(' is an ')[1].split('.')[0]
            else:
                job = text.split(' is an ')[1].split('. ')[0]
        else:
            if len(text.split(' is a ')[1].split('.')[0]) < len(text.split(' is a ')[1].split('. ')[0]):
                job = text.split(' is a ')[1].split('.')[0]
            else:
                job = text.split(' is a ')[1].split('. ')[0]

    elif ' is an ' in text:
        if len(text.split(' is an ')[1].split('.')[0]) < len(text.split(' is an ')[1].split('. ')[0]):
            job = text.split(' is an ')[1].split('.')[0]
        else:
            job = text.split(' is an ')[1].split('. ')[0]

    elif ' is a ' in text:
        if len(text.split(' is a ')[1].split('.')[0]) < len(text.split(' is a ')[1].split('. ')[0]):
            job = text.split(' is a ')[1].split('.')[0]
        else:
            job = text.split(' is a ')[1].split('. ')[0]
    else:
        pass

    substring = job
    substring = re.sub('  ', ' ', substring)
    substring = re.sub(' a ', ' ', substring)
    substring = re.sub(', ', ',', substring)
    substring = substring.strip()

    pattern = []
    choice = []
    for item in key_lst:
        pattern.append('(.*?)' + item)

    for item in key_lst:
        if item in substring:
            choice.append(re.search(pattern[key_lst.index(item)], substring).group(1))
        else:
            continue

    for item in choice:
        if item == [item for item in choice if len(item) == min([len(item) for item in choice])][0]:
            substring = item
        else:
            continue

    for item in NATIONALITIES_list:
        if item + '-born' in substring:
            substring = re.sub(item + '-born', '', substring)
        elif item in substring:
            substring = re.sub(item, '', substring)

    for item in Useless:
        if item in substring:
            substring = re.sub(item, '', substring)

    if ',and ' and ' and ' in substring:
        clean_text = substring.split(' and ')
        clean_text = ','.join(clean_text).split(',and ')

    elif ',and ' in substring:
        clean_text = substring.split(',and ')

    elif ' and ' in substring:
        clean_text = substring.split(' and ')

    else:
        clean_text = substring.split(',')

    finall = word_tokenize(','.join(clean_text))

    if finall[-1] == ',' and finall[0] == '-':
        finall.pop(-1)
        finall.pop(0)

    elif finall[0] == '-':
        finall.pop(0)

    elif finall[-1] == ',':
        finall.pop(-1)

    elif '-' in finall[1:-1]:
        finall.pop(finall.index('-'))

    return ' '.join(finall)


Celeb_table = pd.read_excel('User_tweet_hashtag.xlsx', sheet_name='sheet_1')


def Seek_job(Data_Frame, key_lst, NATIONALITIES_list, Useless):
    Jobs = []
    for item in Data_Frame['name']:
        try:
            text = wikipedia.summary(item, sentences=2, auto_suggest=False)
            Jobs.append(clean_txt(text, key_lst, NATIONALITIES_list, Useless))
        except:
            try:
                text = wikipedia.summary(item, sentences=2, auto_suggest=True)
                Jobs.append(clean_txt(text, key_lst, NATIONALITIES_list, Useless))
            except:
                try:
                    text = wikipedia.summary([item for item in Data_Frame[Data_Frame['name'] == item]['username']][0],
                                             sentences=2, auto_suggest=True)
                    Jobs.append(clean_txt(text, key_lst, NATIONALITIES_list, Useless))
                except:
                    Jobs.append("Can't find the real name !")

        finally:
            print(Jobs[-1])

    Data_Frame['Job'] = pd.Series(Jobs)
    return Data_Frame


finall_table = Seek_job(Celeb_table, key_lst, NATIONALITIES_list, Useless)
finall_table.to_excel('User_job.xlsx', sheet_name='sheet_1', index=False)
