import requests
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout="wide", page_title="Movie-Recommendation-System")


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=11253bd3b7da263cca802fc2ae66dff7&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommend_movies_tags = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api

        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_tags.append(movies.iloc[i[0]].tags)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_poster, recommend_movies_tags


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox('Which movie you want to search?', movies['title'].values)

if st.button('recommend'):
    names, poster, Tags = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text("Movie Name:")
        st.text(names[0])
        st.image(poster[0])
        # st.text("Description:")
        # st.text(Tags[0])
        expander = st.expander("Description")
        expander.write(Tags[0])

    with col2:
        st.text("Movie Name:")
        st.text(names[1])
        st.image(poster[1])
        # st.text("Description:")
        # st.text(Tags[1])
        expander = st.expander("Description")
        expander.write(Tags[1])

    with col3:
        st.text("Movie Name:")
        st.text(names[2])
        st.image(poster[2])
        # st.text("Description:")
        # st.text(Tags[2])
        expander = st.expander("Description")
        expander.write(Tags[2])

    with col4:
        st.text("Movie Name:")
        st.text(names[3])
        st.image(poster[3])
        # st.text("Description:")
        # st.text(Tags[3])
        expander = st.expander("Description")
        expander.write(Tags[3])

    with col5:
        st.text("Movie Name:")
        st.text(names[4])
        st.image(poster[4])
        # st.text("Description:")
        # st.text(Tags[4])
        expander = st.expander("Description")
        expander.write(Tags[4])
