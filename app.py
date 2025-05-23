import  streamlit as st
import pickle
import pandas as pd
import gdown
import os

# Loading the similarity.pkl file from the Google drive


if not os.path.exists('similarity.pkl'):
    url = "https://drive.google.com/uc?id=1sBN2sBzI68blXI2ibmfd1bPkuRXl6Q5-"
    gdown.download(url, 'similarity.pkl', quiet=False)

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommend_movies.append(movies.iloc[i[0]].title)
    
    return recommend_movies

st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
    'Select your movie',
    movies['title'].values
)

if st.button('RECOMMEND'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
