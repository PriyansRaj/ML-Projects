import streamlit as  st
import pickle
import pandas as pd
import requests
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movie = pd.DataFrame(movie_dict)
st.title("Movie Recommender System")
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(title):
    movie_index = movie[movie['title'] == title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]

    recommended_movies  =[]
 
    for i in movie_list:
      
        recommended_movies.append(movie.iloc[i[0]].title)
    return recommended_movies

selected_movie_name = st.selectbox(
    'Select the movie',
     movie['title'].values
)

if st.button("Recommend"):
    name = recommend(selected_movie_name)
    for i in range(len(name)):
        st.text(name[i])
