import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
base='dark'
backgroundColor="ff0099"
def poster(id):
    Response=requests.get('http://www.omdbapi.com/?t={}&apikey=d6d0520d'.format(id))
    data=Response.json()
    # print(data)
    return data['Poster']
movies_dic = pickle.load(open('moviesdic.pkl','rb'))
movies=pd.DataFrame(movies_dic)
st.title("Movie Recommendation System")
dismat=pickle.load(open('similarity.pkl','rb'))
def recom(movie):
    ind=movies[movies['title']==movie].index[0]
    dis=sorted(enumerate(dismat[ind]),reverse=True,key=lambda x:x[1])[1:6]
    re=[]
    po=[]
    for i in dis:
        po.append(poster(movies.iloc[i[0]].title))
        re.append(movies.iloc[i[0]].title)
    return re,po
smn =st.selectbox(
    'Enter the movie name',
    (movies['title'])
)
if(st.button('recommend')):
    re,po=recom(smn)
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(re[0])
        st.image(po[0])
    with col2:
        st.text(re[1])
        st.image(po[1])
    with col3:
        st.text(re[2])
        st.image(po[2])
    with col4:
        st.text(re[3])
        st.image(po[3])
    with col5:
        st.text(re[4])
        st.image(po[4])

        

