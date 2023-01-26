import pyspark
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator


# # load data
# data = pd.read_csv('ratings.csv') 
# games = pd.read_csv('games.csv')

# matrix = data
# matrix

spark = pyspark.sql.SparkSession.builder.appName('Games').getOrCreate()
# spark

# create spark dataframe with header and infer schema
df = spark.read.csv('ratings.csv', header=True, inferSchema=True)

# cast all the columns to int
df = df.select(df.user_id.cast('int'), df.game_id.cast('int'), df.rating.cast('int'))

# build test and train data
(train, test) = df.randomSplit([0.8, 0.2], seed = 40)



# build the recommendation model using ALS on the training data
als = ALS(maxIter=5, regParam=0.01, userCol='user_id', itemCol='game_id', ratingCol='rating')

# fit the model to the training data
model = als.fit(train)

# evaluate the model by computing the RMSE on the test data
predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName='rmse', labelCol='rating', predictionCol='prediction')

# get the RMSE
rmse = evaluator.evaluate(predictions)
print('Root-mean-square error = ' + str(rmse))

# get input user id
user_id = int(input('Enter user id: '))

# make a single prediction
single_user = test.filter(test['user_id']==user_id).select(['user_id', 'game_id'])
print('single_user')
single_user.show()

# recommend top 5 games for the user
recommendations = model.transform(single_user)
print('recommendations')
recommendations.orderBy('prediction', ascending=False).show(n=5)


# list of game_id recommended to user 
game_id = recommendations.orderBy('prediction', ascending=False).select('game_id').collect()
recomendation_score = recommendations.orderBy('prediction', ascending=False).select('prediction').collect()


games = pd.read_csv('games.csv')

# print name game with game_id
for i in range(len(game_id)):
    game_data = games.loc[games['game_id'] == game_id[i][0]]
    print(i+1 , ':', 'game:' ,game_data['name'].values[0], '  score:', recomendation_score[i][0])















































# import numpy as np
# import pandas as pd
# import pyspark
# from pyspark.sql import SparkSession
# from pyspark.ml.recommendation import ALS
# from pyspark.ml.evaluation import RegressionEvaluator







# # this ptogram is to Recommender system user-user using Spark

# # load data
# data = pd.read_csv('ratings_t.csv') 
# games = pd.read_csv('games_t.csv')

# # drop columns of release data, summery and meta score
# games.drop(games.columns[[2,3,4]], axis=1, inplace=True)

# # merge data matching game_id 
# merged_data = pd.merge(data, games, on='game_id')

# # create matrix row->game_id, column->user_id, value->rating
# matrix = merged_data.pivot_table(index='game_id', columns='user_id', values='rating')



# print(matrix)

# # create spark session
# spark = pyspark.sql.SparkSession.builder.getOrCreate()
# print(spark)

# # create spark dataframe with header and infer schema
# df = spark.createDataFrame(matrix, )
# df.show()


# # create spark dataframe


























###### Step 1: Import Python Libraries
# Data processing
import pandas as pd
import numpy as np
import scipy.stats
# Visualization
import seaborn as sns
# Similarity
from sklearn.metrics.pairwise import cosine_similarity
import os


data = pd.read_csv('ratings_t.csv')
games = pd.read_csv('games_t.csv')

# drop columns of release data, summery and meta score
games.drop(games.columns[[2,3,4]], axis=1, inplace=True)

# merge data matching game_id 
merged_data = pd.merge(data, games, on='game_id')

# create matrix row->game_id, column->user_id, value->rating
matrix = merged_data.pivot_table(index='game_id', columns='user_id', values='rating')

# save matrix to file using numpy
# np.save('matrix.npy', matrix)

# read matrix from file 
# matrix = np.load('matrix.npy')

# # normalize data
# Normalize user-item matrix
matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 'rows')
matrix_norm.head()
###### Step 6: Identify Similar Users
# User similarity matrix using Pearson correlation
user_similarity = matrix_norm.T.corr()
user_similarity.head()
# User similarity matrix using cosine similarity
user_similarity_cosine = cosine_similarity(matrix_norm.fillna(0))
user_similarity_cosine
# Number of similar users
n = 10
# User similarity threashold
user_similarity_threshold = 0.3
# Get top n similar users
similar_users = user_similarity[user_similarity[picked_userid]>user_similarity_threshold][picked_userid].sort_values(ascending=False)[:n]
# Print out top n similar users
print(f'The similar users for user {picked_userid} are', similar_users)
###### Step 7: Narrow Down Item Pool
# Remove movies that have been watched
picked_userid_watched = matrix_norm[matrix_norm.index == picked_userid].dropna(axis=1, how='all')
picked_userid_watched
# Movies that similar users watched. Remove movies that none of the similar users have watched
similar_user_movies = matrix_norm[matrix_norm.index.isin(similar_users.index)].dropna(axis=1, how='all')
similar_user_movies
# Remove the watched movie from the movie list
similar_user_movies.drop(picked_userid_watched.columns,axis=1, inplace=True, errors='ignore')
# Take a look at the data
similar_user_movies
###### Step 8: Recommend Items
# A dictionary to store item scores
item_score = {}
# Loop through items
for i in similar_user_movies.columns:
  # Get the ratings for movie i
  movie_rating = similar_user_movies[i]
  # Create a variable to store the score
  total = 0
  # Create a variable to store the number of scores
  count = 0
  # Loop through similar users
  for u in similar_users.index:
    # If the movie has rating
    if pd.isna(movie_rating[u]) == False:
      # Score is the sum of user similarity score multiply by the movie rating
      score = similar_users[u] * movie_rating[u]
      # Add the score to the total score for the movie so far
      total += score
      # Add 1 to the count
      count +=1
  # Get the average score for the item
  item_score[i] = total / count
# Convert dictionary to pandas dataframe
item_score = pd.DataFrame(item_score.items(), columns=['movie', 'movie_score'])
    
# Sort the movies by score
ranked_item_score = item_score.sort_values(by='movie_score', ascending=False)
# Select top m movies
m = 10
ranked_item_score.head(m)
###### Step 9: Predict Scores (Optional)
# Average rating for the picked user
avg_rating = matrix[matrix.index == picked_userid].T.mean()[picked_userid]
# Print the average movie rating for user 1
print(f'The average movie rating for user {picked_userid} is {avg_rating:.2f}')
# Calcuate the predicted rating
ranked_item_score['predicted_rating'] = ranked_item_score['movie_score'] + avg_rating
# Take a look at the data
ranked_item_score.head(m)