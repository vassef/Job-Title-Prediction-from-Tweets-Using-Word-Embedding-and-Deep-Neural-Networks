# Project Title
Job-Title-Prediction-from-Tweets-Using-Word-Embedding-and-Deep-Neural-Networks

## Description

The more social media take its place in our lives, the
more important their analysis becomes and the more researchers’
attention is drawn to it. Studies contain various topics such as
sentiment analysis, trend prediction, bot detection, etc. Here, for
the first time, we propose a novel method to predict the job title
of social media users. Twitter, a popular social media, is the our
target social media. We introduce a dataset consist of 1314 users’
tweets and bios. The user’s job title is found using Wikipedia
crawling. The challenge of multiple job title per user is handled
using a semantic word embedding and clustering method. Then,
a job prediction method based on a deep neural network and TF-IDF word embedding is introduced. We also take the advantage
of hashtags and emojis in the tweets for job prediction. Results
show that the job title of users in Twitter could be well predicted
with 54% accuracy in nine categories.

## Getting Started

### Dependencies

* twint library(If you get the error: "Cannot connect to host twitter.com", then check out this [link](https://github.com/twintproject/twint/issues/442))
* emojis library
* GloVe pre-trained model

### Installing

 1. Installing twint :
    - Download and Install git in your windows from [here](https://git-scm.com/download/win)
    - pip3 install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
 2. Installing emojis :
    - pip3 install emojis
 3. Download the GloVe zip file from [here](https://nlp.stanford.edu/projects/glove/)

### Executing program
1. Folders
   - There are 4 files inside an "Excel_files folder", which are the list of users with their features updating during each process.
   - Also, there are 5 files located in the "Extrcat_data" folder which are the processing steps to construct our whole dataset.
   - After that, we began preprocessing on our dataset consist of embedding and cleaning steps which are located in the "Preprocessing" folder.
   - Finally, We fed our dataset to the designed models inside the "Models" folder.
2. Step-by-step
   - Firstly we start our work by searching for two terms including emojis and hashtags. We provided the list of hashtags inside the Hashtag.xlsx file, but the emojis were located inside the code. Tweets with less than 50k likes have been removed, which means we were searching for famous groups of users, especially celebrities or influencers on Twitter. The codes for these two methods are located in the "Extract_data" folder naming Search_by_hashtags.py and Search_by_emojis.py .
- After searching for users by these two methods, we extracted user's tweets by searching their usernames. We set two limits on extracting tweets:
  - only English-written tweets would be extracted.
  - We selected the last 10 to 40 tweets for each user depending on the number of tweets available for that user.
You can find the whole process in the Extract_tweets.py inside the "Extract_data" folder.

* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
