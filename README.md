# Project Title

Job Title Prediction from Tweets Using Word Embedding and Deep Neural Networks

## Description
Here is the official implementation of our [paper](https://drive.google.com/file/d/1m4jL2300ChtihBlAp3TMh1N_U097mFPv/view?usp=sharing) submitted at the ICEE conference.
## Getting Started

### Dependencies

* Twint library
* Emojis library
* GloVe pre-trained model

### Installing

 1. Installing twint :
    - Download and Install git in your windows from [here](https://git-scm.com/download/win)
    - pip3 install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
 2. Installing emojis :
    - pip3 install emojis
 3. Download the GloVe zip file from [here](https://nlp.stanford.edu/projects/glove/)

### Executing program
* Folders
  - There are four files inside an "Excel_files" folder, the list of users with their features updating during each process. You can find the **user's complete information** in User.FInfo.xlsx and the **final preprocessed dataset** in FDF.xlsx. 
  There are five files located in the "Extrcat_data" folder, which are the extracting steps to construct our whole dataset.
  - After that, we began preprocessing on our dataset consisting of embedding and cleaning steps located in the "Preprocessing" folder.
  - Finally, We fed our dataset to the designed models inside the "Models" folder.
* Step-by-step
  - Firstly, we start our work by searching for two terms, including emojis and hashtags. We provided the list of hashtags inside the Hashtag.xlsx file, but the emojis were located inside the code. Tweets with less than 50k likes have been removed, which means we were searching for famous groups of users, especially celebrities or influencers on Twitter. The codes for these two methods are located in the "Extract_data" folder named Search_by_hashtags.py and Search_by_emojis.py.
  - After searching for users by these two methods, we extracted users' tweets by searching their usernames. We set two limits on removing tweets:
    - only English-written tweets would be extracted.
    - We selected the last 10 to 40 tweets for each user depending on the number of tweets available for that user.
     Inside the Extract_tweets.py, you can find the whole process in the Extract_tweets.py inside the "Extract_data" folder.
  - Next, we found each user's bio by searching the user profile. The code is attached to the  "Extract_data" folder named Extract_bio.py.
  - The final step in the extraction is to seek the user's jobs. We employed Wikipedia as a reference web page to extract users' information, especially employment. We developed an algorithm to separate the job phrase from the user's Wikipedia summary. After that, we designed a cleaning algorithm to return all the jobs user is involved in, separated by a comma. To clarify this, suppose that the user's Wikipedia summary is: "John Joseph Nicholson is an American retired actor and filmmaker whose career spanned more than 50 years." The output of the process would be "actor, filmmaker. " You can find the code in the "Extract_data" folder named Extract_jobs.py.\
Here is the 20 most frequent unigram appearing inside the job titles:![newplot](https://user-images.githubusercontent.com/88703731/134731330-c846dd28-f2ff-406c-91bb-38afc964e38f.png)
  - After preparing our dataset, it's time to apply preprocessing steps.
We first employed the GolVe pre-trained model for the embedding purpose. To generalize our model, we extracted the first two jobs of many that the user can have. Then we converted each position to a single word since we would measure the similarity between two terms.  As an example, we converted the string "news anchor "  to the combination of "news" and "anchor" and then replaced the most similar word to this combination. After that, we use the Kmeans clustering to categorize our job titles in which The jobs with the same interest lie in the same group.
by using the Elbow method, we find **9** unique labels as shown below:\
![fig3](https://user-images.githubusercontent.com/88703731/134761715-27a06f5b-d296-475d-b90a-4f5fa69bf63f.png)\
Also, you can see the patterns appearing in each label:\
![pattern](https://user-images.githubusercontent.com/88703731/134761822-3bd233cd-fb86-44b5-a3b8-c018547b12b9.png)\
The code is located in the "Preprocessing" folder named User_jobs_embedding.ipynb. 
  - Also, we proposed three methods dealing with hashtags and compared the performance for each of them.
You can access the code in the "Preprocessing" folder named User_finall_processing.ipynb. 
### Results
 Now, it's time to evaluate our dataset by investigating the three designed models in the "Models" folder. Also, the model performance caused by each method and the  classification report of the DDN model is attached below :\
![Model_summary](https://user-images.githubusercontent.com/88703731/134739319-aa54ea88-d6c6-4cb1-bda7-d3e279816d0c.png)

## Help
If you have connection issues like: "Cannot connect to host twitter.com," check out this [link](https://github.com/twintproject/twint/issues/442).
## Authors

* Shayan Vassef 
  - Gmail : shayanvassef2000@gmail.com
  - Linkedin : [shayan vassef](https://www.linkedin.com/in/shayan-vassef-319023203)
* Ramin Toosi
  - Email : r.toosi@ut.ac.ir
  - Linkedin : [Ramin Toosi](https://www.linkedin.com/in/ramin-toosi-54308296/)

## Acknowledgments
I would like to thank [Adak Vira Iranian Rahjo (Avir) company](https://www.avir.co.com/IR/index.html) for their contribution during this project.


