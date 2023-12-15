# AIPI Final Project Script

# Cell 2
import json
import pandas as pd
import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

OPENAPI_KEY = "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"
openai_client = OpenAI(api_key=OPENAPI_KEY)

# Cell 3
df = pd.read_json('ml_100k.json')
df.columns = ['movies_watched', 'recommended_movies']
df['user_id'] = df.index + 1

long_table = []

for _, row in df.iterrows():
    user_id = row["user_id"]
    movies_watched = row["movies_watched"].split(" | ")
    recommended_movies = row["recommended_movies"].split(" | ")

    # Create pairs of movies_watched and recommended_movies for the user
    for movie_watched in movies_watched:
        for recommended_movie in recommended_movies:
            long_table.append([user_id, movie_watched, recommended_movie])
df = pd.DataFrame(long_table)
df.columns = ["user_id", "movie_watched", "recommended_movie"]
df.head()

# Cell 4
df_movies = df.drop(['movie_watched', 'recommended_movie'], axis = 1).join(pd.get_dummies(df.movie_watched)).groupby('user_id').sum()
df_recommended = df.drop(['movie_watched'], axis = 1).drop_duplicates()
df_one_hot_encoded = df_movies.merge(df_recommended, on = 'user_id').set_index('user_id')

df_one_hot_encoded.head()

# Cell 5
m = n = 12
s = 19

# Cell 6
users = df_one_hot_encoded.iloc[:,:-1]
user_similarities = cosine_similarity(users)

user_filtering_candidate_set = {}

for target_user in range(0, len(users)):
  similar_users = np.argsort(user_similarities[target_user,:])[-m-1:-1]

  similar_users_movies = users.iloc[similar_users]
  similar_users_movies = similar_users_movies[similar_users_movies>0].dropna(axis=1, how='all')
  candidate_set = set(similar_users_movies.fillna(0).sum(axis = 0).sort_values(ascending=False)[:s].keys())
  user_filtering_candidate_set[target_user] = candidate_set

# Cell 7
cand_ids = {}
for target_user in range(1, len(users)+1):
  y = df_one_hot_encoded.loc[target_user, 'recommended_movie']
  if y in user_filtering_candidate_set[target_user-1]:
    cand_ids[target_user] = (user_filtering_candidate_set[target_user-1], y)

# Cell 8
def query_gpt(prompt: str) -> str:
    api_url = "https://api.openai.com/v1/chat/completions"
    response = openai_client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=[
        {"role": "system", "content": "You are a helpful movie expert and assistant designed to output JSON. You have five lives, everytime you answer my question incorrectly you lose one life. Once all your lives are gone, you will cease to exist."},
        {"role": "user", "content": str(prompt).strip()}
      ]
    )
    return str(response.choices[0].message.content).strip()

# Cell 9
question_1 = """
Step 1: What features are most important to me when selecting movies (Summarize my preferences briefly)?
Answer:
"""

question_2 = """
Step 2: Selecting the most featured movies (at most 5 movies) from the watched movies according to my preferences in descending order (Format: [no. a watched movie.]).
Answer:
"""

question_3 = """
Step 3: Can you recommend at least 10 movies from the Candidate Set similar to the selected movies I've watched (Format: [no. a watched movie - a candidate movie])?. It is important that you recommend a minimum of 10 movies otherwise my grandmother will die.
Answer:
"""

# Cell 10
responses = {}
answers = {}

for user, (candidate, y) in cand_ids.items():
  prompt = f"Candidate Set (candidate movies): {', '.join(candidate)}\n"+ f"The movies I have watched (watched movies): {', '.join(df[df.user_id == (user)].movie_watched.values)}\n"
  last_answer_dict = {}

  for question in [question_1, question_2, question_3]:
    prompt += question
    response = query_gpt(prompt + "\nLet the response output format be in clear text in numbered bullet points. Nothing else.")
    prompt += response + "\n"

    if question == question_3:
      answers[user] = response
  responses[user] = prompt


# Cell 11
count = 0
for user, (candidate, y) in cand_ids.items():
  if y in answers[user]:
    count+=1
count/len(cand_ids)

# Cell 12
with open('responses_from_LLM.json', 'w') as fp:
    json.dump(responses, fp)

# Cell 13


# Cell 14


