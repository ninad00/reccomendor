import streamlit as st
import pickle
import requests
from sklearn.cluster import KMeans
import numpy as np

userid=st.session_state.user_index

st.set_page_config(page_title="Your Next Binge", page_icon="🍿", layout="wide")

movielist=pickle.load(open('pages/movies1.pkl', 'rb'))
df1=pickle.load(open('pages/df1.pkl', 'rb'))
df_for_content=pickle.load(open('pages/df_fr_content.pkl', 'rb'))
similar=pickle.load(open('pages/similar.pkl', 'rb'))
usermatrix=pickle.load(open('s.pkl', 'rb'))
users=pickle.load(open('pages/users.pkl', 'rb'))


def getposter(id):
    url = "https://api.themoviedb.org/3/movie/{movieid}?language=en-US"
    url=url.format(movieid=id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YzMyNTkzNmEzMzJiZjE4MGI2ODUzZDc2M2VhYzY4ZSIsIm5iZiI6MTczODU4ODIwMi4yMDcsInN1YiI6IjY3YTBjMDJhNmI2MDkxMThkMTI2MjRiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CwAaEK2UjLYKURHorgitvhdfeO5d81eyc3ab9YvjS6A"
    }
    response = requests.get(url, headers=headers)
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original"+data['poster_path']


def recommend(movie):
    idx=df_for_content[df_for_content["title"]==movie].index[0]
    frthatmovie=similar[idx]
    movie_list=sorted(list(enumerate(frthatmovie)),reverse=True,key=lambda x:x[1])[1:6]
    final_list=[]
    final_poster_list=[]
    for i in movie_list:
        x,y=i
        tmdbid=df_for_content.iloc[i[0]].id
        final_poster_list.append(getposter(tmdbid))
        final_list.append(df_for_content['title'][x])
    return final_list,final_poster_list


kmeans = KMeans(n_clusters=6, random_state=42)
kmeans.fit(usermatrix)

def user_recommend(index):
    user_cluster = kmeans.predict(usermatrix[index].reshape(1, -1))[0]
    cluster_users = np.where(kmeans.labels_ == user_cluster)[0]
    cluster_ratings = usermatrix[cluster_users]
    predicted_ratings = cluster_ratings.mean(axis=0)
    unrated_items = np.where(usermatrix[index] == 0)[0]
    recommended_items = unrated_items[np.argsort(predicted_ratings[unrated_items])[::-1]][0:5]
    final_list=[]
    final_poster_list=[]
    for x in recommended_items:
        id=df1.iloc[x]['id']
        final_poster_list.append(getposter(id))
        final_list.append(df1['title'][x])
    return final_list,final_poster_list

def top5():
    movie_ratings = df1.groupby("title")["rating"].mean().reset_index()
    top_movies = movie_ratings.sort_values(by="rating", ascending=False).head(5)
    final_list=[]
    final_poster_list=[]
    for x in top_movies:
        id=df1.iloc[x]['id']
        final_poster_list.append(getposter(id))
        final_list.append(df1['title'][x])
    return final_list,final_poster_list


st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
        }
        .title-text {
            font-family: 'Arial', sans-serif;
            color: #f5c518;
            text-align: center;
            font-size: 40px;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #333;
            color: #f5c518;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }
        .stselectbox>div>div {
            background-color: #222;
            color: #e0e0e0;
            font-size: 16px;
            padding: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title-text'>Your Next Binge 🍿</div>", unsafe_allow_html=True)

option = st.selectbox(
        "What's on your Mind",
        movielist,
    )

if st.button(f"Because you watched {option}"):
    recommendations,posters=recommend(option)
    count=-1

    col1, col2, col3,col4,col5 = st.columns(5)

    st.markdown(
        """
        <style>
        .column-text {
            font-family: 'Georgia', serif;
            font-size: 20px;
            color: darkred;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with col1:

        st.write(recommendations[0])
        st.image(posters[0])

    with col2:
        st.write(recommendations[1])
        st.image(posters[1])

    with col3:
        st.write(recommendations[2])
        st.image(posters[2])

    with col4:
        st.write(recommendations[3])
        st.image(posters[3])

    with col5:
        st.write(recommendations[4])
        st.image(posters[4])

else:
    st.write("")




st.header("Popular movies for you", divider="gray")
recommendations, posters = user_recommend(userid)
col1, col2, col3, col4, col5 = st.columns(5)
st.markdown(
            """
            <style>
            .column-text {
                font-family: 'Georgia', serif;
                font-size: 20px;
                color: darkred;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
with col1:
    st.write(recommendations[0])
    st.image(posters[0])

with col2:
    st.write(recommendations[1])
    st.image(posters[1])

with col3:
    st.write(recommendations[2])
    st.image(posters[2])

with col4:
    st.write(recommendations[3])
    st.image(posters[3])

with col5:
    st.write(recommendations[4])
    st.image(posters[4])



