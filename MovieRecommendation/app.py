import streamlit as st
import pickle
import pandas as pd
import  requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_matrix[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #Fetch Poster using API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        # print(movies.iloc[i[0]].title)
    return  recommended_movies,recommended_movies_poster


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity_matrix=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

import streamlit as st

selectedmovie = st.selectbox(
'How would you like to be contacted?',movies['title'].values)

st.write('You selected:', selectedmovie)

import streamlit as st

if st.button('Recommend'):
    # names,poster=recommend(selectedmovie)
    # st.write(selectedmovie)
    # for i in recommendations:
    #     st.write(i)
    recommended_movie_names, recommended_movie_posters = recommend(selectedmovie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



